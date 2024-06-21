# Preprocess the Alexsis dataset into a numpy array
import numpy as np
import pandas as pd
import numpy as np
from collections import Counter
from collections import defaultdict

from src.utils.data_provider import DataProvider

class TsarPtDataProvider(DataProvider):

    _filename = '/content/drive/MyDrive/nlp_ss24/multilingual-lexical-simplification/data/tsar_pt/tsar2022_pt_test_gold.tsv'

    def provide_data_as_numpy_array(self):
        data = np.genfromtxt(self._filename, delimiter='\t', dtype=None, encoding=None)
        substitutes = data[:, -25:]
        synonyms_as_list = [row.tolist() for row in substitutes]
        
        sorted_lists = []
        for synonyms_list in synonyms_as_list:
            filtered_synonyms_list = [word for word in synonyms_list if word]
            word_counts = Counter(filtered_synonyms_list)
            freq_dict = defaultdict(list)
            for word, count in word_counts.items():
                freq_dict[count].append(word)
            sorted_freq_dict = dict(sorted(freq_dict.items(), reverse=True))
            sorted_lists.append(sorted_freq_dict)

        processed_data = []
        for index, data_values in enumerate(data):
            processed_line = [str(data_values[0]), str(data_values[1]), None,sorted_lists[index]]
            processed_data.append(processed_line)

        return np.array(processed_data, dtype=object)
