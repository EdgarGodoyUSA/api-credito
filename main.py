from fastapi import FastAPI, Form
import joblib
import boto3
import os

app = FastAPI()

##pipeline = joblib.load("modelos/pipeline1.joblib")
##modelo = joblib.load("modelos/model01.joblib")

s3 = boto3.resource('s3', 'us-east-1')

s3.meta.client.download_file('modelo-credito-mia', 'modelos/pipeline1.joblib' , 'pipeline.joblib')

s3.meta.client.download_file('modelo-credito-mia', 'modelos/model01.joblib' , 'model.joblib')

transformer = joblib.load('pipeline.joblib')

model = joblib.load('model.joblib')

os.remove('pipeline.joblib')

os.remove('model.joblib')

@app.post("/predict")
def predict(sexo: str=Form(...),
            edad: int=Form(...),
            monto: int=Form(...),
            tipovivienda: str=Form(...)):

    X = transformer.transform([[sexo, edad, monto, tipovivienda]])
    
    proba_bad_client = model.predict_proba(X)[0][1]
    

    return {"proba_bad_client": proba_bad_client}
