#media de uma lista de numeros

lista =[0, 1, 6, 8, 64, 42]
soma = 0
contagem = 0



for numero in lista:
    soma = soma + numero
    contagem = contagem + 1

media = soma / contagem 
print(media)
