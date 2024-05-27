from typing import List, Dict, Set

from lexical_simplifier import LexicalSimplifier
from utils.data_provider import DataProvider
from utils.bench_ls_data_provider import BenchLSDataProvider
from utils.germaneval_data_provider import GermanEvalDataProvider
from language import Language

import numpy as np
import pandas as pd


class BenchmarkSuite:
    """
    Provides a single point of contact for benchmarking lexical simplification systems.

    Attributes:
        testee_model (LexicalSimplifier): The lexical simplification model which an instance of this class will benchmark.
        languages: (Set[Language]): The languages for which testee_model will be benchmarked.
        _AVAILABLE_DATASETS (Dict[Language, List[DataProvider]]): The currently implemented and available datasets.
            This is constant and serves as a baseline to compare against when synchronizing the enabled languages and
            datasets.
        _enabled_datasets (Dict[Language, List[DataProvider]]): The datasets on which testee_model will be evaluated.
            This is either a subset of _available_datasets or, if a full benchmark is performed, equal to it.
    """

    testee_model: LexicalSimplifier = None
    languages: Set[Language] = None
    # Rather than dynamically initializing self._datasets right away via self inspection and the like,
    # I decided to simply remove unused languages after the fact.
    # This tradeoff is essentially compute vs memory bound and since the DataProvider implementations
    # are constrained to lazily fetch the datasets via provide_data_as_numpy_array,
    # these objects are very lightweight.
    _AVAILABLE_DATASETS: Dict[Language, List[DataProvider]] = {
        Language.DE: [GermanEvalDataProvider()],
        Language.EN: [BenchLSDataProvider()]
    }
    _enabled_datasets: Dict[Language, List[DataProvider]] = {}

    def __init__(self, testee_model: LexicalSimplifier, languages: Set[Language]):
        """
        Creates a BenchmarkSuite instance for a specific LexicalSimplifier model. The model is going to be benchmarked
        on the languages configured in this class.

        Args:
            testee_model (LexicalSimplifier): The lexical simplification model to benchmark.
            languages: (Set[Language]): The languages for which testee_model will be benchmarked.
        """
        self.testee_model = testee_model
        self.languages = languages

        self.__enable_datasets_by_languages()

    def run(self):
        results = pd.DataFrame()

        for language in self.languages:
            for dataset in self._enabled_datasets[language]:
                benchmark_data = dataset.provide_data_as_numpy_array()

                results.loc[f'{language.name}-{dataset.__name__}'] = self.__benchmark_model_on(benchmark_data)

        results.to_csv('/content/drive/MyDrive/nlp_ss24/multilingual-lexical-simplification/data/benchmark_results.csv',
                       index=True, index_label='run', header=True)

    def __benchmark_model_on(self, benchmark_data: np.ndarray):
        # TODO: Generate substitutions for each entry in benchmark_data
        #   Then evaluate and return in the same format across all models
        pass

    def enable_language(self, language: Language):
        """
        Enables the specified language and related datasets for benchmarking.
        Updates the state of self.__enabled_datasets.

        Args:
            language (Language): The language to enable for benchmarking.
        """
        self.languages.add(language)

        self.__enable_datasets_by_languages()

    def enable_languages(self, languages: List[Language]):
        """
            Enables the specified languages and related datasets for benchmarking.
            Updates the state of self.__enabled_datasets.

            Args:
                languages (List[Language]): The languages to enable for benchmarking.
        """
        for language in languages:
            self.enable_language(language)

        self.__enable_datasets_by_languages()

    def disable_language(self, language: Language):
        """
            Disables the specified language and related datasets for benchmarking.
            Updates the state of self.__enabled_datasets.

            Args:
                language (Language): The language to disable for benchmarking.
        """
        self.languages.remove(language)

        self.__disable_datasets_by_languages()

    def disable_languages(self, languages: List[Language]):
        """
            Disables the specified languages and related datasets for benchmarking.
            Updates the state of self.__enabled_datasets.

            Args:
                languages (List[Language]): The languages to disable for benchmarking.
        """
        for language in languages:
            self.disable_language(language)

        self.__disable_datasets_by_languages()

    def __enable_datasets_by_languages(self):
        """
            Updates the self._enabled_datasets to account for additional languages that should
            be benchmarked.

            Computes the set difference languages \ enabled_datasets.keys since this function is called
            whenever additional languages are enabled. Thus follows:
            | languages | > | enabled_datasets.keys |
        """
        languages_to_enable = self.languages.difference(set(self._enabled_datasets.keys()))

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
        languages_to_disable = set(self._enabled_datasets.keys()).difference(self.languages)

        for language_to_disable in languages_to_disable:
            del self._enabled_datasets[language_to_disable]


