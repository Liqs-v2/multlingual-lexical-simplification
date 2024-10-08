import ast
from typing import List

import torch
from transformers import pipeline

from lexical_simplifier import LexicalSimplifier


# DISCLAIMER: This file was authored in an IDE with Github Copilot enabled.


class LLMLexicalSimplifier(LexicalSimplifier):
    """
    A dialogue/chat-based implementation of lexical simplification (enabling the use of LLMs). Masks the given complex
    word with [MASK], adds other
    BERT specific tokens and generates a list of possible substitutions via the model predictions based on the prompt.

    The prompt is dynamically built using the pattern attribute, which should be a format string that can take at least
    one argument - the original sentence with the masked complex word.

    Attributes:
        model: The model used for generating substitutions, in this case a CausalLM model.
        tokenizer: The tokenizer used for tokenizing the input sentence. Must be the model tokenizer.
        pattern: The format string used to dynamically build prompts for generating substitutions. For this implementation,
            the pattern should contain placeholders for the original sentence and the sentence with the masked complex word.
            Between these, an instruction is injected to guide the model towards simplifying the complex word.
        exemplars: A list of exemplars used for in-context learning. If provided, these will be prepended to the every
            prompt.
        mask_token: The token used to mask the complex word in the input sentence. Defaults to '[MASK]'.
        device: The device that is used for model inference. Used to determine if CUDA is available.
        _pipe: Text generation pipeline for the model. Refer to HuggingFace
            documentation for more information.
        _generation_args: Arguments to be passed to the pipeline for text generation. Refer to HuggingFace
            documentation for more information.

    Raises:
        ValueError: If the exemplars list is empty or None. Requires exemplars.
    """
    device = None
    _pipe = None
    _generation_args = None

    def __init__(self, model, tokenizer, mask_token, pattern=None, exemplars=None, generation_args=None):
        if exemplars is None or len(exemplars) == 0:
            raise ValueError("Please provide a list of exemplars for in-context learning."
                             "Without exemplars the model will not produce output in in the expected format.")

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"Using {self.device} for model inference.")

        super().__init__(model.to(self.device), tokenizer, mask_token, pattern, exemplars)

        self._pipe = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            device=self.device
        )

        self._generation_args = generation_args

    def generate_substitutions_for(self, complex_word: str, original_sentence: str, topic: str = 'unknown'):
        """
        Generates a list of substitutions via the model predictions for the given complex word in the context of the sentence.

        The input sentence specified by the original_sentence parameter should contain the complex word to be simplified.
        Based on the complex_word, the original_sentence and the currently configured self.pattern, the complex word is masked
        and a prompt is generated. The provided exemplars for in-context learning are prepended to this. Then the prompt
        is tokenized before being passed to the model.

        Will use CUDA if available.

        Args:
            complex_word: The complex word to be simplified. This is given in our case, we do not tackle complex word identification.
            original_sentence: The sentence containing the complex word.
            topic: The topic of the sentence. This can be used to guide the simplification process. Default: 'unknown'

        Returns:
            A list of possible substitutions for the complex word. None if the model does not adhere to the format
            specified (parsing fails).

        Raises:
            ValueError: If the string returned by the LLM is not a valid list representation and parsing fails.
        """
        # Setup prompt
        # Assumes that complex_word is in the original_sentence, in the same case
        if complex_word not in original_sentence:
            # This covers the edge case of the complex word being the first word in the sentence
            complex_word = complex_word.capitalize() if complex_word.capitalize() in original_sentence else complex_word
        sentence_with_complex_word_masked = original_sentence.replace(complex_word, self.mask_token)

        input_text = self.apply_pattern_to(original_sentence, sentence_with_complex_word_masked, topic)

        output = self._pipe(self.exemplars + [{'role': 'user', 'content': input_text}], **self._generation_args)
        substitutions = output[0]['generated_text']

        try:
            parsed_substitutions = self.__parse_llm_output(substitutions)
        except ValueError as e:
            print(f"Failed to parse the output from the LLM: {e}\n"
                  f"Returning empty list.")
            return []

        return parsed_substitutions

    def __parse_llm_output(self, llm_output: str) -> List[str]:
        """
        Parses the string returned by the LLM into a list of possible substitutions.

        Args:
            llm_output (str): The string returned by the LLM.

        Returns:
            A list of possible substitutions for the complex word, if parsing succeeded.

        Raises:
            ValueError: If the provided string is not a valid list representation.
        """

        try:
            return ast.literal_eval(llm_output.strip())
        except (ValueError, SyntaxError):
            raise ValueError(f"The provided string is not a valid list representation: {llm_output}")
