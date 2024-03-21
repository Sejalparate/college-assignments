import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
import spacy

nltk.download('punkt')
nltk.download('stopwords')
nlp = spacy.load("en_core_web_sm")
stop_words = set(stopwords.words("english"))
stemmer = SnowballStemmer("english")

# Function to perform tokenization
def tokenize(text):
    tokens = word_tokenize(text)
    tokens = [word.lower() for word in tokens if word.isalpha()]
    return tokens

# Function to perform stemming
def stem(tokens):
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return stemmed_tokens

# Function to perform lemmatization
def lemmatize(tokens):
    doc = nlp(" ".join(tokens))
    lemmatized_tokens = [token.lemma_ for token in doc if not token.is_stop]
    return lemmatized_tokens

# Function to remove stop words
def remove_stop_words(tokens):
    filtered_tokens = [word for word in tokens if not word in stop_words]
    return filtered_tokens

# Load the text from the doc file
with open("Assgn2_txt.txt") as file:
    text = file.read()

tokens = tokenize(text)
stemmed_tokens = stem(tokens)
lemmatized_tokens = lemmatize(tokens)
filtered_tokens = remove_stop_words(lemmatized_tokens)

# Print the tokens
print("Original Tokens:", tokens[:20])
print("Stemmed Tokens:", stemmed_tokens[:20])
print("Lemmatized Tokens:", lemmatized_tokens[:20])
print("Filtered Tokens:", filtered_tokens[:20])