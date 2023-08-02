import pandas as pd
import os
import tkinter as tk
from tkinter import messagebox

# Caminho para o arquivo Excel de origem
arquivo_excel = 'Coloque aqui a pasta onde esta pasta do arquivo em xlsx'

# Caminho para a pasta onde será salvo o arquivo CSV
pasta_destino = 'Coloque aqui a pasta de destino'

# Define o caminho completo e nome do novo arquivo CSV
nome_arquivo_csv = os.path.join(pasta_destino, 'novo_arquivo.csv')

# Verifica se o arquivo 'novo_arquivo.csv' já existe
if os.path.exists(nome_arquivo_csv):
    # Remove o arquivo existente
    os.remove(nome_arquivo_csv)

# Carrega o arquivo Excel usando o Pandas
df = pd.read_excel(arquivo_excel)

# Salva o DataFrame em formato CSV
df.to_csv(nome_arquivo_csv, index=False)

# Exibe uma notificação pop-up informando que o processo foi executado com sucesso
root = tk.Tk()
root.withdraw()  # Oculta a janela principal do tkinter
messagebox.showinfo("Sucesso", "O processo foi executado com sucesso!")
root.destroy()

print("Arquivo convertido com sucesso!")



