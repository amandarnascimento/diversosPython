#Importanto o yyk do Tkinter
#from tkinter import ttk as tk

from tkinter import ttk

# Substituindo as ferramentas nativas do tkinter por ferramentas
# melhores, mais modernas
from tkinter import *
from tkinter.ttk import *


# Criando a janela
#1
janela = Tk()
janela.title("Exemplo de notebook")

#3
notebook = ttk.Notebook(janela)

#Primeira guia
guia1 = ttk.Frame(notebook)
notebook.add(guia1, text="Guia 1")

label1 = ttk.Label(guia1, text="Conteúdo guia 1")
label1.pack(padx=10, pady=10)


#Segunda guia
guia2 = ttk.Frame(notebook)
notebook.add(guia2, text="Guia 2")

label2 = ttk.Label(guia2, text="Conteúdo guia 2")
label2.pack(padx=10, pady=10)


#Terceira guia
guia3 = ttk.Frame(notebook)
notebook.add(guia3, text="Guia 3")

label3 = ttk.Label(guia3, text="Conteúdo guia 3")
label3.pack(padx=10, pady=10)


#Posicionando Notebook
notebook.pack(padx=30, pady=50)


#Rodando a janela
#2
janela.mainloop()