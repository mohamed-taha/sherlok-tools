#!/usr/bin/python

""" 
    use a Naive Bayes Classifier to identify polarity of text
    
    polarity and labels:
    negative has label 0
    positive has label 1

"""

import sys
from time import time
sys.path.append("/home/mohamed/python/sherlok-tools/helpers/")
from text_preprocess import Preprocess
from sklearn.naive_bayes import GaussianNB


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = Preprocess()

# classification goes here

clf = GaussianNB()

# training
train_t0 = time()
clf.fit(features_train, labels_train)
train_t1 = time()

# prediction or testing
test_t0 = time()
predict = clf.predict(features_test)
test_t1 = time()

print "accuracy: ", clf.score(features_test, labels_test)
print "#################################"
print "tain time: ", round(train_t1 - train_t0, 3), "s"
print "prediction time: ", round(test_t1 - test_t0, 3), "s"



