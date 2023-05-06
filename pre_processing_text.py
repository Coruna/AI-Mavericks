import json
import string
import nltk
from nltk.corpus import stopwords

# Load the JSON file
with open('speech_recognition_output.json') as file:
    data = json.load(file)


# Tokenize the text
tokens = nltk.word_tokenize(data)

# Remove stop words and punctuation, and turn all letters to lowercase
stop_words = set(stopwords.words('english'))
punctuations = set(string.punctuation)
filtered_tokens = [token.lower() for token in tokens if token.lower() not in stop_words and token not in punctuations]

# Join the tokens to form the cleaned text
cleaned_text = ' '.join(filtered_tokens)

with open('cleaned_text.json', 'w') as file:
    json.dump(cleaned_text, file)