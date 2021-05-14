import re
from uk_stemmer import UkStemmer

stemmer = UkStemmer()
test_string = 'кольоровий'

prepare_test_string = test_string.lower()
words = re.split(r'(\W)', prepare_test_string)
words = [word for word in words if word != '']

for i in range(len(words)):
    words[i] = stemmer.stem_word(words[i])

stem_test_string = ''.join(words)
print('Source: %s\nStemmed: %s' % (test_string, stem_test_string))