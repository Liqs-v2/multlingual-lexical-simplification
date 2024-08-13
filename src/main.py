import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from benchmark_suite import BenchmarkSuite
from language import Language
from src.llm_lexical_simplifier import LLMLexicalSimplifier


# DISCLAIMER: This file was authored in an IDE with Github Copilot enabled.


def main():
    torch.random.manual_seed(0)

    model = AutoModelForCausalLM.from_pretrained(
        "distilbert/distilgpt2",
        torch_dtype="auto",
        trust_remote_code=True,
        # Flash attention is only supported starting Ampere architecture
        # So we cant use it on free-tier GPUs
    )
    tokenizer = AutoTokenizer.from_pretrained("distilbert/distilgpt2")
    tokenizer.padding_side = "left"
    # Define PAD Token = EOS Token
    tokenizer.pad_token = tokenizer.eos_token
    model.config.pad_token_id = model.config.eos_token_id

    messages = [
        {"role": "user",
         "content": "Der Maschinenbau hat in Europa durch die Bildung der EU eine starke Erleichterung erhalten. Die "
                    "vereinfachte Version des vorigen Satzes ist: Der Maschinenbau hat in Europa durch die Bildung "
                    "der EU eine starke [MASK] erhalten. Results as ordered, AST parsable Python list:"},
        {"role": "assistant",
         "content": '["Vereinfachung", "Entspannung", "Begünstigung", "Unterstützung", "Rückenwind,  "Förderung", '
                    '"Rückhalt", "Aufwind", "Antrieb", "Erleichterung"]'},
        {"role": "user",
         "content": "Die EU-Renaturierungsverordnung galt eigentlich bereits als durchgebracht; das EU-Parlament "
                    "hatte zugestimmt und die Staaten ihren grundsätzlichen Sanktus signalisiert. Die vereinfachte "
                    "Version des vorigen Satzes ist: Die EU-Renaturierungsverordnung galt eigentlich bereits als "
                    "durchgebracht; das EU-Parlament hatte zugestimmt und die Staaten ihren grundsätzlichen [MASK] "
                    "signalisiert. Ten results as ordered, AST parsable Python list:"},
        {"role": "assistant",
         "content": '["Zustimmung", "Einverständnis", "Okay", "Segen", "Billigung, Bestätigung, Bejahung, Zuspruch, '
                    'Akzeptanz, Befürwortung"]'},
    ]

    generation_args = {
        "max_new_tokens": 100,
        "return_full_text": False,
        "num_return_sequences": 1,
        "do_sample": False,
    }

    llm_ls = LLMLexicalSimplifier(model=model, tokenizer=tokenizer,
                                  pattern='{original_sentence} Die vereinfachte Version des vorigen Satzes ist: {'
                                          'sentence_with_complex_word_masked} Ten results as ordered, AST parsable '
                                          'Python list:',
                                  exemplars=messages, mask_token='[MASK]', generation_args=generation_args)

    suite = BenchmarkSuite(llm_ls, {
        Language.DE: {'pattern': '{original_sentence}. Die vereinfachte Version des vorigen Satzes ist: '
                                 '{sentence_with_complex_word_masked}. Ten results as ordered, AST parsable '
                                 'Python list:',
                      'exemplars': messages}})
    suite.run()


if __name__ == '__main__':
    main()
