from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import List

app = FastAPI()

# Lista para guardar los datos temporalmente
historial_datos = []

class DatosSensor(BaseModel):
    sensor: str
    valor: float

@app.get("/")
def inicio():
    # Ahora la página principal mostrará todos los datos recibidos
    return {
        "mensaje": "Panel de Control IoT",
        "lecturas_recibidas": len(historial_datos),
        "datos": historial_datos
    }

@app.post("/")
async def recibir_datos(datos: DatosSensor):
    nueva_lectura = {
        "sensor": datos.sensor,
        "valor": datos.valor,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Guardamos en la lista (mantenemos las últimas 20 lecturas)
    historial_datos.insert(0, nueva_lectura) 
    if len(historial_datos) > 20:
        historial_datos.pop()
        
    print(f"Guardado: {nueva_lectura}")
    return {"estado": "Exito", "dato": nueva_lectura}
