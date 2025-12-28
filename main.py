from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Definimos qué datos esperamos del ESP32
class DatosIoT(BaseModel):
    sensor: str
    valor: float

@app.get("/")
def inicio():
    return {"mensaje": "Servidor activo. Listo para recibir datos del ESP32"}

# Esta es la "puerta" que falta para corregir el error 405
@app.post("/")
async def recibir_datos(datos: DatosIoT):
    print(f"Dato recibido de {datos.sensor}: {datos.valor}")
    return {"estado": "recibido", "valor": datos.valor}
