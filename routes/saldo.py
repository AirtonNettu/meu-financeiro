from fastapi import APIRouter

roteador = APIRouter(prefix="/saldo", tags=["Saldo"])



@roteador.get("/")
def consultar_saldo():
    return {"saldo": 0}