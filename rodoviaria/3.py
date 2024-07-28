import pyttsx3
import tkinter as tk
from tkinter import ttk, messagebox

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

def executar_chamada():
    numero_carro = numero_carro_entry.get()
    empresa_idx = empresa_combobox.current()
    
    if empresa_idx == -1:
        messagebox.showerror("Erro", "Selecione uma empresa válida.")
        return
    
    if not numero_carro.isdigit() or not (3 <= contarNum(numero_carro) <= 5):
        messagebox.showerror("Erro", "Digite um número de carro válido (3 a 5 dígitos).")
        return

    empresa_escolhida = empresas[empresa_idx]
    mensagem = chamada(numero_carro, empresa_escolhida)
    
    engine = pyttsx3.init()
    engine.say(mensagem)
    engine.runAndWait()

app = tk.Tk()
app.title("Chamada de Passageiros")
app.geometry("400x300")
app.configure(bg="#f0f8ff")

titulo_label = tk.Label(app, text="Chamada de Passageiros", font=("Helvetica", 16), bg="#f0f8ff")
titulo_label.pack(pady=10)

numero_carro_label = tk.Label(app, text="Número do carro:", font=("Helvetica", 12), bg="#f0f8ff")
numero_carro_label.pack(pady=5)
numero_carro_entry = tk.Entry(app, font=("Helvetica", 12))
numero_carro_entry.pack(pady=5)

empresa_label = tk.Label(app, text="Selecione a empresa:", font=("Helvetica", 12), bg="#f0f8ff")
empresa_label.pack(pady=5)
empresa_combobox = ttk.Combobox(app, values=empresas, font=("Helvetica", 12))
empresa_combobox.pack(pady=5)

play_button = tk.Button(app, text="Play", command=executar_chamada, font=("Helvetica", 12), bg="#007fff", fg="white")
play_button.pack(pady=20)

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

app.mainloop()
