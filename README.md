# Calculadora

calculadora.sh

Para executar o arquivo .sh no Linux, siga os passos abaixo:
 - Abra o terminal no menu de aplicativos.
 - Vá até o diretório onde o arquivo foi salvo, usando o comando cd
 - Use o comando chmod para tornar o arquivo executável: chmod +x calculadora.sh
 - Por fim execute o arquivo usando o comando ./calculadora.sh
 
calculadora.py

Este código cria um menu interativo, para uma calculadora básica, com operações de soma, subtração, multiplicação e divisão. veja como ele funciona:
 - Estrutura básica do código: utiliza um loop While True para criar um menu que continua exibindo até que o usuário deseje sair.
 - Exibindo o menu: o código pede para que o usuário digite um número, assim que ele é feito, o código pede que escolha a operação desejada (+, -, *, /), ou escreva "sair" para encerrar o programa, se o úsuário escolher uma operação, o código segue pedindo o segundo número.
 - Executando a operação selecionada:
   - soma (+): Soma os dois números e exibe o resultado;
   - subtração (-): Subtrai o primeiro número do segundo e exibe o resultado;
   - multiplicação: Multiplica os dois números e exibe o resultado;
   - divisão (/): Divide o primeiro numero pelo segundo e exibe o resultado, caso a divisão for por zero, irá imprimir na tela "operação inválida".
