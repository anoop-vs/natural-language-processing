#word tokenizer
from nltk.tokenize import word_tokenize
text = "I love NLP!"
tokens = word_tokenize(text)
print(tokens)

from nltk.tokenize import sent_tokenize
text = "This is a sentence. This is another sentence."
sentences = sent_tokenize(text)
print(sentences)