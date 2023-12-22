from domain.models import Produto

class ProdutoFactory:
    def call(self, nome: str, quantidade: str, preco: str, tipo: str) -> Produto:
        raise NotImplementedError()