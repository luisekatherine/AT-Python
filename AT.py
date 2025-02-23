# estoque inicial
estoque_inicial = "Notebook Dell;201;15;3200.00;4500.00#Notebook Lenovo;202;10;2800.00;4200.00#Mouse Logitech;203;50;70.00;150.00#Mouse Razer;204;40;120.00;250.00#Monitor Samsung;205;10;800.00;1200.00#Monitor LG;206;8;750.00;1150.00#Teclado Mecânico Corsair;207;30;180.00;300.00#Teclado Mecânico Razer;208;25;200.00;350.00#Impressora HP;209;5;400.00;650.00#Impressora Epson;210;3;450.00;700.00#Monitor Dell;211;12;850.00;1250.00#Monitor AOC;212;7;700.00;1100.00"

# transforma a string de estoque inicial para um formato de lista de dicionários
def carregar_estoque(estoque_inicial):
  produtos = estoque_inicial.split('#')
  estoque = []
  for produto in produtos:
    dados = produto.split(';')
    estoque.append({
      'descricao': dados[0],
      'codigo': int(dados[1]),
      'quantidade': int(dados[2]),
      'custo': float(dados[3]),
      'preco_venda': float(dados[4])
    })
  return estoque

# variável global de estoque chamando a função
estoque = carregar_estoque(estoque_inicial)

# cadastro de produtos
def cadastrar_produto(descricao, codigo, quantidade, custo, preco_venda):
  """Função para cadastrar um novo produto"""
  produto = {
    'descricao': descricao,
    'codigo': codigo,
    'quantidade': quantidade,
    'custo': custo,
    'preco_venda': preco_venda
  }
  estoque.append(produto)
  print(f"O produto '{descricao}' foi cadastrado com sucesso!")

# listar produtos
def listar_produtos():
  """Função que lista todos os produtos que foram cadastrados no sistema"""
  print(f"{'Descrição'.ljust(30)}{'Código'.rjust(12)}{'Quantidade'.rjust(12)}{'Custo'.rjust(12)}{'$$ Venda'.rjust(15)}")
  for produto in estoque:
    print(f"{produto['descricao'].ljust(30)}{str(produto['codigo']).rjust(12)}{str(produto['quantidade']).rjust(12)}{str(produto['custo']).rjust(12)}{str(produto['preco_venda']).rjust(15)}")

# ordenar produtos por quantidade
def ordenar_por_quantidade(ordem='asc'):
  """Função que ordena os produtos pela quantidade, seja crescente ou decrescente"""
  if ordem not in ['asc', 'desc']:
    print("Ops! Valor inválido. Use 'asc' para crescente ou 'desc' para decrescente.")
    return

  reverse = True if ordem == 'desc' else False
  estoque.sort(key=lambda x: x['quantidade'], reverse=reverse)
    
  print(f"\nProdutos ordenados por quantidade ({'crescente' if ordem == 'asc' else 'decrescente'}):")
  print(f"{'Descrição'.ljust(30)}{'Código'.rjust(10)}{'Quantidade'.rjust(12)}")
  for produto in estoque:
    print(f"{produto['descricao'].ljust(30)}{str(produto['codigo']).rjust(10)}{str(produto['quantidade']).rjust(12)}")


# buscar produto
def buscar_produto(descricao=None, codigo=None):
  """Função para buscar produtos com base na descrição ou no código"""
  produtos_encontrados = []
  
  # verifica se foi informado um código ou uma descrição
  if descricao:
    for produto in estoque:
      if descricao.lower() in produto['descricao'].lower():
        produtos_encontrados.append(produto)
  elif codigo is not None:
    for produto in estoque:
      if produto['codigo'] == codigo:
        produtos_encontrados.append(produto)

  # exibe os produtos encontrados, se não encontra nada, exibe mensagem na tela
  if produtos_encontrados:
    print(f"{'Descrição'.ljust(30)}{'Código'.rjust(10)}{'Quantidade'.rjust(12)}{'Custo'.rjust(10)}{'Preço Venda'.rjust(15)}")
    for produto in produtos_encontrados:
      print(f"{produto['descricao'].ljust(30)}{str(produto['codigo']).rjust(10)}{str(produto['quantidade']).rjust(12)}{str(produto['custo']).rjust(10)}{str(produto['preco_venda']).rjust(15)}")
  else:
    print("O produto não foi encontrado.")

# remove um produto usando o código como parâmetro
def remover_produto(codigo):
  """Função para remover produto com base no código"""
  global estoque
  estoque = [produto for produto in estoque if produto['codigo'] != codigo]
  print(f"Produto com código {codigo} removido!")

# consulta os produtos esgotados
def consultar_esgotados():
  """Exibe os produtos esgotados"""
  esgotados = [produto for produto in estoque if produto['quantidade'] == 0]
  if esgotados:
    print(f"{'Descrição'.ljust(30)}{'Código'.rjust(10)}{'Quantidade'.rjust(12)}")
    for produto in esgotados:
      print(f"{produto['descricao'].ljust(30)}{str(produto['codigo']).rjust(10)}{str(produto['quantidade']).rjust(12)}")
  else:
    print("Não temos produtos esgotados.")

