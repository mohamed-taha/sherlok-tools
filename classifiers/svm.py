# -*- coding: utf-8 -*-
#!/usr/bin/python

""" 
    use a suooprt vector machine Classifier to identify polarity of text
    
    polarity and labels:
    negative has label 0
    positive has label 1

"""
from sklearn.svm.classes import LinearSVC

import sys
from time import time
sys.path.append("/home/mohamed/python/sherlok-tools/helpers/")
from text_preprocess import Preprocess
#from preprocess_input import preprocess_input
from sklearn import svm


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = Preprocess()

# classification goes here

clf = svm.SVC(kernel="linear")

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
#text = ['يحب']
#print "prediction of ", clf.predict(text)


#SVC rbf
print("RBF")
clf_rbf=svm.SVC()

# training
train_r0 = time()
clf_rbf.fit(features_train, labels_train)
train_r1 = time()

# prediction or testing
test_r0 = time()
predict = clf_rbf.predict(features_test)
test_r1 = time()

print "accuracy: ", clf_rbf.score(features_test, labels_test)
print "#################################"
print "tain time: ", round(train_r1 - train_r0, 3), "s"
print "prediction time: ", round(test_r1 - test_r0, 3), "s"
print "#################################"

#SVC lib_linear
print("lib_linear")
clf_lib=LinearSVC()

# training
train_l0 = time()
clf_lib.fit(features_train, labels_train)
train_l1 = time()

# prediction or testing
test_l0 = time()
predict = clf_lib.predict(features_test)
test_l1 = time()

print "accuracy: ", clf_lib.score(features_test, labels_test)
print "#################################"
print "tain time: ", round(train_l1 - train_l0, 3), "s"
print "prediction time: ", round(test_l1 - test_l0, 3), "s"