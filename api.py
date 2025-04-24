from fastapi import FastAPI, Request
from pydantic import BaseModel
import joblib
from utils import mask_pii

app = FastAPI()
clf = joblib.load("classifier_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

class EmailInput(BaseModel):
    email_body: str

@app.post("/classify")
async def classify_email(data: EmailInput):
    masked_text, entities = mask_pii(data.email_body)
    vec = vectorizer.transform([masked_text])
    category = clf.predict(vec)[0]
    return {
        "input_email_body": data.email_body,
        "list_of_masked_entities": entities,
        "masked_email": masked_text,
        "category_of_the_email": category
    }