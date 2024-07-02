import torch

from lexical_simplifier import LexicalSimplifier


# DISCLAIMER: This file was authored in an IDE with Github Copilot enabled.


class SimpleBertLexicalSimplifier(LexicalSimplifier):
    """
    A simple BERT based implementation of lexical simplification. Masks the given complex word with [MASK], adds other
    BERT specific tokens and generates a list of possible substitutions via the model predictions based on the prompt.

    The prompt is dynamically built using the pattern attribute, which should be a format string that can take at least
    one argument - the original sentence with the masked complex word.

    Attributes:
        model: The model used for generating substitutions, in this case a BERT instance.
        tokenizer: The tokenizer used for tokenizing the input sentence. Must be the model tokenizer.
        pattern: The format string used to dynamically build prompts for generating substitutions. For this implementation,
            the pattern should contain placeholders for the original sentence and the sentence with the masked complex word.
            Between these, an instruction is injected to guide the model towards simplifying the complex word.
        exemplars: A list of exemplar words used for in-context learning. Unused for this implementation.
        mask_token: The token used to mask the complex word in the input sentence. Defaults to '[MASK]'.
        device: The device that is used for model inference. Used to determine if CUDA is available.
    """
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using {device} for model inference.")

    def __init__(self, model, tokenizer, mask_token, pattern=None, exemplars=None):
        super().__init__(model.to(self.device), tokenizer, mask_token, pattern, exemplars)

    def generate_substitutions_for(self, complex_word: str, original_sentence: str, top_k: int = 10):
        """
        Generates a list of substitutions via the model predictions for the given complex word in the context of the sentence.

        The input sentence specified by the original_sentence parameter should contain the complex word to be simplified.
        Based on the complex_word, the original_sentence and the currently configured self.pattern, the complex word is masked
        and a prompt is generated. This prompt is then tokenization before being passed to the model. The top_k predictions
        are returned.

        Will use CUDA if available.

        Args:
            complex_word: The complex word to be simplified. This is given in our case, we do not tackle complex word identification.
            original_sentence: The sentence containing the complex word.
            top_k: The number of top predictions to return.

        Returns:
            A list of the top_k possible substitutions for the complex word.
        """

        # Setup prompt
        # Assumes that complex_word is in the original_sentence, in the same case
        if complex_word not in original_sentence:
            # This covers the edge case of the complex word being the first word in the sentence
            complex_word = complex_word.capitalize() if complex_word.capitalize() in original_sentence else complex_word
        sentence_with_complex_word_masked = original_sentence.replace(complex_word, self.mask_token)
        input_text = self.apply_pattern_to(original_sentence, sentence_with_complex_word_masked)

        # Tokenize input text
        inputs = self.tokenizer(input_text, return_tensors="pt", padding=True, truncation=True).to(self.model.device)

        # Since the tokenizer returns a dict, we need to unpack to correctly move the tensors to CUDA
        inputs = {name: tensor.to(self.device) for name, tensor in inputs.items()}

        # Forward pass through the model
        with torch.no_grad():
            outputs = self.model(**inputs)

        # Get predicted probabilities for the masked token
        if (print(self.tokenizer.mask_token_id) ==5):
            print(inputs["input_ids"].squeeze().tolist())
            print(self.tokenizer.mask_token_id)
        masked_index = inputs["input_ids"].squeeze().tolist().index(self.tokenizer.mask_token_id)
        probs = torch.nn.functional.softmax(outputs.logits[0, masked_index], dim=-1)

        # Get the top predictions
        top_k_tokens = torch.topk(probs, k=top_k).indices.tolist()

        # Convert token IDs back to tokens
        predicted_tokens = [self.tokenizer.decode(token).strip() for token in top_k_tokens]

        return predicted_tokens
