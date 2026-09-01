from fastapi import APIRouter
from database.conexao import calcular_saldo


roteador = APIRouter(prefix="/saldo", tags=["Saldo"])



@roteador.get("/")
def consultar_saldo():
    saldo = calcular_saldo()
    return {"saldo": saldo}