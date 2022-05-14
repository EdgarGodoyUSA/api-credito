from fastapi import FastAPI, Form
import joblib

app = FastAPI()

pipeline = joblib.load("modelos/pipeline1.joblib")
modelo = joblib.load("modelos/model01.joblib")

@app.post("/predict")
def predict(sexo: str=Form(...),
            edad: int=Form(...),
            monto: int=Form(...),
            tipovivienda: str=Form(...)):

    X = pipeline.transform([[sexo, edad, monto, tipovivienda]])
    
    proba_bad_client = modelo.predict_proba(X)[0][1]
    

    return {"proba_bad_client": proba_bad_client}
