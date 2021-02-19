
import pandas as pd
import re
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from joblib import dump

def clean(text):
    StopWords = stopwords.words("english")
    text = text[len('subject: '):]
    text = text.lower()
    text = ' '.join([word for word in text.split() if word not in StopWords])
    text = re.sub(r'([^a-zA-Z ]+?)',' ', text)
    text = re.sub(' +', ' ', text)
    return text

def clean_messages(messages):
    cleaned = [clean(text) for text in messages]
    return cleaned

def preprocess(messages, model):
    cleaned = clean_messages(messages)
    transformed = model.transform(cleaned)
    return transformed

if __name__ == "__main__":
    mails = pd.read_csv("datasets\spam_ham_dataset.csv")
    x, y = mails["text"].values, mails["label_num"].values
    x = clean_messages(x)
    vectorizer = CountVectorizer()
    vectorizer.fit(x)
    dump(vectorizer, 'models/encoder.joblib') 
