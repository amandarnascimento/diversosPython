import pyttsx3

empresas = ('Cometa', 'Gontijo', 'Itapemirim', 'Buser')

def contarNum(numero):
    return len(numero)

def numero_texto(numero):
    numero = int(numero)
    if numero < 20:
        return dicionarioNextensos[numero]
    elif numero < 100:
        dezena, unidade = divmod(numero, 10)
        if unidade == 0:
            return dicionarioNextensos[dezena * 10]
        else:
            return f"{dicionarioNextensos[dezena * 10]} e {dicionarioNextensos[unidade]}"
    elif numero < 1000:
        centena, resto = divmod(numero, 100)
        if resto == 0:
            return dicionarioNextensos[centena * 100]
        else:
            return f"{dicionarioNextensos[centena * 100]} e {numero_texto(resto)}"
    else:
        milhar, resto = divmod(numero, 1000)
        if resto == 0:
            return f"{numero_texto(milhar)} mil"
        else:
            return f"{numero_texto(milhar)} mil e {numero_texto(resto)}"

def chamada(numero_carro, empresa):
    if 3 <= contarNum(numero_carro) <= 5:
        numero_extenso = numero_texto(numero_carro)
        return f"Atenção passageiros, o carro de número {numero_extenso} da empresa {empresa} sairá da plataforma em breve."
    else:
        return "Número do carro inválido. O número deve ter entre 3 a 5 dígitos."

def main():
    numero_carro = input("Digite o número do carro: ")
    
    print("Selecione a empresa:")
    for i, empresa in enumerate(empresas, 1):
        print(f"{i} - {empresa}")
    
    opcao_empresa = int(input("Digite o número correspondente à empresa: "))
    if 1 <= opcao_empresa <= len(empresas):
        empresa_escolhida = empresas[opcao_empresa - 1]
    else:
        print("Opção inválida. Tente novamente.")
        return
    
    mensagem = chamada(numero_carro, empresa_escolhida)
    print(mensagem)
    
    engine = pyttsx3.init()
    engine.say(mensagem)
    engine.runAndWait()

dicionarioNextensos = {
    0: "zero", 1: "um", 2: "dois", 3: "três", 4: "quatro", 5: "cinco",
    6: "seis", 7: "sete", 8: "oito", 9: "nove", 10: "dez", 11: "onze",
    12: "doze", 13: "treze", 14: "quatorze", 15: "quinze", 16: "dezesseis",
    17: "dezessete", 18: "dezoito", 19: "dezenove", 20: "vinte", 30: "trinta",
    40: "quarenta", 50: "cinquenta", 60: "sessenta", 70: "setenta", 80: "oitenta",
    90: "noventa", 100: "cem", 200: "duzentos", 300: "trezentos", 400: "quatrocentos",
    500: "quinhentos", 600: "seiscentos", 700: "setecentos", 800: "oitocentos",
    900: "novecentos"
}

if __name__ == "__main__":
    main()
