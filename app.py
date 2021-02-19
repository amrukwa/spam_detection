from flask import Flask, request, Response, render_template
import pandas as pd
import nltk
from nltk.corpus import stopwords
from models.encoding import preprocess
from joblib import dump, load

nltk.download('stopwords')
mapped_results = ["ham", "spam"]
encoder = load('models/encoder.joblib') 
predictor = load('models/predictor.joblib')

app = Flask(__name__)

@app.route('/')
def get_text():
    return render_template('text_form.html')

@app.route('/', methods=['POST'])
def check_message():
    text = [request.form['text']]
    X = preprocess(text, encoder)
    value = predictor.predict(X)
    meaning = mapped_results[value[0]]
    return render_template('result.html', result=meaning)
