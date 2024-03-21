import docx
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
import spacy
from Assgn2_txt import *

nltk.download('punkt')
nltk.download('stopwords')
nlp = spacy.load("en_core_web_sm")
stop_words = set(stopwords.words("english"))
stemmer = SnowballStemmer("english")

doc = docx.Document("Assgn2_docx.docx")
text = ''
for paragraph in doc.paragraphs:
    text += paragraph.text
    
tokens = tokenize(text)
stemmed_tokens = stem(tokens)
lemmatized_tokens = lemmatize(tokens)
filtered_tokens = remove_stop_words(lemmatized_tokens)

print("Original Tokens:", tokens[:20])
print("Stemmed Tokens:", stemmed_tokens[:20])
print("Lemmatized Tokens:", lemmatized_tokens[:20])
print("Filtered Tokens:", filtered_tokens[:20])