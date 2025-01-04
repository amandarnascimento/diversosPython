
def classificacao_idade(idade):
    if idade <= 12:
        print("Criança")
    elif idade > 12 and idade <= 19:
        print("adolescente")
    elif idade > 19 and idade <= 64:
        print("adulto")
    else:
        print("idoso")


idadepessoa = int(input("Digite a idade: "))


#classificacao_idade = idadepessoa
#usar a função sem sobrescrever seu nome
classificacao_idade(idadepessoa)