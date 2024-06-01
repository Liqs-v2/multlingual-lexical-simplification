# Preprocess the LexMTurk dataset into a numpy array
import numpy as np

from src.utils.data_provider import DataProvider

# DISCLAIMER: This file was authored in an IDE with Github Copilot enabled.

class TsarENDataProvider(DataProvider):
    _filename = '/content/drive/MyDrive/nlp_ss24/multilingual-lexical-simplification/tsar_en/tsar_en.txt'

    def get_position(self, word, sentence):
        """
        Returns the position of the word in the sentence. (Taken from germaneval_data_provider)
        """
        words = sentence.split()
        try:
            index = words.index(word)
        except:
            index = next((i for i, s in enumerate(words) if word in s), None)
        return index
    
    def process_line(self, line):
        parts = line.strip().split("\t")
        
        sentence = parts[0]
        complex_word = parts[1]
        position = self.get_position(complex_word, sentence)

        # Count the occurrences and group by counts simultaneously
        count_dict = {}
        for item in parts[2:]:
            count_dict[item] = count_dict.get(item, 0) + 1

        grouped_count_dict = {}
        for item, count in count_dict.items():
            if count in grouped_count_dict:
                grouped_count_dict[count].append(item)
            else:
                grouped_count_dict[count] = [item]

        # Sort by counts in descending order and create the final ranked dictionary
        substitution_dict = {rank + 1: items for rank, (count, items) in enumerate(sorted(grouped_count_dict.items(), key=lambda x: x[0], reverse=True))}

        return [sentence, complex_word, position, substitution_dict]
    
    def provide_data_as_numpy_array(self):
        with open(self._filename, "r", encoding="utf-8") as file:
            lines = file.readlines()

        processed_lines = [self.process_line(line) for line in lines]
        return np.array(processed_lines, dtype=object)