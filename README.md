## Burocracia de Implementação
#### Definição do MVP
- Cadastro de Produtos
    - Capacidade de adicionar novos produtos ao sistema, incluindo informações básicas como nome, descrição, quantidade, tipo, etc.
- Listagem de produtos
    - Mostrar todos os produtos cadastrados, permitindo visualizar suas informações.
- Atualização de Produtos
    - Editar informações de produtos existentes, como nome, descrição, quantidade e tipo.
- Remoção de Produtos
    - Excluir produtos que não são mais necessários no sistema.
- Busca por nome
    - Possibilidade de pesquisar produtos por nome, facilitando a localização de itens específicos na lista.
- Ordenação (Quantidade de Tipo)
    -  Capacidade de ordenar a lista de produtos com base na quantidade disponível ou no tipo de produto (por exemplo, ordenar do maior para o menor em termos de quantidade).

### Escolha de linguagem
> Optamos pela linguagem Python devido à sua compreensibilidade, tornando-a menos propensa a erros por parte dos desenvolvedores. Considerando a urgência na entrega do projeto e o fato de que o sistema não requer a velocidade e segurança associadas a linguagens de baixo nível, Python se apresenta como uma escolha adequada. Além disso, a familiaridade dos desenvolvedores com a linguagem escolhida influenciou essa decisão, facilitando a implementação e manutenção do sistema.

### Regra de negócio
- Blocos
    - Criar
        - Capturar dados(id_produto, nome, preço, quantidade, tipo).
        - Autenticar dados.
        - Caso os dados estejam corretos, salvar.
    - Atualizar
        - Capturar dados (id_produto, novo_nome, novo_preço, nova_quantidade, novo_tipo).
        - Autenticar dados.
        - Caso os dados estejam corretos, deletar o conjunto de dados.
    - Deletar
        - Capturar (id_produto, nome, preço, quantidade, tipo).
        - Autenticar dados.
        - Caso os dados estejam corretos retornar dados (nome, preço, tipo).
    - Acessar
        - Capturar (id_produto).
        - Autenticar dados.
        - Caso os dados estejam corretos, retornar dados (nome, preço, tipo).
- Componentes
- Funcionalidades

### Design de codigo