import os
import tkinter as tk
from tkinter import filedialog, messagebox
from docx2pdf import convert

def selecionar_pasta():
    pasta_selecionada = filedialog.askdirectory()
    if pasta_selecionada:
        caminho_pasta.set(pasta_selecionada)

def gerar_pdfs():
    pasta = caminho_pasta.get()
    if not pasta:
        messagebox.showerror("Erro", "Nenhuma pasta selecionada.")
        return

    pasta_saida = os.path.join(pasta, "PDFs criados")
    os.makedirs(pasta_saida, exist_ok=True)

    arquivos_word = [f for f in os.listdir(pasta) if f.endswith('.docx')]
    if not arquivos_word:
        messagebox.showinfo("Informação", "Nenhum arquivo Word encontrado na pasta selecionada.")
        return

    for arquivo_word in arquivos_word:
        caminho_arquivo_word = os.path.join(pasta, arquivo_word)
        caminho_arquivo_saida = os.path.join(pasta_saida, f"{os.path.splitext(arquivo_word)[0]}.pdf")
        convert(caminho_arquivo_word, caminho_arquivo_saida)

    messagebox.showinfo("Sucesso", f"{len(arquivos_word)} arquivos foram convertidos em PDF.")

app = tk.Tk()
app.title("Gerar PDF")

caminho_pasta = tk.StringVar()

tk.Label(app, text="Selecione a pasta:").pack(pady=10)
tk.Entry(app, textvariable=caminho_pasta, width=50).pack(padx=10)
tk.Button(app, text="Selecionar Pasta", command=selecionar_pasta).pack(pady=10)
tk.Button(app, text="Gerar PDFs", command=gerar_pdfs).pack(pady=10)

app.mainloop()
