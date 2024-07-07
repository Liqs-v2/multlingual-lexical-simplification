import numpy as np
from src.utils.create_script import get_dataset
from src.utils.data_provider import DataProvider

# DISCLAIMER: This file was authored in an IDE with Github Copilot enabled.
class GPT_Created_Data_Provider(DataProvider):

    _filename = "/home/caro/MLS/multilingual-lexical-simplification/create_script.py"


    def provide_data_as_numpy_array(self):
        dataset = get_dataset()

        new_data = []
        for data in dataset:
            sentence = str(data[0])
            complex_word = str(data[1])
            position = int(data[2])
            substitutes = data[3]

            if complex_word not in sentence:
                continue

            new_position = self.getPosition(sentence=sentence,complex_word=complex_word)

            new_line = [complex_word, complex_word, new_position,substitutes]
            new_data.append(new_line)

        return np.array(new_data, dtype=object)


    def getPosition(self,sentence,complex_word):
        word = (complex_word.split())[0]
        words = sentence.split()
        try:
            index = words.index(word)
        except:
            index = next((i for i, s in enumerate(words) if word in s), None)
        return index

