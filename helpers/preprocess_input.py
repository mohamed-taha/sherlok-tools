# -*- coding: utf-8 -*-
#!/usr/bin/python

import pickle
import string
import numpy

from sklearn import cross_validation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif

def preprocess_input(feature_test,words_file="/home/mohamed/python/sherlok-tools/helpers/word_data.pkl", labels_file="/home/mohamed/python/sherlok-tools/helpers/label_data.pkl"):

    word_data = pickle.load( open(words_file, "r"))
    labels = pickle.load( open(labels_file, "r") )

    ### test_size is the percentage of events assigned to the test set (remainder go into training)
    ### split training & testing
    features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(word_data, labels, test_size=0.0, random_state=42)
    vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, encoding='windows-1256')
    features_train_transformed = vectorizer.fit_transform(features_train)
    features_test_transformed = vectorizer.transform(feature_test)

    selector = SelectPercentile(f_classif, percentile=10)
    selector.fit(features_train_transformed, labels_train)
    features_train_transformed = selector.transform(features_train_transformed).toarray()
    features_test_transformed = selector.transform(features_test_transformed).toarray()

    ### info on the data
    print ("no. of positive training files:", sum(labels_train))
    print ("no. of negative training files:", len(labels_train)-sum(labels_train))


    return features_train_transformed, features_test_transformed, labels_train



