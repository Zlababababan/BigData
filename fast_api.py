from fastapi import FastAPI

from joblib import load
clf = load('model_dumped.joblib')

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello world!"}

@app.get("/predict")
async def predict(text="empty"):
    return str(clf.predict([text])[0])
