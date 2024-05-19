import xml.etree.ElementTree as ET
import numpy as np

# Parse the XML file
tree = ET.parse('data/germeval/train-dataset.xml')
root = tree.getroot()

# Extract the data from XML and store it in a list
data = []
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
array = np.array(text)
print(array)

