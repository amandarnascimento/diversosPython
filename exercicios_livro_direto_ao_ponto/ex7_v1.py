import random

numero_secreto = random.randint(1, 100)
tentativas_max = 5

for tentativa in range(1, tentativas_max + 1):
    try:
        palpite = int(input(f"Tentativa {tentativa}: Qual é o seu palpite? "))

        if palpite == numero_secreto:
            print(f"Aeeee, voce acertou! ")
            break
        elif palpite < numero_secreto:
            print("O número é maior! ")
        else:
            print("O número é menor!")
    except ValueError:
        print("Entrada inválida, digite novamente ")
        continue

else: 
    print(f"\nVocê atingiu o limite de tentativas! O número secreto era {numero_secreto}.")


    