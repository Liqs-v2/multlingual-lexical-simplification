import xml.etree.ElementTree as ET

import numpy as np

from src.utils.data_provider import DataProvider


# DISCLAIMER: This file was authored in an IDE with Github Copilot enabled.


class GermanEvalDataProvider(DataProvider):

    _path_to_data = '/content/drive/MyDrive/nlp_ss24/multilingual-lexical-simplification/data/germeval/train-dataset.xml'
    _path_to_substitutes = '/content/drive/MyDrive/nlp_ss24/multilingual-lexical-simplification/data/germeval/train-dataset.gold'

    def get_position(self, word, sentence):
        """
        Returns the position of the word in the sentence.
        """
        words = sentence.split()
        try:
            index = words.index(word)
        except:
            index = next((i for i, s in enumerate(words) if word in s), None)
        return index

    def get_complex_words(self, root):
        """
        Returns all complex words in the dataset as a NumPy array.
        :param root:
        :return:
        """
        complexWords = []
        for instance in root.findall(".//instance"):
            head_word = instance.find(".//head").text
            complexWords.append(head_word)
        return np.array(complexWords)

    def get_sentences(self, root):
        """
        Returns all sentences in the dataset as a NumPy array.
        """
        text = []
        for child in root:
            sentence = ''.join(child.itertext())
            cleaned_text = sentence.replace('\n', ' ')
            sentences = cleaned_text.split('. ')
            sentences_without_whitespace = [s.strip() for s in sentences]
            # Remove empty strings from the list
            filtered_list = [item for item in sentences_without_whitespace if item != ""]
            text.extend(filtered_list)
        # Convert the list to a NumPy array
        sentences = np.array(text)
        return sentences

    def read_dataset_in(self, path):
        # Parse the XML file
        tree = ET.parse(path)
        return tree.getroot()

    def read_substitues_in(self, path):
        # Read the substitues file
        with open(path, 'r') as file:
            # Remove newline characters and store each line as an element in a list
            lines = [line.strip() for line in file.readlines()]

        substitutions_list = []
        for line in lines:
            line = line.split("::")
            substitutes = line[1].split(";")
            substitutes = [s for s in substitutes if s!=""]

            # Parse the substitutions into a dictionary
            substitution_dict = {}
            for substitute in substitutes:
                substitute = substitute.strip()
                rank = int(substitute[len(substitute)-1:])  
                substitute = substitute[:len(substitute)-2] 
                if rank in substitution_dict:
                    substitution_dict[rank].append(substitute)
                else:
                    substitution_dict[rank] = [substitute]
            # ranks in wrong order
            # Assign correct ranks
            new_rankings = {}
            for index,(rank,substitutes) in enumerate(substitution_dict.items()):
                new_rankings[index+1] = substitutes

            substitutions_list.append(new_rankings)

        return substitutions_list

    def provide_data_as_numpy_array(self):
        substitutes = self.read_substitues_in(self._path_to_substitutes)
        root = self.read_dataset_in(self._path_to_data)
        complexWords = self.get_complex_words(root)
        sentences = self.get_sentences(root)

        processedDate = []
        for index, substitute in enumerate(substitutes):
            processedLine = [sentences[index], complexWords[index], self.get_position(complexWords[index], sentences[index]),
                             substitute]
            processedDate.append(processedLine)

        return np.array(processedDate, dtype=object)
