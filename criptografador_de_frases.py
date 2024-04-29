import tkinter as tk
from tkinter import messagebox

def criptografar_frase(frase):
    substituicao = {
        'a': 'U', 'b': 'S', 'c': 'M', 'd': 'Q', 'e': 'Z',
        'f': 'L', 'g': 'U', 'h': '-', 'i': 'C', 'j': 'U',
        'k': 'V', 'l': 'C', 'm': 'U', 'n': 'G', 'o': 'D',
        'p': '-', 'q': 'S', 'r': 'Q', 's': 'G', 't': 'Z',
        'u': 'U', 'v': '-','w': '-', 'x': '-', 'y': '-',
        'z': 'U', ' ': ' '
    }

    def trocar_letra(char):
        return substituicao.get(char.lower(), char)

    frase_criptografada = ''.join(trocar_letra(char) for char in frase)

    return frase_criptografada

def obter_frase():
    frase_digitada = entrada_frase.get()
    if frase_digitada.strip() == "":
        messagebox.showwarning("Aviso", "Por favor, digite uma frase.")
        return
    frase_criptografada = criptografar_frase(frase_digitada)
    messagebox.showinfo("Frase Criptografada", "Frase criptografada: " + frase_criptografada)

janela = tk.Tk()
janela.title("Criptografador de Frases")

frame = tk.Frame(janela)
frame.pack(padx=20, pady=20)

texto_instrucao = tk.Label(frame, text="Digite uma frase para criptografar:")
texto_instrucao.pack(padx=5, pady=5)

entrada_frase = tk.Entry(frame, width=40)
entrada_frase.pack(padx=5, pady=5)

botao_criptografar = tk.Button(frame, text="Criptografar", command=obter_frase)
botao_criptografar.pack(pady=5)

janela.mainloop()
