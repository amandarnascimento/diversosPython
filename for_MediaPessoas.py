# Programa que leia nome, idade e sexo de 3 pessoas
# resultado: pessoas com menos de  20 anos
# média de idade de todo o grupo
# nome da pessoa mais velha

soma_idade = 0
menorq20 = 0
media = 0
maior = 0

for i in range(0, 3):
    nome = input('Digite um nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo: ')
    soma_idade = soma_idade + idade

    if (idade < 20):
        menorq20 = menorq20 + 1
 
    if (idade > maior):
        maior = idade
        nomeMaisVelho = nome


media = soma_idade / 3


print('Menores que 20 anos ', menorq20)    
print('A média de idades das três pessoas: ', media)
print('O nome da pessoa mais velha é: ', nomeMaisVelho)