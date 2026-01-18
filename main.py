from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Variable global simple (en memoria) para controlar la lámpara
# En un proyecto real usarías una base de datos
estado_dispositivos = {
    "lampara": "OFF",
    "motor_velocidad": 0
}

class DatosSensor(BaseModel):
    sensor: str
    valor: float

@app.get("/")
def inicio():
    return {"mensaje": "Servidor de IoT activo", "estado_actual": estado_dispositivos}

# 1. El ESP32 envía datos aquí
@app.post("/")
async def recibir_datos(datos: DatosSensor):
    print(f"LECTURA RECIBIDA: {datos.sensor} -> {datos.valor}")
    
    # Respondemos al ESP32 y de paso le decimos qué debe hacer con la lámpara
    return {
        "estado": "Exito",
        "accion_lampara": estado_dispositivos["lampara"],
        "dato_recibido": datos.valor
    }

# 2. Tú usas esta ruta para encender/apagar la lámpara desde tu navegador
@app.get("/control/{dispositivo}/{accion}")
def controlar(dispositivo: str, accion: str):
    if dispositivo in estado_dispositivos:
        estado_dispositivos[dispositivo] = accion.upper()
        return {"mensaje": f"{dispositivo} actualizado a {accion}"}
    return {"error": "Dispositivo no encontrado"}
