import pickle
import sys

import pandas
from sklearn import svm

def make_classifier(df):
    features = df.iloc[:,0:-1]
    labels = df.iloc[:,-1]

    clf = svm.SVC(gamma=0.001, C=100.)
    clf.fit(features, labels)

    return clf

def main():
    infile, outfile = sys.argv[1:]
    if '-' == infile:
        infile = sys.stdin
    df = pandas.read_csv(infile, sep = '\t')
    with open(outfile, 'wb') as fp:
        fp.write(pickle.dumps(make_classifier(df)))

if '__main__' == __name__:
    main()
