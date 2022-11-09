# Define valores de variáveis 

frutas = []
estoque = 50


def adicionarfrutas():
  fruta = input("\nQue fruta é?\n")
  frutas.append(fruta)
  print(f'\n{fruta} foi adicionada no estoque!')

def encerrapqestoqueacabou():
  frutas.clear()
  estoque.clear()
  print('\nNão temos mais nada pra vender, sartee fora!')

def frutajaremovidadoestoque():
  print(f'\n{frutas[0]} foi vendida!')
  frutas.pop(0)
  
def consultaestoque():
  print(f'\n{estoque} itens!')11

def encerraratividade():
  estoque = 100  
  print('Obrigado, tudo encerrado!')

def main():
  print('O Gerenciador de Estoques foi iniciado!')
  
  while (estoque != 100):
    resposta = int(input("\n1 - Adicionar fruta ao estoque\n2 - Remover fruta do estoque\n3 - Consultar estoque\n4 - Encerrar vendas\n"))
    
    if (resposta == 1):
      adicionarfrutas()
      if (resposta == 2):
          frutajaremovidadoestoque()
          if (resposta == 3):
              consultaestoque()
              if (resposta == 4):
                  encerraratividade()
main()