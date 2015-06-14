# -*- coding: utf-8 -*-
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
from preprocess_input import preprocess_input
from sklearn.naive_bayes import GaussianNB

def NB(text):
    ### features_train and features_test are the features for the training
    ### and testing datasets, respectively
    ### labels_train and labels_test are the corresponding item labels
    features_train, features_test, labels_train, labels_test = Preprocess()
    Ifeatures_train,Ifeatures_test,Ilabels_train=preprocess_input([text])

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

    print "#################################"

    clf.fit(Ifeatures_train,Ilabels_train)
    print ("prediction of ",str(clf.predict(Ifeatures_test))[1])

    #print "prediction of ", clf.predict(preprocess_input(text))
    return  str(clf.predict(Ifeatures_test))[1]

NB("جميل")