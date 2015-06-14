#!/usr/bin/python

import os
import pickle
import re
import sys
import csv

from parse_out_file_text import parseOutText , parseOutText_csv

"""
    starter code to process the text from positive and negative files to extract
    the features and get the documents ready for classification

    the data is stored in lists and packed away in pickle files at the end

"""

positive_files_path = "/home/mohamed/python/sherlok-tools/datasets/Twitter/Positive/"
negative_files_path = "/home/mohamed/python/sherlok-tools/datasets/Twitter/Negative/"

label_data = []
word_data = []

for file in os.listdir(positive_files_path):
	f = open(positive_files_path + file, 'r')
	text = parseOutText(f) ##get stem
	word_data.append(text.strip())
	label_data.append(1)
	f.close()

for file in os.listdir(negative_files_path):
	f = open(negative_files_path + file, 'r')
	text = parseOutText(f)
	word_data.append(text.strip())
	label_data.append(0)
	f.close()


###############################################################
# add nile university  dataset
'''
words=[]
labels=[]
f=open("/home/mohamed/python/sherlok-tools/datasets/m.csv")
try:
    reader = csv.reader(f)
    for row in reader:
        words.append(row[0])
        labels.append(row[1])

finally:
    f.close()

for i in range(0,len(words)):
    if labels[i] == "positive" :
        text = parseOutText_csv(words[i]) # get stem
        word_data.append(words[i].strip())
        label_data.append(1)
    else:
        text = parseOutText_csv(words[i]) # get stem
        word_data.append(words[i].strip())
        label_data.append(0)
'''        





print ("Text processed")

pickle.dump(word_data, open("word_data.pkl", "w"))
pickle.dump(label_data,open("label_data.pkl", "w"))