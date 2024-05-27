# Preprocess the BenchLS dataset into a numpy array
import numpy as np

from src.utils.data_provider import DataProvider
from src.language import Language


class BenchLSDataProvider(DataProvider):
    # Example usage
    '''
    filename = r"data\BenchLS\BenchLS.txt"
    array = read_file_to_array(filename)
    '''

    # Example output of first line:
    """
    ['in March 1992 , Linux version 0.95 was the first to be capable of running X . This large version number jump was due to a feeling that a version 1.0 with no major missing pieces was imminent .'
     'pieces' 
     35
     {1: ['parts'], 2: ['bits'], 3: ['components'], 4: ['information', 'elements', 'items', 'component', 'part', 'sections']}]
    """

    filename = '/content/drive/MyDrive/nlp_ss24/multilingual-lexical-simplification/data/BenchLS/BenchLS.txt'
    applicable_languages = [Language.EN]

    def __init__(self, filename):
        self.filename = filename


    def process_line(self, line):
        """Process a line from the BenchLS dataset into a numpy array"""
        parts = line.strip().split("\t")
        sentence = parts[0]
        complex_word = parts[1]
        position = int(parts[2])
        substitutions = parts[3:]

        # Parse the substitutions into a dictionary
        substitution_dict = {}
        for substitution in substitutions:
            rank, candidate = substitution.split(":")
            rank = int(rank)
            if rank in substitution_dict:
                substitution_dict[rank].append(candidate)
            else:
                substitution_dict[rank] = [candidate]

        return [sentence, complex_word, position, substitution_dict]

    def provide_data_as_numpy_array(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            lines = file.readlines()

        processed_lines = [self.process_line(line) for line in lines]
        return np.array(processed_lines, dtype=object)
