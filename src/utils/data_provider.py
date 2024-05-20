import abc
import numpy as np
from abc import ABCMeta

# DISCLAIMER: This file was authored in an IDE with Github Copilot enabled.


class DataProvider(metaclass=ABCMeta):

    @abc.abstractmethod
    def provide_data_as_numpy_array(self, filename: str) -> np.ndarray:
        """
        Reads the data from the given file and returns it as a numpy array. The format the data that is returned
        must conform to is specified in the documentation of the return value of this method.

        Args:
            filename: The path to the file containing the data.

        Returns:
            A numpy array where each row corresponds to a datapoint from a lexical simplification dataset.
            Each row should contain the following elements:
                - The original sentence
                - The complex word to be simplified
                - The position of the complex word in the sentence (0-indexed)
                - A dictionary containing the substitutions for the complex word, where the keys are the ranks of the
                    substitutions and one or more candidate substitutions are stored as a list for each rank.
        """
        raise NotImplementedError("Please implement this method in the subclass.")