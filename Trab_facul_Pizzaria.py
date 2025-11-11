def menu():
  print('\n', '-' * 27,'    Opções do MENU    ','-' * 28)
  print('Tamanho P: Pizza Salgada (PS) custa 30 reais e a Pizza Doce (PD) custa 34 reais')
  print('Tamanho M: Pizza Salgada (PS) custa 45 reais e a Pizza Doce (PD) custa 48 reais')
  print('Tamanho G: Pizza Salgada (PS) custa 60 reais e a Pizza Doce (PD) custa 66 reais\n')

def pedido():
  global totalPedido #importando a varivável "acumuladora"

  #invocando as funções para questionar e validar as entradas do tipo e tamanho de pizza
  tipoPizza = validaTipo() 
  tamanho = validaTamanho()
  valorPizza = 0

  #calculando e incrementando a variável totalPedido
  if tipoPizza == 'PS':
    if tamanho == 'P':
      valorPizza = 30
      totalPedido += valorPizza
    elif tamanho == 'M':
      valorPizza = 45
      totalPedido += valorPizza
    else:
      valorPizza = 60
      totalPedido += valorPizza
    print(f'Você incluiu no pedido uma Pizza Salgada no tamanho {tamanho} de valor R$ {valorPizza}.')
  else:
    if tamanho == 'P':
      valorPizza = 34
      totalPedido += valorPizza
    elif tamanho == 'M':
      valorPizza = 48
      totalPedido += valorPizza
    else:
      valorPizza = 66
      totalPedido += valorPizza
    print(f'Você incluiu no pedido uma Pizza Doce no tamanho {tamanho} de valor R$ {valorPizza}.')

  return totalPedido  #retonando o valor total do pedido para o programa principal

def validaTipo():  #função para validar a entrada do tipo de pizza
  print('Informe o tipo de pizza, sendo PS para pizza salgada ou PD para pizza doce.')
  while True:
    try:
      tipoPizza = input('Qual tipo de pizza deseja (PS ou PD): ').upper().strip()
      if tipoPizza == 'PS' or tipoPizza == 'PD':
        return tipoPizza  #se opção válida, retorna o tipoPizza para a função pedido()
      else:
        print('Sabor inválido. Tente novamente!')
        continue
    except:
      print('Sabor inválido. Tente novamente!')

def validaTamanho():  #função para validar a entrada do tamanho de pizza
  print('\nAgora escolha o tamanho da pizza, sendo P para pequeno, M para médio ou G para grande')
  while True:
    try:
      tamanho = input('Informe o tamanho (P, M ou G): ').upper().strip()
      if tamanho == 'P' or tamanho == 'M' or tamanho == 'G':
        return tamanho  #se opção válida, retorna o tamanho para a função pedido()
      else:
        print('Tamanho inválido. Tente novamente.')
    except:
      print('Tamanho inválido. Tente novamente.')

###### Programa principal ######

totalPedido = 0.0  #inicializando a variável acumuladora com tipo float.
print('-------  Bem vindos a pizzaria do pizzaiolo Charles Silva da Silva   -------')
menu()  # apresentação do Menu ao usuário
nomeCliente = input('Informe seu nome: ')
print(f'Deseja fazer um pedido {nomeCliente}?')

while True:  #laço para validar a resposta do cliente
  desejo = input('Informe SIM ou NÃO: ').upper()
  if desejo == 'SIM' or desejo == 'S':
    print()
    pedido() # Se cliente respondeu SIM, invoca a função para fazer pedidos
    print(f'\nO valor atual do pedido é de: R$ {totalPedido:.2f}') # retorno após a função pedido()
    print(f'Deseja pedir mais alguma coisa {nomeCliente}?') # pergunta antes de reiniciar o laço
      
  elif desejo == 'NÃO' or desejo == 'NAO' or desejo == 'N':
      break
  else:
    print('Ops! Tente novamente.')
    
if totalPedido != 0.0:    #checa se o cliente fez algum pedido
  while True:  #questiona o usuário de deseja concluir ou cancelar o pedido
    print(f'\nO valor total do pedido é de: R$ {totalPedido:.2f}')
    desejo = input('Digite 1 para concluir, 2 para incluir mais intens ou 3 para cancelar: ').strip()
    if desejo == '1':
      print(f'\nObrigado por comprar conosco {nomeCliente}!')
      print('Dirija-se ao caixa para efetuar o pagemento.')
      break
    elif desejo == '2': 
      menu()  # apresentando novamente o menu ao usuário
      pedido() # invocando a função para fazer adicionar itens ao pedido
      continue
    elif desejo == '3':
      print(f'\nTudo bem {nomeCliente}, o pedido foi cancelado.')
      break
    elif desejo != '1' or desejo != '2':
      print('humm. Tente novamente.')
      continue
else:  #conclui o programa depois da negativa de pedido
  print(f'\nAh que pena {nomeCliente}! Fica para uma próxima.') 
