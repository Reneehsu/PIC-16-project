#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 16:25:14 2018

@author: reneehsu
"""

import nltk
from nameparser import HumanName
from nltk import word_tokenize, pos_tag, ne_chunk
import numpy as np

with open('firstname.txt', 'r') as myfile:
  data = myfile.read().replace('\n', '')
with open('Harry Potter 2 - Chamber of Secrets.txt', 'r') as myfile:
  book = myfile.read().replace('\n', '')
import re
firstname = re.findall(r'[A-Z]+',data)


def get_human_names(text):
    tokens = nltk.tokenize.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos, binary = False)
    person_list = []
    person = []
    name = ""
    for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
        
        for leaf in subtree.leaves():
            
            person.append(leaf[0])
        if len(person) > 1: #avoid grabbing lone surnames
            for part in person:
                
                name += part + ' '
            if name[:-1] not in person_list:
                
                person_list.append(name[:-1])
        elif len(person) == 1:
            person = ''.join(person)
            if person.upper() in firstname:
                person_list.append(person)
        name = ''
        person = []
    
    return set(person_list)

names = get_human_names(book)

names.remove('Had Harry')
names.remove('Famous Harry Potter')
#print names

character = {}
for name in names:
    temp = [HumanName(name).last ,HumanName(name).first]
    character[name] = temp
    character[name].append(name)
print character

n=len(character)
adjMatrix = [[0]*n for _ in range(n)]


words = word_tokenize(book)

#this should be changed to the first one appear
lastcharacter = 0
lastpos = 0

for p in range(len(words)):
    for i, (key, value) in enumerate(character.iteritems()):  
            if words[p] in value and key!= character.keys()[lastcharacter]: 
                if p - lastpos < 20:
                    adjMatrix[lastcharacter][i]+=1
                    lastcharacter = i
                    lastpos = p
                    break
               

adjMatrix = np.array(adjMatrix)
print adjMatrix
print adjMatrix[1][:]
print adjMatrix.shape

#plotting
import matplotlib.pyplot as plt 
import networkx as nx
G = nx.DiGraph()
G.add_nodes_from(character.keys())
for i in range(adjMatrix.shape[0]):
    for j in range(adjMatrix.shape[1]): 
        if adjMatrix[i][j] > 5:  
            G.add_edge(character.keys()[i],character.keys()[j],weight=adjMatrix[i][j])
nx.draw(G,with_labels=True)
plt.show()

pr = nx.pagerank(G, alpha=0.85) # the default damping parameter alpha = 0.85
print pr

for char in character.keys():
    if pr[char] < 0.0022:
        G.remove_node(char)
nx.draw(G,with_labels=True)
#plt.savefig("path_graph_cities.png")
plt.show()        




text = """
Some economists have responded positively to Bitcoin, including 
Francois R. Velde, senior economist of the Federal Reserve in Chicago 
who described it as "an elegant solution to the problem of creating a 
digital currency." In November 2013 Richard Branson announced that 
Virgin Galactic would accept Bitcoin as payment, saying that he had invested 
in Bitcoin and found it "fascinating how a whole new global currency 
has been created", encouraging others to also invest in Bitcoin.
Other economists commenting on Bitcoin have been critical. 
Economist Paul Krugman has suggested that the structure of the currency 
incentivizes hoarding and that its value derives from the expectation that 
others will accept it as payment. Sorry, Larry Summers has expressed 
a "wait and see" attitude when it comes to Bitcoin. Nick Colas, a market 
strategist for ConvergEx Group, has remarked on the effect of increasing 
use of Bitcoin and its restricted supply, noting, "When incremental 
adoption meets relatively fixed supply, it should be no surprise that 
prices go up. Renee and Mr. Potter work together. And that’s exactly what is happening to BTC prices."
"""


