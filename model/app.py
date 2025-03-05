from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()


MODEL_PATH = "model.pkl"
with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)


class InputRequest(BaseModel):
    sex: int
    age: int
    fare: int
    familysize: int


@app.post("/predict")
def predict(request: InputRequest):
    input_data = np.array(
        [[request.sex, request.age, request.fare, request.familysize]]
    )
    # 0 = did not survive, 1 = survived
    prediction = model.predict(input_data)[0]
    return {"survived": bool(prediction)}
