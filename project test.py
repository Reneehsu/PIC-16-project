#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 16:36:21 2018

@author: reneehsu
"""
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.chunk import conlltags2tree, tree2conlltags
#with open('Harry Potter 2 - Chamber of Secrets.txt', 'r') as myfile:
 # document = myfile.read().replace('\n', '')





sentences = [nltk.word_tokenize(sent) for sent in sentences]
print sentences


sentences = [ne_chunk(nltk.pos_tag(sent)) for sent in sentences]
iob_tagged=tree2conlltags(sentences)
print iob_tagged

print sentences

from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.chunk import conlltags2tree, tree2conlltags
document = "Renee loves Harry. Hannah is her friend. Harry likes Hannah. Sorry, I'm wrong. Fear, not."
sentences = nltk.sent_tokenize(document)

ne_tree = [ne_chunk(pos_tag(word_tokenize(sentence))) for sentence in sentences]
 
iob_tagged = []
for tree in ne_tree:
    iob_tagged.append(tree2conlltags(tree))
print iob_tagged