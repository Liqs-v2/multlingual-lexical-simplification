import abc
import numpy as np
from abc import ABCMeta

from src.language import Language
from typing import List

# DISCLAIMER: This file was authored in an IDE with Github Copilot enabled.


class DataProvider(metaclass=ABCMeta):
    """
    Defines the interfaces for a data provider that reads a lexical simplification dataset from a file and returns it as
    a numpy array for further processing. Note that the variables relating to the path to the dataset should be
    stored as attributes in the implementing subclass and accessed this way. This is to allow for the flexibility of
    changing the path to the dataset without changing the method signature.
    """

    @abc.abstractmethod
    def provide_data_as_numpy_array(self) -> np.ndarray:
        """
        Reads the data from the given file and returns it as a numpy array. The format the data that is returned
        must conform to is specified in the documentation of the return value of this method.

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