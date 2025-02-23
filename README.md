Sistema de Gerenciamento de Estoque de Produtos
Trabalho realizado para o INFNET. Sistema simples de gerenciamento de estoque de produtos. Ele permite a realização de várias operações de cadastro, atualização e consulta de produtos no estoque, como adicionar novos produtos, atualizar preços, listar itens, remover produtos, calcular o valor total do estoque e muito mais.

Funcionalidades
1. Cadastro de Produtos
Permite ao usuário cadastrar novos produtos, cada um com os seguintes atributos:

- Descrição
- Código (identificador único)
- Quantidade em estoque
- Custo do item
- Preço de venda por item

  
2. Inserção Inicial de Estoque
O sistema define um estoque inicial através de uma string contendo os dados dos produtos. Ao executar o programa, ele converte essa string em uma lista de dicionários para iniciar a manipulação do estoque.

3. Listagem de Produtos
Exibe todos os produtos cadastrados, mostrando informações como descrição, código, quantidade, custo e preço de venda.

4. Ordenação de Produtos por Quantidade
Permite ao usuário ordenar os produtos de acordo com a quantidade disponível em estoque, tanto em ordem crescente quanto decrescente.

5. Busca de Produtos
Realiza a busca de produtos no estoque por descrição ou código. Caso o produto seja encontrado, suas informações são exibidas. Caso contrário, uma mensagem apropriada será mostrada.

6. Remoção de Produtos
Permite ao usuário remover um produto do sistema através do código do produto.

7. Consulta de Produtos Esgotados
Exibe todos os produtos que possuem a quantidade em estoque igual a zero.

8. Filtro de Produtos com Baixa Quantidade
Filtra produtos com quantidade abaixo de um limite especificado pelo usuário e gera um relatório com esses itens.

9. Atualização de Estoque
Permite ao usuário atualizar a quantidade de um produto no estoque, tanto para entradas quanto para saídas.

10. Atualização de Preços
Permite ao usuário alterar o preço de venda de um produto específico.

11. Validação de Atualizações
Garante que as atualizações de quantidade não resultem em valores negativos e que o preço de venda nunca seja inferior ao custo do item.

12. Cálculo do Valor Total do Estoque
Calcula o valor total do estoque multiplicando a quantidade de cada item pelo seu preço de venda.

13. Cálculo do Lucro Presumido
Calcula o lucro presumido do estoque com base na diferença entre o preço de venda e o custo do item, multiplicado pela quantidade disponível. O lucro total é exibido no terminal.

14. Relatório Geral do Estoque
Exibe um relatório completo no terminal, incluindo a descrição, código, quantidade, custo, preço de venda e o valor total por item. No final do relatório, o custo total e o faturamento total do estoque também são apresentados.
