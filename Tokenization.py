import nltk #pip install nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download required NLTK resources
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")

# Input text
text = "This is a very useful cloud computing course."

# Tokenize the text
tokens = word_tokenize(text)

# Load English stop words
stop_words = set(stopwords.words("english"))

# Remove stop words
filtered = [
    word for word in tokens
    if word.lower() not in stop_words
]

# Display the results
print("Tokens:", tokens)
print("After stop word removal:", filtered)