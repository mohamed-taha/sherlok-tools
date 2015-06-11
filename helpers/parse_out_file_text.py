#!/usr/bin/python

from nltk.stem.snowball import SnowballStemmer
import string

def parseOutText(f):
    """ given an opened text file f, parse out all text """

    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read().strip()

    words = ""
    if len(all_text) > 1:
        ### remove punctuation
        words = all_text.translate(string.maketrans("", ""), string.punctuation)

    return words

def main():
    ff = open("/home/mohamed/python/sherlok-tools/datasets/Twitter/Positive/positive117.txt", "r")
    text = parseOutText(ff)
    print text


if __name__ == '__main__':
    main()

