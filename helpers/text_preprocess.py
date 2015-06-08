#!/usr/bin/python

import pickle
import numpy

from sklearn import cross_validation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif


def Preprocess(words_file="/home/mohamed/python/sherlok-tools/helpers/word_data.pkl", labels_file="/home/mohamed/python/sherlok-tools/helpers/label_data.pkl"):
    """ 
        this function takes a pre-made list of data texts (by default word_data.pkl)
        and the corresponding labels (by default label_data.pkl) and performs
        a number of preprocessing steps:
            -- splits into training/testing sets (10% testing)
            -- vectorizes into tfidf matrix
            -- selects/keeps most helpful features

        after this, the feaures and labels are put into numpy arrays, which play nice with sklearn functions

        4 objects are returned:
            -- training/testing features
            -- training/testing labels

    """

    ### the words (features) and labels (positive or negative)
    word_data = pickle.load( open(words_file, "r"))
    labels = pickle.load( open(labels_file, "r") )

    ### test_size is the percentage of events assigned to the test set (remainder go into training)
    features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(word_data, labels, test_size=0.1, random_state=42)

    ### text vectorization--go from strings to lists of numbers
    vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5)
    features_train_transformed = vectorizer.fit_transform(features_train)
    features_test_transformed = vectorizer.transform(features_test)

    ### feature selection, because text is super high dimensional and 
    ### can be really computationally chewy as a result
    selector = SelectPercentile(f_classif, percentile=10)
    selector.fit(features_train_transformed, labels_train)
    features_train_transformed = selector.transform(features_train_transformed).toarray()
    features_test_transformed = selector.transform(features_test_transformed).toarray()

    ### info on the data
    print "no. of positive training files:", sum(labels_train)
    print "no. of negative training files:", len(labels_train)-sum(labels_train)

    return features_train_transformed, features_test_transformed, labels_train, labels_test        	