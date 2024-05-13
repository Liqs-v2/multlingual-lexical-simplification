from lexical_simplifier import LexicalSimplifier


class GermanBertLexicalSimplifier(LexicalSimplifier):
    """
    A German BERT based implementation of lexical simplification. Masks the given complex word with [MASK], adds other
    BERT specific tokens and generates a list of possible substitutions via the model predictions based on the prompt.
    """

    def __init__(self, model, pattern, exemplars):
        super().__init__(model, pattern, exemplars)

    def generate_substitutions_for(self, complex_word):
        """Generates a list of substitutions via the model predictions for the given complex word."""
        raise NotImplementedError("Please implement this method in the subclass.")