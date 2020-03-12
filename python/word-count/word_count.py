import re

def count_words(sentence):
    sentence = re.findall(r"[\w']+", sentence.replace("_", ' ').lower())
    sentence = [i.replace("'", '') if i.endswith("'") else i for i in sentence]
    word = {}
    for i in sentence:
        if i in word:
            word[i] += 1
        else:
            word[i] = 1
    return word
