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
    tree = ET.parse(path)
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
        substitutes = line[1].split(";")
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
        # ranks in wrong order
        # Assign new rank
        new_rankings = {}

        for index,(rank,substitutes) in enumerate(substitution_dict.items()):
            new_rankings[index+1] = substitutes

        substitutions_list.append(new_rankings)
    
    return substitutions_list

# Get the proocessed Dataset and Substitutes
def processData(pathData, pathSubstitutes):
    subsitutes = readSubstituesIn(pathSubstitutes)
    root = readDatasetIn(pathData)
    complexWords = getComplexWords(root)
    sentences = getSentences(root)

    processedDate = []
    for index,subsitute in enumerate(subsitutes):
        processedLine = [sentences[index],complexWords[index],getPosition(complexWords[index],sentences[index]),subsitute]
        processedDate.append(processedLine)    

    return np.array(processedDate, dtype=object)  