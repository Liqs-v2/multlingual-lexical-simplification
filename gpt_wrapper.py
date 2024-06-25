import openai # Import the OpenAI library
import src.utils.nnseval_data_provider as nnseval_data_provider
from src.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY
content = None

original_data = nnseval_data_provider.NNSevalDataProvider().provide_data_as_numpy_array()

completion = openai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Translator for a Lexical simplification dataset"},
        {"role": "user", "content": "Übersetze dieses Datenset zu Deutsch, behalte das gleiche Format: " + str(original_data)}
    ]
)
response = str(completion.choices[0].message.content)

# Save response in a text file
with open('response.txt', 'w') as file:
        file.write(response)


