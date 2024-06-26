import openai # Import the OpenAI library
import src.utils.nnseval_data_provider as nnseval_data_provider
from src.config import OPENAI_API_KEY
import datetime
import numpy as np

openai.api_key = OPENAI_API_KEY
content = None

original_data = nnseval_data_provider.NNSevalDataProvider().provide_data_as_numpy_array()
og_sentence = "harry also becomes the worthy possessor of the remaining deathly hallows : the invisibility cloak and the resurrection stone , hence becoming the true master of death ."
sentence = 'harry wird auch der würdige Besitzer der verbleibenden Heiligtümer des Todes: der Unsichtbarkeitsmantel und des Auferstehungssteins, wird dadurch zum wahren Meister des Todes.'
og_word = 'possessor'
word = 'Besitzer'
og_position = 5
position = 6
og_synonyms = {1: ['owner'], 2: ['holder'], 3: ['buyer', 'master', 'teacher']}
synonyms = {1: ['Eigentümer'], 2: ['Inhaber'], 3: ['Käufer', 'Meister', 'Lehrer']}

example = sentence + "," + word + "," + str(position) + "," + str(synonyms)
original_example = og_sentence + "," + og_word + "," + str(og_position) + "," + str(og_synonyms)
def iteratively():
    new_data = []
    for data in original_data:
        content = "Übersetze diesen Eintrag zu Deutsch (sowohl den Satz, die neue Position des Wortes in dem Satz wie auch das zu übersetzende Wort und die Liste der Substitutionen) und behalte dabei das gleiche Format, z.B.: \n" + original_example +"\nto \n"+ example+":\n" + str(data)

        # Perform operations on each element of the array
        completion = openai.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "Translator for a Lexical simplification dataset"},
            {"role": "user", "content": content}
            ]
        )
        response = str(completion.choices[0].message.content)
        new_data.append(response)

    # Save response in a text file
    with open('response' +datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y") +'.txt', 'w') as file:
        file.write(str(new_data))

    with open("output", 'w', encoding='utf-8') as f:
        for item in new_data:
            f.write(f"{item}\n")

    response = np.array(new_data, dtype=object)
    np.savetxt('output_unicode.csv', data, delimiter=',', fmt='%s', encoding='utf-8')
    with open('response_numpy' +datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y") +'.txt', 'w') as file:
        file.write(str(new_data))

def whole_set():
    content = "Übersetze dieses Dataset zu Deutsch (es sollte kein einziges Wort mehr auf Englisch sein) und behalte dabei das originale Format des gesamten Datensets, ein Übersetzungsbeispiel: \n" + original_example +"\nto \n"+ example+":\n" + str(original_data)
    completion = openai.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "system", "content": "Translator for a Lexical simplification dataset"},
        {"role": "user", "content": content}
    ]
    )
    response = str(completion.choices[0].message.content)
    with open('response' +datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y") +'.txt', 'w') as file:
        file.write(str(response))

whole_set()