#Comentarios em Python sao com #
#Crie um programa que pegue o valor de uma conta
#de restaurante e divida pelo numero de pessoas
#Por fim some o valor da gorjeta em cima do 
#valor final

contaRestaurante = int(input("Qual o valor da conta: "))
numeroPessoas = int(input("Dividir para quantas pessoas: "))
porcentagemGorjeta = int(input("Qual a porcentagem da gorgeta: "))

valorCadaPessoa = (((contaRestaurante * porcentagemGorjeta ) / 100 ) + contaRestaurante ) / numeroPessoas

print(valorCadaPessoa)
