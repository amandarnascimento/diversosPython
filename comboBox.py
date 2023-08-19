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
janela.title("Dias da semana")

#3
#Criando a lista
dias_semana = [
    "Domingo",
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sábado",
]

#Criando combobox
Combobox = ttk.Combobox(janela, values=dias_semana)
#randerizar o combobox com algum método:
Combobox.pack(padx=75, pady=20)


#Rodando a janela
#2
janela.mainloop()