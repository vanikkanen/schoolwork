import re
from nltk import bigrams, trigrams

file = open("TheStoryofAnHour-KateChopin.txt")
text = file.read()

# Preprocess
text = text.lower()
text = re.sub(r"[^a-zA-Z\s]", " ", text)  # Remove special characters and numbers

stopwords = {'a', 'an', 'and', 'as', 'at', 'for', 'from', 'in', 'into', 'of',
             'on', 'or', 'the', 'to'}

words = re.split('\n| ', text)
tokens = [word for word in words if word not in stopwords and len(word) >= 2]

to_find = ('joy', 'that')

ngrams = list(bigrams(tokens))
count = sum(1 for ngram in ngrams if ngram == to_find)

n = 1
num = count/len(ngrams)
while True:
    new_num = int(num*pow(10, n))
    if new_num//100 % 10 != 0:
        break
    n += 1

num_to_divide_by = 127

print(new_num % num_to_divide_by)

