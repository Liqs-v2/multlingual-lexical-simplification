from typing import List, Dict

from lexical_simplifier import LexicalSimplifier
from utils.data_provider import DataProvider
from utils.bench_ls_data_provider import BenchLSDataProvider
from utils.germaneval_data_provider import GermanEvalDataProvider
from language import Language


class BenchmarkSuite:
    testee_model: LexicalSimplifier = None
    languages: List[Language] = None
    _datasets: Dict[Language: List[DataProvider]] = None

    def __init__(self, testee_model: LexicalSimplifier, languages: List[Language]):
        self.testee_model = testee_model
        self.languages = languages

        # TODO this should be dynamically created based on the languages passed

        self._datasets = {}
        for language in self.languages:
            self._datasets[language] = [

            ]


        self._datasets = {
            Language.DE: [GermanEvalDataProvider(
                '/content/drive/MyDrive/nlp_ss24/multilingual-lexical-simplification/data/germeval/train-dataset.xml',
                '/content/drive/MyDrive/nlp_ss24/multilingual-lexical-simplification/data/germeval/train-dataset.gold')],
            Language.EN: [BenchLSDataProvider(
                '/content/drive/MyDrive/nlp_ss24/multilingual-lexical-simplification/data/BenchLS/BenchLS.txt')]
        }

    def run(self):
        # run the benchmark suite with the specified config (ie attrs)
        pass

    def enable_language(self, language: Language):
        self.languages.append(language)

    def enable_languages(self, languages: List[Language]):
        for language in languages:
            self.enable_language(language)

    def disable_language(self, language: Language):
        self.languages.remove(language)

    def disable_languages(self, languages: List[Language]):
        for language in languages:
            self.disable_language(language)