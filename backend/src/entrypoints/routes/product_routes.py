# api.py
from fastapi import FastAPI, HTTPException
from backend.src.domain.models.product import Product
from backend.src.domain.services.controllers import DatabaseController
from backend.src.infraestructure.product_repositories.product_repository_postgres import ProductRepositoryPostgres

app = FastAPI()
database_controller = DatabaseController()
product_repository = ProductRepositoryPostgres()
produto_service = ProductRepositoryPostgres(product_repository, database_controller)

@app.post('/cadastrar_produto')
def cadastrar_produto(produto: Product):
    return produto_service.cadastrar_produto(produto)

@app.get('/obter_produtos')
def obter_produtos():
    return produto_service.obter_produtos()

@app.get('/obter_produto/{produto_id}')
def obter_produto(produto_id: int):
    produto = produto_service.obter_produto_por_id(produto_id)
    if produto:
        return produto
    raise HTTPException(status_code=404, detail="Produto não encontrado")

@app.put('/atualizar_produto/{produto_id}')
def atualizar_produto(produto_id: int, produto: Product):
    produto_atualizado = produto_service.atualizar_produto(produto, produto_id)
    if produto_atualizado:
        return produto_atualizado
    raise HTTPException(status_code=404, detail="Produto não encontrado")

@app.delete('/deletar_produto/{produto_nome}')
def deletar_produto(produto_nome: str):
    return produto_service.deletar_produto(produto_nome)
