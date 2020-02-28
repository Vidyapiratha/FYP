# import codecs
# import tamil
# import tamilstemmer
# import tamil.utf8 as utf8
# #     wlen = map(lambda x: len(tamil.utf8.get_letters(x)), ta_parts)
# #     wlen = list(wlen)
# def test_project_MADURAI(self):
#     fname = "data/project_madurai_tscii.txt"
#     fexact = "data/project_madurai_utf8.txt"
#
#
# with codecs.open(fexact, 'r', 'utf-8') as fileHandle:
#     exact = fileHandle.read()
#
#     # convert
# with codecs.open(fname, 'r', 'utf-8') as fileHandle:
#     output = tamil.tscii.convert_to_unicode(fileHandle.read())


# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai
#
# import codecs
#
# # setup the paths
# from opentamiltests import *
# import tamil
# from ngram.Corpus import Corpus
# from ngram import LetterModels
#
# import tamil.utf8 as utf8
#
#
# class Letters(unittest.TestCase):
#     def test_data_op(self):
#         dat = '\x97\xC8\xA2\xD7\xC3\xA2'
#         output = tamil.tscii.convert_to_unicode(dat)
#         if (LINUX):
#             print(output)
#
#     def test_project_MADURAI(self):
#         fname = "data/project_madurai_tscii.txt"
#         fexact = "data/project_madurai_utf8.txt"
#
#         # expected
#         with codecs.open(fexact, 'r', 'utf-8') as fileHandle:
#             exact = fileHandle.read()
#
#             # convert
#         with codecs.open(fname, 'r', 'utf-8') as fileHandle:
#             output = tamil.tscii.convert_to_unicode(fileHandle.read())
#
#         if (LINUX):
#             print(len(output))
#             print(len(exact))
#
#         ta_parts = u"டைட்டானிக் படத்தில் வரும் ஜேக் மற்றும் ரோஸ் போன்று தன் காதலை வெளிப்படுத்தும் இரு தவளைகள்".split()
#         wlen_expected = [5, 5, 3, 2, 4, 2, 3, 2, 3, 8, 2, 5]
#         wlen = map(lambda x: len(tamil.utf8.get_letters(x)), ta_parts)
#         if PYTHON3:
#             wlen = list(wlen)
#         if (LINUX):
#             print(wlen)
#             print(wlen_expected)
#         self.assertEqual(wlen, wlen_expected)
#
#
# if __name__ == "__main__":
#     unittest.main()

###########################################################################################################################

import re
import tamil
def token(sentence, remove_vowels=False, remove_repeat=False, minchars=2):
    tokens = []
#   for t in re.findall("[A-Z]{2,}(?![a-z])|[A-Z][a-z]+(?=[A-Z])|[\w]+",sentence.lower()):
    for t in re.findall("[a-zA-Z]+",sentence.lower()):

        if len(t)>=minchars:
            if remove_vowels:
                t=removeVovels(t)
            if remove_repeat:
                t=removeRepeat(t)
            tokens.append(t)
    return tokens
#######################################################################################################################
# Naive method for splitting a text into sentences
def split_content_to_sentences(self, content):
    content = content.replace("\n", ". ")
    return content.split(". ")

# Naive method for splitting a text into paragraphs
def split_content_to_paragraphs(self, content):
    # return content.split("\n\n")
    return content.split("<newline>")

# Caculate the intersection between 2 sentences
def sentences_intersection(self, sent1, sent2):

    # split the sentence into words/tokens
    # s1 = set(sent1.split(" "))
    # s2 = set(sent2.split(" "))
    s1 = set(tamil.utf8.get_letters(sent1))
    s2 = set(tamil.utf8.get_letters(sent2))

    # If there is not intersection, just return 0
    # if (len(s1) + len(s2)) == 0:
    if len(s1.intersection(s2)) == 0:
        return 0

    # We normalize the result by the average number of words
    return len(s1.intersection(s2)) / ((len(s1) + len(s2)) / 2.0)

# Format a sentence - remove all non-alphbetic chars from the sentence
# We'll use the formatted sentence as a key in our sentences dictionary
def format_sentence(self, sentence):
    # sentence = re.sub(r'\W+', '', sentence)       # [\u0B80-\u0BFF]
    sentence = re.sub(r'\s+', '', sentence)
    sentence = re.sub(r'\d+', '', sentence)
    print(sentence)
    return sentence

# Convert the content into a dictionary <K, V>
# k = The formatted sentence
# V = The rank of the sentence
def get_sentences_ranks(self, content):

    # Split the content into sentences
    sentences = self.split_content_to_sentences(content)

    # Calculate the intersection of every two sentences
    n = len(sentences)
    values = [[0 for x in range(n)] for x in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            # Metric for intersection is symmetric so we calculate 1/2 only
            # For additional metrics see: ngram.Distance module in open-tamil
            # Ref https://github.com/Ezhil-Language-Foundation/open-tamil/blob/master/ngram/Distance.py
            if i >= j:
                values[i][j] = values[j][i]
                continue
            values[i][j] = self.sentences_intersection(sentences[i], sentences[j])

# Format a sentence - remove all non-alphbetic chars from the sentence
# We'll use the formatted sentence as a key in our sentences dictionary
def format_sentence(self, sentence):
    # sentence = re.sub(r'\W+', '', sentence)       # [\u0B80-\u0BFF]
    sentence = re.sub(r'\s+', '', sentence)
    sentence = re.sub(r'\d+','',sentence)
    # print sentence
    return sentence
#######################################################################################################################
VOWELS = ['a', 'e', 'i', 'o', 'u']

def removeRepeat(string):
    return re.sub(r'(.)\1+', r'\1\1', string)

def removeVovels(string):
    return ''.join([l for l in string.lower() if l not in VOWELS])

if __name__ == '__main__':
    pass

def normalize_matrix(matrix):
    pass
