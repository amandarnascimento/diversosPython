def maiornum(num1,num2):
    if num1 > num2:
        print("Numero 1 maior")
    if num1 == num2:
        print("Iguais")
    if num1 < num2:
        print("Número 1 menor")


numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um número: "))

resultado = maiornum(numero1,numero2)

print(resultado)