# filtro de produtos com baixa quantidade no estoque
def filtro_baixa_quantidade(limite=5):
  """Exibe produtos com quantidade abaixo de um limite"""
  poucos_produtos = [produto for produto in estoque if produto['quantidade'] < limite]
  if poucos_produtos:
    print(f"{'Descrição'.ljust(30)}{'Código'.rjust(10)}{'Quantidade'.rjust(12)}")
    for produto in poucos_produtos:
      print(f"{produto['descricao'].ljust(30)}{str(produto['codigo']).rjust(10)}{str(produto['quantidade']).rjust(12)}")
  else:
    print("Não temos produtos com baixa quantidade.")

# atualiza o estoque
def atualizar_estoque(codigo, quantidade):
  """Atualiza a quantidade de um produto no estoque"""
  for produto in estoque:
    if produto['codigo'] == codigo:
      if produto['quantidade'] + quantidade >= 0:
        produto['quantidade'] += quantidade
        print(f"Estoque do produto {produto['descricao']} atualizado com sucesso!")
      else:
        print("Não é possível ter quantidade negativa.")
      return
  print("O produto não foi encontrado.")

# atualiza o preço
def atualizar_preco(codigo, novo_preco):
  """Atualiza o preço de venda de um produto"""
  for produto in estoque:
    if produto['codigo'] == codigo:
      if novo_preco >= produto['custo']:
        produto['preco_venda'] = novo_preco
        print(f"O preço do produto '{produto['descricao']}' foi atualizado com sucesso!")
      else:
        print("O novo preço não pode ser menor que o custo do produto.")
      return
  print("O prroduto não foi encontrado.")

# calcula o valor total do estoque
def calcular_valor_estoque():
  """Calcula o valor total do estoque"""
  valor_total = sum(produto['quantidade'] * produto['preco_venda'] for produto in estoque)
  print(f"Valor total do estoque: {valor_total:.2f}")

# calcula o lucro presumido
def calcular_lucro_presumido():
  """Calcula o lucro presumido do estoque"""
  lucro_total = sum((produto['preco_venda'] - produto['custo']) * produto['quantidade'] for produto in estoque)
  print(f"Lucro presumido total: {lucro_total:.2f}")

# traz um relatório geral
def relatorio_geral():
  """Exibe um relatório geral com todos os produtos e valores"""
  print(f"{'Descrição'.ljust(30)}{'Código'.rjust(10)}{'Quantidade'.rjust(12)}{'Custo'.rjust(10)}{'Preço Venda'.rjust(15)}{'Total'.rjust(15)}")
  for produto in estoque:
    total_item = produto['quantidade'] * produto['preco_venda']
    print(f"{produto['descricao'].ljust(30)}{str(produto['codigo']).rjust(10)}{str(produto['quantidade']).rjust(12)}{str(produto['custo']).rjust(10)}{str(produto['preco_venda']).rjust(15)}{str(total_item).rjust(15)}")
  total_estoque = sum(produto['quantidade'] * produto['preco_venda'] for produto in estoque)
  custo_total = sum(produto['quantidade'] * produto['custo'] for produto in estoque)
  print(f"{'Custo Total'.ljust(60)}{custo_total:.2f}")
  print(f"{'Faturamento Total'.ljust(60)}{total_estoque:.2f}")

# menu interativo
def menu():
  """Função de menu interativo"""
  while True:
    print("\n****************************************")
    print("Menu:")
    print("1. Listar produtos")
    print("2. Ordenar produtos por quantidade")
    print("3. Buscar produto")
    print("4. Remover produto")
    print("5. Consultar produtos esgotados")
    print("6. Filtro de produtos com baixa quantidade")
    print("7. Atualizar estoque")
    print("8. Atualizar preço")
    print("9. Calcular valor total do estoque")
    print("10. Calcular lucro presumido")
    print("11. Relatório geral do estoque")
    print("0. Sair")
    print("****************************************")
    opcao = input("Escolha uma opção, digitando apenas o número da opção escolhida: ")
    
    if opcao == '1':
      listar_produtos()
    elif opcao == '2':
      ordem = input("Digite 'asc' para crescente ou 'desc' para decrescente: ")
      ordenar_por_quantidade(ordem)
    elif opcao == '3':
      busca_tipo = input("Digite 'descricao' para buscar por descrição ou 'codigo' para buscar por código: ").strip().lower()
      if busca_tipo == 'descricao':
        descricao = input("Digite a descrição do produto: ").strip()
        buscar_produto(descricao=descricao)
      elif busca_tipo == 'codigo':
        codigo = int(input("Digite o código do produto: ").strip())
        buscar_produto(codigo=codigo)
      else:
        print("Opção inválida. Tente novamente.")
    elif opcao == '4':
      codigo = int(input("Digite o código do produto a ser removido: "))
      remover_produto(codigo)
    elif opcao == '5':
      consultar_esgotados()
    elif opcao == '6':
      limite = int(input("Digite o limite de baixa quantidade (ou aperte Enter para usar o padrão de 5): ") or 5)
      filtro_baixa_quantidade(limite)
    elif opcao == '7':
      codigo = int(input("Digite o código do produto: "))
      quantidade = int(input("Digite a quantidade a ser alterada (pode ser negativa): "))
      atualizar_estoque(codigo, quantidade)
    elif opcao == '8':
      codigo = int(input("Digite o código do produto: "))
      novo_preco = float(input("Digite o novo preço: "))
      atualizar_preco(codigo, novo_preco)
    elif opcao == '9':
      calcular_valor_estoque()
    elif opcao == '10':
      calcular_lucro_presumido()
    elif opcao == '11':
      relatorio_geral()
    elif opcao == '0':
      print("Saindo...")
      break
    else:
      print("Ops! Opção inválida. Tente novamente.")

# executa o menu interativo
menu()