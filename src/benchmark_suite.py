from typing import List, Dict

from lexical_simplifier import LexicalSimplifier
from utils.data_provider import DataProvider


class BenchmarkSuite:

    testee_model: LexicalSimplifier = None
    languages: List[str] = None # TODO transform str into enum for robustness
    datasets: Dict[str: List[DataProvider]] = None

    def __init__(self):
        pass

    def run(self):
        # run the benchmark suite with the specified config (ie attrs)
        pass

    def add_language(self, language: str):
        # add a language to the benchmark suite
        pass

    def add_languages(self, languages: List[str]):
        # add multiple languages to the benchmark suite
        pass

    def remove_language(self, language: str):
        # remove a language from the benchmark suite
        pass

    def remove_languages(self, languages: List[str]):
        # remove multiple languages from the benchmark suite
        pass

    def disable_dataset(self, dataset: str):
        # disable a dataset from the benchmark suite
        pass

    def disable_datasets(self, datasets: List[str]):
        # disable multiple datasets from the benchmark suite
        pass

