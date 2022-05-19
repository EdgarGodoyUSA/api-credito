from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
url = "http://127.0.0.1:8000/predict"
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})



@app.post("/consultar")
def consultar(nombre: str=Form(...), sexo: str=Form(...),
            edad: int=Form(...),
            monto: int=Form(...),
            tipovivienda: str=Form(...)):
     data = {"sexo": sexo, "edad": edad,
                             "monto": monto, "tipovivienda": tipovivienda}
     
     response = requests.post(url, data=data)
     print(response)
     respuesta = response.json()
     print(respuesta)
     if respuesta["proba_bad_client"] > 0.5:
        mensaje = f"Apreciado {nombre}, no le podemos prestar dinero."
     else:
        mensaje = f"Apreciado {nombre}, su credito fue aprobado"
        
     return mensaje