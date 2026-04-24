from pydantic import BaseModel, Field
from typing import Annotated, Literal

class PatientDetails(BaseModel):

    Age: Annotated[
        int,
        Field(..., gt=0, description="Age of patient", example=23)
    ]

    Sex: Annotated[
        Literal['M', 'F'],
        Field(..., description="Sex of patient", example='M')
    ]

    BP: Annotated[
        Literal['LOW', 'NORMAL', 'HIGH'],
        Field(..., description="Blood pressure level", example='HIGH')
    ]

    Cholesterol: Annotated[
        Literal['NORMAL', 'HIGH'],
        Field(..., description="Cholesterol level", example='NORMAL')
    ]

    Na_to_K: Annotated[
        float,
        Field(..., gt=0, description="Na to K ratio", example=15.2)
    ]

class PredictionOutput(BaseModel):
    predicted_drug: Annotated[Literal['drugA','drugB','drugC','drugX','drugY'], Field(..., description='Drug predicted to the patient', example='drugA')]
    