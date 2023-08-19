altura = float(input('Digite a altura: '))
sexo = input('Digite o sexo: ')
error = 'n'

if(sexo == 'f'): 
    peso = (62.1 * altura) - 44.7

elif (sexo == 'm'):
    peso = (72.7 * altura) - 58

else: 
    error = 'y'


if (error == 'y'):
    print('Sexo inválido. Impossível calcular')
else:      
    print('O peso ideal é ', peso)