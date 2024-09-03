import tkinter as tk
from tkinter import filedialog, messagebox
import os
import pandas as pd

def verificar_planilhas_e_empilhar(pasta, nome_arquivo, ignorar_tipos=False):
    # Procurar todos os arquivos .xlsx na pasta selecionada
    arquivos_xlsx = [os.path.join(pasta, f) for f in os.listdir(pasta) if f.endswith('.xlsx')]
    
    if not arquivos_xlsx:
        messagebox.showerror("Erro", "Nenhum arquivo .xlsx encontrado na pasta selecionada.")
        return
    
    # Inicializar variáveis para verificar consistência das planilhas
    colunas_referencia = None
    tipos_referencia = None
    planilhas_validas = []
    erros = []
    
    for arquivo in arquivos_xlsx:
        try:
            df = pd.read_excel(arquivo)
            colunas_atual = df.columns
            tipos_atual = df.dtypes
            
            # Se for a primeira planilha, definir as colunas e tipos de referência
            if colunas_referencia is None:
                colunas_referencia = colunas_atual
                tipos_referencia = tipos_atual
            else:
                # Verificar se as colunas coincidem com a referência
                if not colunas_atual.equals(colunas_referencia):
                    erros.append(f"'{os.path.basename(arquivo)}' tem colunas diferentes.\nEsperado: {list(colunas_referencia)}\nEncontrado: {list(colunas_atual)}\n")
                    continue
                
                # Verificar se os tipos coincidem com a referência, a menos que ignorar_tipos seja True
                if not ignorar_tipos and not tipos_atual.equals(tipos_referencia):
                    tipos_diferentes = [(coluna, tipos_referencia[coluna], tipos_atual[coluna]) 
                                        for coluna in colunas_atual 
                                        if tipos_referencia[coluna] != tipos_atual[coluna]]
                    erro_tipos = "\n".join([f"Coluna '{coluna}': esperado {tipo_ref}, encontrado {tipo_atual}" 
                                            for coluna, tipo_ref, tipo_atual in tipos_diferentes])
                    erros.append(f"'{os.path.basename(arquivo)}' tem tipos de dados diferentes:\n{erro_tipos}\n")
                    continue
            
            planilhas_validas.append(df)
        except Exception as e:
            erros.append(f"Erro ao processar o arquivo '{os.path.basename(arquivo)}': {str(e)}")
            continue
    
    # Exibir erros, se houver
    if erros:
        if not ignorar_tipos:
            msg = "\n\n".join(erros) + "\n\nDeseja empilhar as planilhas mesmo assim?"
            if messagebox.askyesno("Inconsistências Encontradas", msg):
                verificar_planilhas_e_empilhar(pasta, nome_arquivo, ignorar_tipos=True)
            else:
                return
        else:
            messagebox.showerror("Inconsistências Encontradas", "\n\n".join(erros))
            return
    
    # Empilhar as planilhas se não houver erros ou se o usuário optar por ignorá-los
    df_final = pd.concat(planilhas_validas, ignore_index=True)
    
    # Salvar o arquivo empilhado
    caminho_arquivo = os.path.join(pasta, f"{nome_arquivo}.xlsx")
    df_final.to_excel(caminho_arquivo, index=False)
    
    messagebox.showinfo("Sucesso", f"Planilhas empilhadas com sucesso! Arquivo salvo em: {caminho_arquivo}")

def selecionar_pasta():
    pasta_selecionada = filedialog.askdirectory()
    if pasta_selecionada:
        entrada_pasta.delete(0, tk.END)
        entrada_pasta.insert(0, pasta_selecionada)

def executar_empilhamento():
    pasta = entrada_pasta.get()
    nome_arquivo = entrada_nome_arquivo.get()
    
    if not pasta or not nome_arquivo:
        messagebox.showerror("Erro", "Por favor, selecione uma pasta e insira o nome do arquivo.")
        return
    
    verificar_planilhas_e_empilhar(pasta, nome_arquivo)

# Interface com Tkinter
janela = tk.Tk()
janela.title("Empilhador de Planilhas Excel")

# Campo para selecionar a pasta
tk.Label(janela, text="Selecione a pasta:").grid(row=0, column=0, padx=10, pady=5)
entrada_pasta = tk.Entry(janela, width=50)
entrada_pasta.grid(row=0, column=1, padx=10, pady=5)
botao_selecionar_pasta = tk.Button(janela, text="Selecionar", command=selecionar_pasta)
botao_selecionar_pasta.grid(row=0, column=2, padx=10, pady=5)

# Campo para inserir o nome do arquivo final
tk.Label(janela, text="Nome do arquivo final:").grid(row=1, column=0, padx=10, pady=5)
entrada_nome_arquivo = tk.Entry(janela, width=50)
entrada_nome_arquivo.grid(row=1, column=1, padx=10, pady=5)

# Botão para executar o empilhamento
botao_executar = tk.Button(janela, text="Executar", command=executar_empilhamento)
botao_executar.grid(row=2, column=1, padx=10, pady=20)

janela.mainloop()
