from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Esto define la estructura de tu JSON de Wokwi
class DatosSensor(BaseModel):
    sensor: str
    valor: float

@app.get("/")
def inicio():
    return {"mensaje": "Servidor activo"}

# Esta es la función que recibirá el POST de Wokwi
@app.post("/")
async def recibir_datos(datos: DatosSensor):
    # Esto aparecerá en los LOGS de Seenode
    print(f"LECTURA RECIBIDA: {datos.sensor} -> {datos.valor}")
    
    return {
        "estado": "Exito",
        "mensaje": "Dato guardado en la nube de Seenode",
        "dato_recibido": datos.valor
    }

   
