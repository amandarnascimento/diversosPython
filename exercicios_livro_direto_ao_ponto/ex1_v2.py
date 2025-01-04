
def classificacao(idade):
    if idade <= 12:
        print("criança")
    elif idade >=13 and idade <= 19:
        print("adolescente")
    else:
        print("idoso")


idadeusuario = int(input("Digite a idade do usuário: "))

classificacao(idadeusuario)