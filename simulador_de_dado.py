import random

def desenhar_dado(valor):
    faces = {
        1: (
            "+-------+\n"
            "|       |\n"
            "|   o   |\n"
            "|       |\n"
            "+-------+"
        ),
        2: (
            "+-------+\n"
            "| o     |\n"
            "|       |\n"
            "|     o |\n"
            "+-------+"
        ),
        3: (
            "+-------+\n"
            "| o     |\n"
            "|   o   |\n"
            "|     o |\n"
            "+-------+"
        ),
        4: (
            "+-------+\n"
            "| o   o |\n"
            "|       |\n"
            "| o   o |\n"
            "+-------+"
        ),
        5: (
            "+-------+\n"
            "| o   o |\n"
            "|   o   |\n"
            "| o   o |\n"
            "+-------+"
        ),
        6: (
            "+-------+\n"
            "| o   o |\n"
            "| o   o |\n"
            "| o   o |\n"
            "+-------+"
        ),
    }
    print(faces[valor])

def rolar_dado():
    valor = random.randint(1, 6)
    print(f"Você jogou um {valor}!\n")
    desenhar_dado(valor)

if __name__ == "__main__":
    while True:
        entrada = input("Pressione Enter para jogar o dado (ou digite 'sair' para finalizar): ").strip().lower()
        if entrada == "sair":
            print("Obrigado por jogar! Até a próxima :)")
            break
        rolar_dado()