from typing import List, Dict

from lexical_simplifier import LexicalSimplifier
from utils.data_provider import DataProvider
from language import Language


class BenchmarkSuite:

    testee_model: LexicalSimplifier = None
    languages: List[Language] = None
    datasets: Dict[str: List[DataProvider]] = {
        "de": ["germeval, germeval2015"],
        "en": ["benchls"]
    }

    def __init__(self, testee_model: LexicalSimplifier, languages: List[Language]):
        self.testee_model = testee_model
        self.languages = languages

    def run(self):
        # run the benchmark suite with the specified config (ie attrs)
        pass

    def add_language(self, language: Language):
        # add a language to the benchmark suite
        pass

    def add_languages(self, languages: List[Language]):
        # add multiple languages to the benchmark suite
        pass

    def remove_language(self, language: Language):
        # remove a language from the benchmark suite
        pass

    def remove_languages(self, languages: List[Language]):
        # remove multiple languages from the benchmark suite
        pass

    def disable_dataset(self, dataset: str):
        # disable a dataset from the benchmark suite
        pass

    def disable_datasets(self, datasets: List[str]):
        # disable multiple datasets from the benchmark suite
        pass

