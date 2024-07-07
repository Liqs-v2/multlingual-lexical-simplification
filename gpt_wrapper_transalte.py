import openai # Import the OpenAI library
import src.utils.nnseval_data_provider as nnseval_data_provider
from src.config import OPENAI_API_KEY
import datetime
import numpy as np

openai.api_key = OPENAI_API_KEY
content = None

original_data = nnseval_data_provider.NNSevalDataProvider().provide_data_as_numpy_array()
print(original_data[3])
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
data_ger_1 = "['harry wird auch der würdige Besitzer der verbleibenden Heiligtümer des Todes: der Unsichtbarkeitsmantel und des Auferstehungssteins, wird dadurch zum wahren Meister des Todes.', 'Besitzer', 5, {1: ['Eigentümer'], 2: ['Inhaber'], 3: ['Käufer', 'Meister', 'Lehrer']}]"

data_eng_1 = "['harry also becomes the worthy possessor of the remaining deathly hallows : the invisibility cloak and the resurrection stone , hence becoming the true master of death .', 'possessor', 5, {1: ['owner'], 2: ['holder'], 3: ['buyer', 'master', 'teacher']}], results in the same format in German: "

data_str_ger_2 = "['Die Vereinigten Staaten veranstalteten 1909 in Shanghai, China, eine 13-Nationen-Konferenz der Internationalen Opiumkommission als Reaktion auf die zunehmende Kritik am Opiumhandel .', 'veranstalteten', 3, {1: ['versammelt'], 2: ['gesammelt'], 3: ['begonnen'], 4: ['eröffnet'], 5: ['angeordnet', 'zusammengebracht']}]"
data_str_eng_2 = "['the united states convened a 13-nation conference of the international opium commission in 1909 in shanghai , china in response to increasing criticism of the opium trade .', 'convened', 3, {1: ['assembled'], 2: ['gathered'], 3: ['started'], 4: ['opened'], 5: ['ordered', 'brought together']}], results in the same format in German:"

messages = [
            {"role": "user", "content": "kreiere ein neues Dataset mit 2 Sätzen und 2 Wörtern, die übersetzt werden sollen."},
            {"role": "assistant", "content": data_ger_1 + data_str_ger_2},
            {"role": "user", "content": "kreiere ein neues Dataset mit 10 Sätzen und 10 Wörtern, die übersetzt werden sollen."},
            ]

def iteratively():
    new_data = []
    for data in original_data:
        # Perform operations on each element of the array
        completion = openai.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages= messages + [{'role': 'user', 'content': str(data)}]
        )
        response = str(completion.choices[0].message.content)
        new_data.append(response)

    # Save response in a text file
    with open('response' +datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y") +'.txt', 'w') as file:
        file.write(str(messages))
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

iteratively()