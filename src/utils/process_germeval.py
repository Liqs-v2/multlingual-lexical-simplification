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

    substitutions_list = []
    for line in lines:
        line = line.split("::")
        line = line[1].split(";")
        substitutes = line[1:]
        substitutes = [s for s in substitutes if s!=""]
        # Parse the substitutions into a dictionary
        substitution_dict = {}
        for substitute in substitutes:
            substitute = substitute.strip()
            rank = int(substitute[len(substitute)-1:])  
            substitute = substitute[:len(substitute)-2] 
            if rank in substitution_dict:
                substitution_dict[rank].append(substitute)
            else:
                substitution_dict[rank] = [substitute]
        substitutions_list.append(substitution_dict)
    
    return substitutions_list

# Get the proocessed Dataset and Substitutes
def processData():
    root = readDatasetIn('data/germeval/train-dataset.xml')
    complexWords = getComplexWords(root)
    sentences = getSentences(root)

    subsitutes = readSubstituesIn('data/germeval/train-dataset.gold')
    processedDate = []
    for index,subsitute in enumerate(subsitutes):
        processedLine = [sentences[index],complexWords[index],getPosition(complexWords[index],sentences[index]),subsitute]
        processedDate.append(processedLine)    

    return np.array(processedDate, dtype=object)  

array = processData()
print(array[0])