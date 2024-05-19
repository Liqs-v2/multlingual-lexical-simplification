import xml.etree.ElementTree as ET
import numpy as np
import numpy as np


#find position of the word in the sentence
def getPosition(word, sentence):
    words = sentence.split()
    try:
        index = words.index(word)
    except:
        index = next((i for i, s in enumerate(words) if word in s), None)
    return index

#returns words that should be substituted
def getComplexWords(root):
    complexWords = []
    for instance in root.findall(".//instance"):
        head_word = instance.find(".//head").text
        complexWords.append(head_word)
    return np.array(complexWords)

#returns all sentences
def getSentences(root):
    text = []
    for child in root:
        sentence = ''.join(child.itertext())
        cleaned_text = sentence.replace('\n', ' ')
        sentences = cleaned_text.split('. ')
        sentences_without_whitespace = [s.strip() for s in sentences]
        # Remove empty strings from the list
        filtered_list = [item for item in sentences_without_whitespace if item != ""]
        text.extend(filtered_list)
    # Convert the list to a NumPy array
    sentences = np.array(text)
    print(sentences)

    return sentences

def readDatasetIn(path):
    # Parse the XML file
    tree = ET.parse('data/germeval/train-dataset.xml')
    return tree.getroot()

    


#'data/germeval/train-dataset.gold'
def readSubstituesIn(path):
    # Read the file
    with open(path, 'r') as file:
        # Remove newline characters and store each line as an element in a list
        lines = [line.strip() for line in file.readlines()]
    return lines

# Get the proocessed Dataset and Substitutes
def processData():
    root = readDatasetIn('data/germeval/train-dataset.xml')
    complexWords = getComplexWords(root)
    sentences = getSentences(root)

    sub_array = readSubstituesIn('data/germeval/train-dataset.gold')
    print(sub_array[0])
    processedDate = []
    for index,subsitute in enumerate(sub_array):
        print(subsitute)
        line = subsitute.split(' ')
        subsitutes = [value for index, value in enumerate(line) if index % 2 != 0 and index > 2]
        string = sentences[index] + '\n' + complexWords[index] + '\n' + str(getPosition(complexWords[index],sentences[index])) + '\n' + str(subsitutes)
        processedDate.append(string)    

    return np.array(processedDate)  

array = processData()
print(array[0])