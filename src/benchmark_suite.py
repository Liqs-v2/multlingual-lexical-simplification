from typing import List, Dict, Set

from lexical_simplifier import LexicalSimplifier
from utils.data_provider import DataProvider
from utils.bench_ls_data_provider import BenchLSDataProvider
from utils.germaneval_data_provider import GermanEvalDataProvider
from language import Language


class BenchmarkSuite:
    testee_model: LexicalSimplifier = None
    languages: Set[Language] = None
    _available_datasets: Dict[Language, List[DataProvider]] = None
    _enabled_datasets: Dict[Language, List[DataProvider]] = {}

    def __init__(self, testee_model: LexicalSimplifier, languages: Set[Language]):
        self.testee_model = testee_model
        self.languages = languages

        # Rather than dynamically initializing self._datasets right away via self inspection and the like,
        # I decided to simply remove unused languages after the fact.
        # This tradeoff is essentially compute vs memory bound and since the DataProvider implementations
        # are constrained to lazily fetch the datasets via provide_data_as_numpy_array,
        # these objects are very lightweight.
        self._available_datasets = {
            Language.DE: [GermanEvalDataProvider()],
            Language.EN: [BenchLSDataProvider()]
        }

        self.__enable_datasets_by_languages()

    def run(self):
        # run the benchmark suite with the specified config (ie attrs)
        pass

    def enable_language(self, language: Language):
        self.languages.add(language)

        self.__enable_datasets_by_languages()

    def enable_languages(self, languages: List[Language]):
        for language in languages:
            self.enable_language(language)

        self.__enable_datasets_by_languages()

    def disable_language(self, language: Language):
        self.languages.remove(language)

        self.__disable_datasets_by_languages()

    def disable_languages(self, languages: List[Language]):
        for language in languages:
            self.disable_language(language)

        self.__disable_datasets_by_languages()

    def __enable_datasets_by_languages(self):
        languages_to_enable = self.languages.difference(set(self._enabled_datasets.keys()))

        for language_to_enable in languages_to_enable:
            self._enabled_datasets[language_to_enable] = self._available_datasets[language_to_enable]

    def __disable_datasets_by_languages(self):
        languages_to_disable = set(self._enabled_datasets.keys()).difference(self.languages)

        for language_to_disable in languages_to_disable:
            del self._enabled_datasets[language_to_disable]


suite = BenchmarkSuite(LexicalSimplifier, {Language.EN})
suite.disable_language(Language.EN)
suite.enable_languages([Language.EN, Language.DE])
suite.disable_languages([Language.DE])
