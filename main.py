from Pydantic_Schema.PydanticSchema import PatientDetails,PredictionOutput
from fastapi import FastAPI, HTTPException
import pickle
import pandas as pd
import os

model_path = os.path.join("models", "pipeline.pkl")

app= FastAPI()

try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
except Exception as e:
    raise RuntimeError(f"Failed to load model: {e}")

# def load_model():
#     try:
#         with open(model_path, "rb") as f:
#             model = pickle.load(f)
#             return model
#     except Exception:
#         raise RuntimeError("Failed to load the model. \nTry Again")
    

@app.get('/')
def default():
    return {"message":"Welcome to FastAPI miniproject! \nHome Page"}


@app.post("/predict", response_model=PredictionOutput)
def predict(patient : PatientDetails):
    
    # model= load_model()
    
    input_dict= patient.model_dump() # converts into dict

    input_df= pd.DataFrame([input_dict])

    try:
        prediction= model.predict(input_df)
    except Exception:
        raise HTTPException(status_code=500, detail="Prediction failed!")
    
    return {"predicted_drug": prediction[0]}


@app.get("/health")
def health():
    return {"status": "ok"}