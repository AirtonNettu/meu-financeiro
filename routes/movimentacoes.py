from fastapi import APIRouter

roteador = APIRouter(
    prefix="/movimentacoes",
    tags=["Movimentações"]
)

@roteador.get("/")
def consultar_movimentacoes():
    return {"message": "Rota de movimentações funcinando!"}