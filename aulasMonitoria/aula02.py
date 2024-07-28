# faca um programa que some todos os numros impares de 1 a 20

# primeiro desenvolva um contador de 1 a 20 depois de cada iteração verifique se o numero é impar
#se for impar some em uma variavel previamente iniciada em 0,

soma_par = 0

for i in range(1, 41):
    if i % 2 == 0:
        soma_par = soma_par + i

print(soma_par)