from fastapi import FastAPI
from routes.saldo import roteador as roteador_saldo

app = FastAPI()

app.include_router(roteador_saldo)

@app.get("/")
def inicio():
    return {"message": "Meu financeiro funcionando"}