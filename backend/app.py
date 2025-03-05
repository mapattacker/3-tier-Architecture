import os

import requests
from fastapi import FastAPI
from pydantic import BaseModel

from utils import (
    insert_data_to_db,
    fetch_recent_history
)


model_url = os.getenv("model_url")
app = FastAPI()


class InputRequest(BaseModel):
    sex: int
    age: int
    fare: int
    familysize: int


@app.post("/predict")
def process_request(request: InputRequest):
    response = requests.post(f"{model_url}/predict", json=request.dict())
    survive = response.json()["survived"]
    insert_data_to_db(
        request.sex, request.age, request.fare, request.familysize, survive
    )
    return {"response": survive}


@app.post("/history")
def history():
    history = fetch_recent_history()
    return {"history": history}
