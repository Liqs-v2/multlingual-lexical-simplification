# Preprocess the BenchLS dataset into a numpy array
import numpy as np

from src.utils.data_provider import DataProvider


class NNSevalDataProvider(DataProvider):
    _filename = 'data/NNSeval/NNSeval short.txt'

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
        with open(self._filename, "r", encoding="utf-8") as file:
            lines = file.readlines()

        processed_lines = [self.process_line(line) for line in lines]
        return np.array(processed_lines, dtype=object)
