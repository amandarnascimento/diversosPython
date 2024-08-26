import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Excel para CSV")
        self.root.geometry("400x200")
        
        self.create_widgets()
        
    def create_widgets(self):
        # Botão para selecionar o arquivo Excel
        self.btn_select_file = tk.Button(self.root, text="Selecionar Arquivo Excel", command=self.select_file)
        self.btn_select_file.pack(pady=20)
        
        # Label para mostrar o caminho do arquivo selecionado
        self.lbl_file_path = tk.Label(self.root, text="")
        self.lbl_file_path.pack(pady=10)
        
        # Botão para executar a conversão
        self.btn_execute = tk.Button(self.root, text="Converter para CSV", command=self.convert_to_csv)
        self.btn_execute.pack(pady=20)
    
    def select_file(self):
        # Abrir diálogo para selecionar o arquivo Excel
        self.file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        self.lbl_file_path.config(text=self.file_path)
        
    def convert_to_csv(self):
        if hasattr(self, 'file_path') and self.file_path:
            try:
                # Ler o arquivo Excel e convertê-lo para CSV
                df = pd.read_excel(self.file_path)
                csv_file_path = self.file_path.replace(".xlsx", ".csv")
                df.to_csv(csv_file_path, index=False, encoding='utf-8-sig')
                messagebox.showinfo("Sucesso", f"Arquivo convertido com sucesso: {csv_file_path}")
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")
        else:
            messagebox.showwarning("Nenhum arquivo selecionado", "Por favor, selecione um arquivo Excel.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
