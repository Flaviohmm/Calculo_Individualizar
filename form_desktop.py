import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

entry_saldo_fgts = None
entry_meses_trabalhados = None
entry_divida_pgfn = None
entry_meses_em_divida = None
result_label = None


def calcular_individualizacao():
    saldo_fgts = float(entry_saldo_fgts.get())
    meses_trabalhados = int(entry_meses_trabalhados.get())
    divida_pgfn = float(entry_divida_pgfn.get())
    meses_em_divida = int(entry_meses_em_divida.get())

    individualizacao_fgts = saldo_fgts / meses_trabalhados
    individualizacao_pgfn = divida_pgfn / meses_em_divida

    result_label.config(text=f'Individualização FGTS: {individualizacao_fgts:.2f}\nIndividualização PGFN: {individualizacao_pgfn:.2f}')


# Criando a janela principal com estilo do Bootstrap
root = tk.Tk()
root.title("Informe os Dados")
style = Style(theme='cosmo') # Escolha um tema do Bootstrap

# Aumentando o tamanho da janela
root.geometry("400x480") # largura x altura

# Adicionando classes do Bootstrap aos widgets
root.option_add('*TCombobox*Listbox*Background', 'white')
root.option_add('*TEntry*FieldBackground', 'white')

tk.ttk.Style().configure('TButton', padding=6, relief='flat', background='#007bff', foreground='white')

# Criando os widgets
label_saldo_fgts = tk.Label(root, text="Saldo FGTS:", font=("Calibri", 12))
label_saldo_fgts.pack(pady=5)
entry_saldo_fgts = tk.Entry(root, font=("Calibri", 12))
entry_saldo_fgts.pack(pady=10)

label_meses_trabalhados = tk.Label(root, text="Meses Trabalhados:", font=("Calibri", 12))
label_meses_trabalhados.pack(pady=5)
entry_meses_trabalhados = tk.Entry(root, font=("Calibri", 12))
entry_meses_trabalhados.pack(pady=10)

label_divida_pgfn = tk.Label(root, text="Dívida PGFN:", font=("Calibri", 12))
label_divida_pgfn.pack(pady=5)
entry_divida_pgfn = tk.Entry(root, font=("Calibri", 12))
entry_divida_pgfn.pack(pady=10)

label_meses_em_divida = tk.Label(root, text="Meses em Dívida:", font=("Calibri", 12))
label_meses_em_divida.pack(pady=5)
entry_meses_em_divida = tk.Entry(root, font=("Calibri", 12))
entry_meses_em_divida.pack(pady=15)

btn_calcular = tk.Button(root, text="Calcular Individualização", command=calcular_individualizacao, font=("Calibri", 12))
btn_calcular.pack(pady=15)

result_label = tk.Label(root, text="", font=("Calibri", 12))
result_label.pack()

root.mainloop()