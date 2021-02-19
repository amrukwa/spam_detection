import pandas as pd
from sklearn import svm
import re
from nltk.corpus import stopwords
from encoding import preprocess
from joblib import dump, load

if __name__ == "__main__":
    mails = pd.read_csv("datasets\spam_ham_dataset.csv")
    x, y = mails["text"].values, mails["label_num"].values
    encoder = load('models/encoder.joblib') 
    X = preprocess(x, encoder)
    model = svm.SVC().fit(X, y)
    dump(model, 'models/predictor.joblib') 
