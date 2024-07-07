import numpy as np
from src.utils.create_gpt_set_script import get_dataset
from src.utils.data_provider import DataProvider

# DISCLAIMER: This file was authored in an IDE with Github Copilot enabled.
class GPT_Created_Data_Provider(DataProvider):

    _filename = "/content/drive/MyDrive/nlp_ss24/multilingual-lexical-simplification/src/utils/create_gpt_set_script.py"


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
            new_substitutes = self.delete_matching_words(substitutes, complex_word=complex_word)
            print(new_substitutes)
            new_line = [sentence, complex_word, new_position,new_substitutes]
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

    def delete_matching_words(self,dictionary, complex_word):
        keys_to_delete = []
        for key, word_list in dictionary.items():
            for word in word_list[:]:  
                if word == complex_word:
                    word_list.remove(word)
            if word_list == []:
                keys_to_delete.append(key)

        for key in keys_to_delete:
            dictionary.pop(key)

        # If there are empty entries, shift subsequent keys up by one
        if keys_to_delete:
            new_dictionary = {}
            new_key = 1
            for key in sorted(dictionary.keys()):
                if key not in keys_to_delete:
                    new_dictionary[new_key] = dictionary[key]
                    new_key += 1
            return new_dictionary
        else:
            return dictionary
