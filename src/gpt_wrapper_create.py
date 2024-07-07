import openai # Import the OpenAI library
import src.utils.germaneval_data_provider as germaneval_data_provider
from src.config import OPENAI_API_KEY
import datetime
import numpy as np

class CreateNewSet:

    _original_data = germaneval_data_provider.GermanEvalDataProvider().provide_data_as_numpy_array()

    _messages = [
            {"role": "user", "content": "kreiere ein neues Dataset mit 10 Sätzen für lexical simplification."},
            {"role": "assistant", "content": str(dataset.tolist())},
            {"role": "user", "content": "kreiere ein neues Dataset mit 30 Sätzen für lexical simplification."},
            ]

    def __init__(self):
        openai.api_key = OPENAI_API_KEY
    
    def create_new_set(self, interval_lower, interval_upper):
        dataset = self._original_data[interval_lower:interval_upper]
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages= self._messages
            )
        response = str(completion.choices[0].message.content)
        with open('/content/drive/MyDrive/nlp_ss24/multilingual-lexical-simplification/data/created_dataset/new_set' +datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y") +'.txt', 'w') as file:
            file.write(str(response))

