import abc
from typing import List
from abc import ABCMeta


class LexicalSimplifier(metaclass=ABCMeta):
    """
    An abstract base class for a lexical simplification. Implements a basic initializer and functions for
    setting the model and pattern for the simplifier. The main function to be implemented by subclasses is
    get_substitutions_for, which should return a list of possible substitutions for a given complex word.

    Attributes:
        model: The model used for generating substitutions.
        pattern: The format string used to dynamically build prompts for generating substitutions. In the simplest
            case this could be a string with one placeholder, into which the input sentence with the masked complex
            word is inserted (eg. for a BERT model).
        exemplars: A list of exemplar words used for zero-shot learning. If provided, these will be prepended to the every
            prompt.
    """
    model = None
    pattern: str = None
    exemplars: List[str] = None

    def __init__(self, model, pattern, exemplars):
        if model is None:
            raise ValueError("Please initialize the model for this LexicalSimplifier.")

        if pattern is None or pattern == "":
            raise ValueError("Please provide a pattern for this LexicalSimplifier.\n"
                             "A pattern should be a format string that can take at least one argument.")

        if exemplars is None or len(exemplars) == 0:
            print("No exemplars provided, using zero-shot mode.")

        self.model = model
        self.pattern = pattern
        self.exemplars = exemplars

    def set_model(self, model):
        self.model = model

    def set_pattern(self, pattern):
        self.pattern = pattern

    @abc.abstractmethod
    def generate_substitutions_for(self, complex_word: str, original_sentence: str) -> List[str]:
        """Generates a list of substitutions via the model predictions for the given complex word in the context of the sentence."""
        raise NotImplementedError("Please implement this method in the subclass.")