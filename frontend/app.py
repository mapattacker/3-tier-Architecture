import os

import requests
import streamlit as st
import pandas as pd


backend_url = os.getenv("backend_url")


def features():
    st.sidebar.subheader("Select Features")
    fsize = st.sidebar.slider("Family Size", min_value=0, max_value=10, value=0)
    fare = st.sidebar.slider("Ticket Price", min_value=0, max_value=500, value=50, step=10)
    sex = st.sidebar.selectbox("Sex", ["male", "female"])
    age = st.sidebar.slider("Age", min_value=0, max_value=100, value=30)

    if sex == "male":
        sex = 1
    else:
        sex = 0
    return fsize, fare, sex, age


def send_model(fsize, fare, sex, age):
    input_ = {
        "familysize": fsize,
        "fare": fare,
        "sex": sex,
        "age": age
    }

    response = requests.post(f"{backend_url}/predict", json=input_)
    if response.status_code == 200:
        result = response.json().get("response", "No response received")
        if result:
            st.success("Congrats! You survived!")
        else:
            st.error("No... You died!")
    else:
        st.error("Error communicating with FastAPI")


def request_history():
    st.subheader("Last 10 predictions")
    response = requests.post(f"{backend_url}/history")
    data = response.json()
    history = data.get("history", [])

    df = pd.DataFrame(history)
    st.table(df)


def header():
    st.title("Titantic Prediction")
    st.write("Predict how likely you are going to die if you were on board the doomed ship!")
    st.image("./titanic.png", width=550)


def body():
    fsize, fare, sex, age = features()
    if st.sidebar.button("Predict Your Survival!"):
        send_model(fsize, fare, sex, age)
        request_history()


if __name__ == "__main__":
    header()
    body()
