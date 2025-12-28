from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def mensaje_de_bienvenida():
    return {"status": "Servidor de Electronica Activo", "docente": "Peru"}

@app.get("/lectura/{valor}")
def recibir_sensor(valor: float):
    return {"mensaje": "Dato recibido", "valor_del_esp32": valor}
