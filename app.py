import streamlit as st

st.button('Re-run')

st.title('App')

from joblib import load
clf = load('model_dumped.joblib')

test = st.experimental_get_query_params()
st.write(test)

user_input = st.text_input("User input:")
result = clf.predict([user_input])

st.write(result)
