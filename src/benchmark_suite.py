from typing import List, Dict

import numpy as np
import pandas as pd
from tqdm import tqdm

from evaluator import Evaluator
from language import Language
from lexical_simplifier import LexicalSimplifier
from utils.bench_ls_data_provider import BenchLSDataProvider
from utils.data_provider import DataProvider
from utils.germaneval_data_provider import GermanEvalDataProvider
from utils.lexmturk_data_provider import LexMTurkDataProvider
from utils.nnseval_data_provider import NNSevalDataProvider
from utils.tsar_en_data_provider import TsarENDataProvider


class BenchmarkSuite:
    """
    Provides a single point of contact for benchmarking lexical simplification systems.

    Attributes:
        testee_model (LexicalSimplifier): The lexical simplification model which an instance of this class will benchmark.
        language_configurations: (Set[Language]): The languages for which testee_model will be benchmarked.
        _AVAILABLE_DATASETS (Dict[Language, List[DataProvider]]): The currently implemented and available datasets.
            This is constant and serves as a baseline to compare against when synchronizing the enabled languages and
            datasets.
        _enabled_datasets (Dict[Language, List[DataProvider]]): The datasets on which testee_model will be evaluated.
            This is either a subset of _available_datasets or, if a full benchmark is performed, equal to it.
    """

    testee_model: LexicalSimplifier = None
    language_configurations: Dict[Language, str] = None
    # Rather than dynamically initializing self._datasets right away via self inspection and the like,
    # I decided to simply remove unused languages after the fact.
    # This tradeoff is essentially compute vs memory bound and since the DataProvider implementations
    # are constrained to lazily fetch the datasets via provide_data_as_numpy_array,
    # these objects are very lightweight.
    _AVAILABLE_DATASETS: Dict[Language, List[DataProvider]] = {
        Language.DE: [GermanEvalDataProvider()],
        Language.EN: [BenchLSDataProvider(), LexMTurkDataProvider(), NNSevalDataProvider(), TsarENDataProvider()]
    }
    _enabled_datasets: Dict[Language, List[DataProvider]] = {}

    def __init__(self, testee_model: LexicalSimplifier, language_configurations: Dict[Language, str]):
        """
        Creates a BenchmarkSuite instance for a specific LexicalSimplifier model. The model is going to be benchmarked
        on the languages configured in this class.

        Args:
            testee_model (LexicalSimplifier): The lexical simplification model to benchmark.
            languages: (Dict[Language, str]): A dictionary where the keys are the languages for which testee_model
                will be benchmarked and the values are the prompts used for the benchmarking of the models.
        """
        self.testee_model = testee_model
        self.language_configurations = language_configurations

        self.__enable_datasets_by_languages()

    def run(self):
        """
        Runs the benchmark pipeline and evaluates self.testee_model on the datasets that are currently enabled.
        The result of the benchmark is persisted in 'data/benchmark_results_<model_clazz_name>.csv'
        """
        results = pd.DataFrame(columns=['potential', 'precision', 'recall', 'f1', 'map_at_k', 'potential_at_k',
                                        'accuracy_at_k_top_1'])

        for language in self.language_configurations.keys():
            print(f'Benchmarking model on {language.name} ...')
            self.testee_model.set_pattern(self.language_configurations[language])

            for dataset in self._enabled_datasets[language]:
                print(f'Benchmarking model on {dataset.__class__.__name__}...')
                benchmark_data = dataset.provide_data_as_numpy_array()

                results.loc[f'{language.name}-{dataset.__class__.__name__}'] = self.__benchmark_model_on(benchmark_data)

        results.to_csv('/content/drive/MyDrive/nlp_ss24/multilingual-lexical-simplification/data/'
                       f'benchmark_results_{self.testee_model.__class__.__name__}_'
                       f'{self.testee_model.model.config.name_or_path.replace("/", "-")}.csv',
                       index=True, index_label='run', header=True)

    def __benchmark_model_on(self, benchmark_data: np.ndarray) -> pd.Series:
        potential = 0
        precision = 0
        recall = 0
        f1 = 0
        map_at_k = 0
        potential_at_k = 0
        accuracy_at_k_top_1 = 0

        # TODO This is why we arent batch processing, we sequentially loop
        for sample in tqdm(benchmark_data, desc='Benchmarking'):
            sentence = sample[0]
            complex_word = sample[1]
            ground_truth_substitutions = sample[3]

            # To easily capture implementations not supporting a specific number of substitutions,
            # we do not pass top_k here and simply use the default in those cases.
            predicted_substitutions = self.testee_model.generate_substitutions_for(complex_word, sentence)

            sample_potential, sample_precision, sample_recall, sample_f1, sample_map_at_k, sample_potential_at_k, sample_accuracy_at_k_top_1 = Evaluator.evaluate(
                ground_truth_substitutions, predicted_substitutions
            )

            if sample_potential:
                potential += 1
            precision += sample_precision
            recall += sample_recall
            f1 += sample_f1
            map_at_k += sample_map_at_k
            if sample_potential_at_k:
                potential_at_k += 1
            if sample_accuracy_at_k_top_1:
                accuracy_at_k_top_1 += 1

        potential = potential / len(benchmark_data)
        precision = precision / len(benchmark_data)
        recall = recall / len(benchmark_data)
        f1 = f1 / len(benchmark_data)
        map_at_k = map_at_k / len(benchmark_data)
        potential_at_k = potential_at_k / len(benchmark_data)
        accuracy_at_k_top_1 = accuracy_at_k_top_1 / len(benchmark_data)

        return pd.Series({
                    'potential': round(potential, 4),
                    'precision': round(precision, 4),
                    'recall': round(recall, 4),
                    'f1': round(f1, 4),
                    'map_at_k': round(map_at_k, 4),
                    'potential_at_k': round(potential_at_k, 4),
                    'accuracy_at_k_top_1': round(accuracy_at_k_top_1, 4)
                })

    def enable_language(self, language: Language, prompt: str):
        """
        Enables the specified language and related datasets for benchmarking.
        Updates the state of self.__enabled_datasets.

        Args:
            language (Language): The language to enable for benchmarking.
            prompt (str): The prompt to use for the benchmarking of the model on the specified language.
        """
        self.language_configurations[language] = prompt

        self.__enable_datasets_by_languages()

    def enable_languages(self, language_configuration: Dict[Language, str]):
        """
            Enables the specified languages and related datasets for benchmarking.
            Updates the state of self.__enabled_datasets.

            Args:
                language_configuration (Dict[Language, str]): The languages to enable for benchmarking and
                    the prompts to use for the benchmarking of the model.
        """
        self.language_configurations.update(language_configuration)

        self.__enable_datasets_by_languages()

    def disable_language(self, language: Language):
        """
            Disables the specified language and related datasets for benchmarking.
            Updates the state of self.__enabled_datasets.

            Args:
                language (Language): The language to disable for benchmarking.
        """
        del self.language_configurations[language]

        self.__disable_datasets_by_languages()

    def disable_languages(self, languages: List[Language]):
        """
            Disables the specified languages and related datasets for benchmarking.
            Updates the state of self.__enabled_datasets.

            Args:
                languages (List[Language]): The languages to disable for benchmarking.
        """
        for language in languages:
            if language in self.language_configurations:
                del self.language_configurations[language]

        self.__disable_datasets_by_languages()

    def __enable_datasets_by_languages(self):
        """
            Updates the self._enabled_datasets to account for additional languages that should
            be benchmarked.

            Computes the set difference languages \ enabled_datasets.keys since this function is called
            whenever additional languages are enabled. Thus follows:
            | languages | > | enabled_datasets.keys |
        """
        languages_to_enable = set(self.language_configurations.keys()).difference(set(self._enabled_datasets.keys()))

        for language_to_enable in languages_to_enable:
            self._enabled_datasets[language_to_enable] = self._AVAILABLE_DATASETS[language_to_enable]

    def __disable_datasets_by_languages(self):
        """
            Updates the self._enabled_datasets to account for languages that should not
            be benchmarked.

            Computes the set difference enabled_datasets.keys \ languages since this function is called
            whenever languages are disabled. Thus follows:
            | languages | < | enabled_datasets.keys |
        """
        languages_to_disable = set(self._enabled_datasets.keys()).difference(set(self.language_configurations.keys()))

        for language_to_disable in languages_to_disable:
            del self._enabled_datasets[language_to_disable]
