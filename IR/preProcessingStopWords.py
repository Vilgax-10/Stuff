from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

sentence = """
This is a sentence for pre-processing a web page before ranking"""

stop_words = set(stopwords.words("english"))
word_tokens = word_tokenize(sentence)

filtered_sentence = [w for w in word_tokens if w not in stop_words]

print(word_tokens)
print(filtered_sentence)
print(stop_words)
