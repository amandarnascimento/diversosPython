import tkinter as tk

def press_key(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(key))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Erro")

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora")

# Entrada de texto para exibir números e resultados
entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botões
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('/', 4, 3),
    ('=', 5, 0)
]

for button in buttons:
    text, row, column = button
    tk.Button(root, text=text, padx=20, pady=10, command=lambda t=text: press_key(t) if t != "=" else calculate()).grid(row=row, column=column)

root.mainloop()
