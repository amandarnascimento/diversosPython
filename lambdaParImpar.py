# numero par ou impar
## lambda comando do python que permite escrever a funcao em uma linha
#a stirng já é entendida como uma lista

par = lambda string : True if string[-1] in "02468" else False
print(par("10"))

#impar = lambda string : True if string[0] == '-' else False
#print(par("10"))

#numero = input("Digite um número: ")
#print(f"O número {numero} é par." if par(numero) else f"o número {numero} é impar.") 
