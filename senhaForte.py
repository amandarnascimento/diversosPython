def verifica_senha(senha):
    conta_caract = len(senha)
    conta_num = 0
    conta_letras = 0
    conta_pontuacoes = 0

    numeros = '0123456789'
    pontuacoes = ',.!?;:^'

    for caract in senha:
        if caract in numeros:
            conta_num += 1
        elif caract.isalpha():
            conta_letras += 1
        elif caract in pontuacoes:
            conta_pontuacoes += 1

    if conta_caract <= 5:
        return 'Senha fraca'
    elif conta_letras > 0 and conta_num > 0 and conta_pontuacoes == 0:
        return 'Senha Forte'
    elif conta_letras > 0 and conta_num > 0 and conta_pontuacoes > 0:
        return 'Senha Muito Forte'
    else:
        return 'Senha inválida'  
    
senha = input("Digite sua senha:")
resultado = verifica_senha(senha)
print(resultado)
