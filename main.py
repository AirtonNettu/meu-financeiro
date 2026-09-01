from fastapi import FastAPI
from routes.saldo import roteador as roteador_saldo
from routes.movimentacoes import roteador as roteador_movimentacoes

app = FastAPI()

app.include_router(roteador_saldo)
app.include_router(roteador_movimentacoes)

@app.get("/")
def inicio():
    return {"message": "Meu financeiro funcionando"}