def somar(num1, num2):
    soma = num1 + num2
    return soma

def subtrair(num1, num2):
    sub = num1 - num2
    return sub

def multiplicar(num1, num2):
    mult = num1 * num2
    return mult

def dividir(num1, num2):
    if num2 != 0:
        num1 / num2
    else:
        print("Erro, não existe divisão por zero!")

def ler_opcao_escolha_user(opcao, numero1, numero2):
    if opcao == 1:
        return somar(numero1, numero2)
    if opcao == 2:
        return subtrair(numero1, numero2) 
    if opcao == 3:
        return multiplicar(numero1, numero2) 
    if opcao == 4:
        return dividir(numero1, numero2) 

print("1- para somar")
print("2- para subtrair")
print("3- para multiplicar")
print("4- para dividir")
print("5- para sair")


while True: 

    opcao = int(input("Digite a opção escolhida: "))
    if opcao > 5 or opcao < 0 :
        continue
    if opcao == 5:
        print("Você saiu do programa")
        break
    else:
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))

        print(ler_opcao_escolha_user(opcao, numero1, numero2))






    