# Drug Prediction System

This project predicts the most suitable drug for a patient based on basic medical attributes like age, blood pressure, cholesterol, and sodium-to-potassium ratio.

It uses a machine learning model served through a FastAPI backend and a simple Streamlit interface for interaction.

---

## What it does

* Takes patient details as input
* Sends the data to a FastAPI endpoint
* Uses a trained model to predict the drug
* Displays the result in a simple UI

---

## Tech used

* FastAPI (backend API)
* Streamlit (frontend UI)
* Scikit-learn (model)
* Pandas (data handling)
* Pydantic (validation)
* Pickle (model storage)

---

## Project structure

```
MiniProject/
│
├── main.py
├── frontend_st.py
├── requirements.txt
│
├── models/
│   └── pipeline.pkl
│
├── Pydantic_Schema/
│   ├── __init__.py
│   └── PydanticSchema.py
```

---

## How to run locally

### 1. Start FastAPI backend

```
uvicorn main:app --reload
```

Open:
http://127.0.0.1:8000/docs

---

### 2. Start Streamlit frontend

```
streamlit run frontend_st.py
```

Open:
http://localhost:8501

---

## API endpoint

### POST /predict

Takes input in this format:

```
{
  "Age": 23,
  "Sex": "M",
  "BP": "HIGH",
  "Cholesterol": "NORMAL",
  "Na_to_K": 15.2
}
```

Returns:

```
{
  "predicted_drug": "drugY"
}
```

---

## Notes

* The model is already trained and stored as `pipeline.pkl`
* FastAPI handles validation using Pydantic
* Streamlit is only used as a UI layer

---

## Possible improvements

* Add batch prediction endpoint
* Show prediction confidence
* Deploy frontend and backend online
* Add logging or database

---

## Author

Aaditya Gangurde
