import abc
from typing import List
from abc import ABCMeta

# DISCLAIMER: This file was authored in an IDE with Github Copilot enabled.


class LexicalSimplifier(metaclass=ABCMeta):
    """
    An abstract base class for a lexical simplification. Implements a basic initializer and functions for
    setting the model and pattern for the simplifier. The main function to be implemented by subclasses is
    get_substitutions_for, which should return a list of possible substitutions for a given complex word.

    Attributes:
        model: The model used for generating substitutions.
        tokenizer: The tokenizer used for tokenizing the input sentence. Must be the model tokenizer.
        pattern: The format string used to dynamically build prompts for generating substitutions. In the simplest
            case this could be a string with one placeholder, into which the input sentence with the masked complex
            word is inserted (eg. for a BERT model).
        exemplars: A list of exemplar words used for zero-shot learning. If provided, these will be prepended to the every
            prompt.
    """
    model = None
    tokenizer = None
    pattern: str = None
    exemplars: List[str] = None

    def __init__(self, model, tokenizer, pattern, exemplars):
        if model is None:
            raise ValueError("Please initialize the model for this LexicalSimplifier.")

        if tokenizer is None:
            raise ValueError("Please initialize the model for this LexicalSimplifier.")

        if pattern is None or pattern == "":
            raise ValueError("Please provide a pattern for this LexicalSimplifier.\n"
                             "A pattern should be a format string that can take at least one argument.")

        if exemplars is None or len(exemplars) == 0:
            print("No exemplars provided, using zero-shot mode.")

        self.model = model
        self.tokenizer = tokenizer
        self.pattern = pattern
        self.exemplars = exemplars

    def set_model(self, model):
        self.model = model

    def set_tokenizer(self, tokenizer):
        self.tokenizer = tokenizer

    def set_pattern(self, pattern):
        self.pattern = pattern

    @abc.abstractmethod
    def generate_substitutions_for(self, complex_word: str, original_sentence: str,  top_k: int = 10) -> List[str]:
        """
        Generates a list of substitutions via the model predictions for the given complex word in the context of the sentence.

        The input sentence specified by the original_sentence parameter should contain the complex word to be simplified and
        might need require further preprocessing (e.g. tokenization, masking) before being passed to the model.

        Args:
            complex_word: The complex word to be simplified. This is given in our case, we do not tackle complex word identification.
            original_sentence: The sentence containing the complex word.
            top_k: The number of top predictions to return.

        Returns:
            A list of possible substitutions for the complex word.
        """
        raise NotImplementedError("Please implement this method in the subclass.")