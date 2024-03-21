import PyPDF2
import nltk
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from Assgn2_txt import *

nltk.download('punkt')
nltk.download('stopwords')
nlp = spacy.load("en_core_web_sm")
stop_words = set(stopwords.words("english"))
stemmer = SnowballStemmer("english")

pdf_file = open('Assgn2_pdf.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)
num_pages = len(pdf_reader.pages)

text = ''
for i in range(num_pages):      # loop through each page and extract the text
    page = pdf_reader.pages[i]
    #pdf_reader.getPage(i)
    text += page.extract_text()
    #page.extractText()

tokens = tokenize(text)
stemmed_tokens = stem(tokens)
lemmatized_tokens = lemmatize(tokens)
filtered_tokens = remove_stop_words(lemmatized_tokens)

# Print the tokens
print("Original Tokens:", tokens[:20])
print("Stemmed Tokens:", stemmed_tokens[:20])
print("Lemmatized Tokens:", lemmatized_tokens[:20])
print("Filtered Tokens:", filtered_tokens[:20])