import sys
import pandas

from sklearn import svm
from sklearn.model_selection import cross_val_score

def main():
    df = pandas.read_csv(sys.argv[1], sep = '\t')
    features = df.iloc[:,0:-1]
    labels = df.iloc[:,-1]

    clf = svm.SVC(kernel='linear', C=1)
    scores = cross_val_score(clf, features, labels, cv=10)

    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

if '__main__' == __name__:
    main()
