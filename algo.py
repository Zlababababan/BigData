from datetime import datetime
def current_time():
    return datetime.now().strftime("%H:%M:%S")


import streamlit as st
import numpy as np
import pandas as pd

st.button("Re-run")

st.title('Big Data TP2')

csv = pd.read_csv('labels.csv')
csv

from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multiclass import OneVsRestClassifier
from stop_words import get_stop_words
from sklearn.svm import SVC
clf = make_pipeline(
    TfidfVectorizer(stop_words=get_stop_words('en')),
    OneVsRestClassifier(SVC(kernel='linear', probability=True))
)

X = csv['tweet']
Y = csv['class']

st.write('Start fit: ', current_time())
clf.fit(X, Y)
st.write('fit finished: ', current_time())

from joblib import dump
st.write('Start dump: ', current_time())
dump(clf, 'model_dumped.joblib')
st.write('Dump finished: ', current_time())
