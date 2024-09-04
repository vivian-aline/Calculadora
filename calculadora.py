nome = input('Digite o nome do usuário ')
print('Olá seja bem vindo', nome)


while True:
  num1 = int(input('Digite um número:'))
  operação = input('Digite uma oeração (+, - , *, /) ou "sair" para encerrar')
  if operação.lower() == 'sair':
    print('Ecerrando a calculadora...')
    break

  num2 = int(input('Digite outro Número'))

  if operação == '+':
    resultado = num1 + num2
  elif operação == '-':
    resultado = num1 - num2
  elif operação == '*':
    resultado = num1 * num2
  elif operação == '/':
    if num2 != 0:
      resultado = num1 / num2
    else:
      print('Erro: Divisão por zero!')
      continue
  else:
    print('Operação invalida')
    continue

  print('O resultado é:', resultado)
