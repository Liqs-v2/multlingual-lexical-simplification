import ast
from typing import List
import openai

from config import OPENAI_API_KEY
from transformers import pipeline

from lexical_simplifier import LexicalSimplifier


# DISCLAIMER: This file was authored in an IDE with Github Copilot enabled.


class GPTLexicalSimplifier(LexicalSimplifier):
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

    def __init__(self, model=None, tokenizer=None, mask_token="[MASK]", pattern=None, exemplars=None, generation_args=None):

        if exemplars is None or len(exemplars) == 0:
            raise ValueError("Please provide a list of exemplars for in-context learning."
                             "Without exemplars the model will not produce output in in the expected format.")

        openai.api_key = OPENAI_API_KEY

    def generate_substitutions_for(self, complex_word: str, original_sentence: str):
        """
        Generates substitutions for a complex word in a sentence using the GPT-3.5 Turbo model.

        Args:
            complex_word (str): The complex word for which substitutions need to be generated.
            original_sentence (str): The original sentence containing the complex word.

        Returns:
            list: A list of generated substitutions for the complex word.
        """
        content = self.apply_pattern_to(original_sentence, complex_word)
        message = self.exemplars + [{'role': 'user', 'content': content}]

        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=message
        )
        response = str(completion.choices[0].message.content)
        return self.__parse_gpt_output(response)

    def __parse_gpt_output(self, gpt_output: str) -> List[str]:
        """
        Parses the string returned by the GPT API call into a list of possible substitutions.

        Args:
            llm_output (str): The string returned by the LLM.

        Returns:
            A list of possible substitutions for the complex word, if parsing succeeded.

        Raises:
            ValueError: If the provided string is not a valid list representation.
        """
        try:
            print(gpt_output)
            return ast.literal_eval(gpt_output)
        except (ValueError, SyntaxError):
            raise ValueError(f"The provided string is not a valid list representation: {gpt_output}")
