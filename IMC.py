peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

# Correção do cálculo do IMC
imc = peso / (altura ** 2)

if imc < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= imc <= 24.9:
    print('PESO IDEAL') 
elif 25 <= imc <= 29.9:
    print('LEVEMENTE ACIMA DO PESO')
elif imc >= 30:
    print('OBESIDADE GRAU I')
