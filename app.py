from flask import Flask, request, Response, render_template
import pandas as pd
from models.encoding import preprocess
from joblib import dump, load

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
    result = "This message is " + meaning + "."
    return result
