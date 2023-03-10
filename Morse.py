import tkinter as tk  # para criar a janela
import re  # para limpar caracteres especiais
import winsound  # biblioteca do beep
import time  # usado para dar um tempo entre as letras
import keyboard as kb  # comando ESC para fechar a janela


# ---------------------------------------------------------------------------------------------------------------------
def limpar():  # limpa os inputs da janela
    morse_var.set('')
    txt_var.set('')


# ---------------------------------------------------------------------------------------------------------------------
def text_to_morse():

    if txt_var.get():
        a = ''  # variavel acumuladora
        string = re.sub(r"[^a-zA-Z0-9 Ç]", "", txt_var.get().upper())  # substitui caracteres especiais

        if string != '':  # limpa os caracteres especiais do input
            txt_var.set(string)  # recebe a string limpa de caracteres especiais no input

            lista = list(string)  # separa a string numa lista em maiusculo

            for item in lista:  # mapea a lista
                a += texto[item] + ' '  # acumula o resultado

            morse_var.set(a)  # mostra na tela

        else:
            txt_var.set('')


# ---------------------------------------------------------------------------------------------------------------------
def morse_to_text():

    if morse_var.get():
        a = ''  # variavel acumuladora
        string = re.sub(r"[^. /-]", "", morse_var.get())  # substitui caracteres especiais
        lista = string.split(' ')  # separa a string numa lista

        for item in lista:  # mapea a lista
            if item != '':  # foi usado esse IF para evitar erros
                try:
                    a += texto[item]  # acumula o resultado
                except Exception as e:
                    a += ' (' + str(e) + ' não encontrado) '  # caso código não seja encontrado no dicionário

        txt_var.set(a)  # mostra no input


# ---------------------------------------------------------------------------------------------------------------------
def som():

    for x in list(morse_var.get()):
        if x == '.':
            winsound.Beep(2500, 100)
        elif x == '-':
            winsound.Beep(2500, 400)
        else:
            time.sleep(.3)


# ---------------------------------------------------------------------------------------------------------------------
# dicionários com as informações, primeira parte texto → morse, segunda morse -> texto
texto = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
         'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
         'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
         '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
         '8': '---..', '9': '----.', '0': '-----', ' ': '/', 'Ç': '-.-.',
         # morse → texto
         '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I',
         '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
         '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',
         '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7',
         '---..': '8', '----.': '9', '-----': '0', '/': ' '}
# ---------------------------------------------------------------------------------------------------------------------
# criação e configuração da janela
janela = tk.Tk()
janela.resizable(width=False, height=False)
janela.title('Código Morse')
# tamanho: 325X250, posição: calula e posiciona
janela.geometry("%dx%d%d%d" % (325, 200, float(325 / 2 - janela.winfo_screenwidth() / 2),
                               float(200 / 2 - janela.winfo_screenheight() / 2)))
# ---------------------------------------------------------------------------------------------------------------------
url_texto = tk.Label(janela, text='Código Morse', font=('', 12))  # título da janela
url_texto.place(x=10, y=10)  # posição do objeto
# ---------------------------------------------------------------------------------------------------------------------
txt_txt = tk.Label(janela, text='Texto', font=('', 10))  # objeto do tkinter
txt_txt.place(x=10, y=42)  # posição do objeto
# ---------------------------------------------------------------------------------------------------------------------
txt_var = tk.StringVar()  # objeto string do tkinter
txt_in = tk.Entry(janela, textvariable=txt_var)  # celúla de entrada do tkinter
txt_in.place(x=60, y=44, width=250)  # posição do objeto
txt_in.focus()  # foca na celula no início do programa
# ---------------------------------------------------------------------------------------------------------------------
morse_txt = tk.Label(janela, text='Morse', font=('', 10))  # objeto do tkinter
morse_txt.place(x=10, y=72)  # posição do objeto
# ---------------------------------------------------------------------------------------------------------------------
morse_var = tk.StringVar()  # objeto string do tkinter
morse_in = tk.Entry(janela, textvariable=morse_var)  # celúla de entrada do tkinter
morse_in.place(x=60, y=74, width=250)  # posição do objeto
# ---------------------------------------------------------------------------------------------------------------------
con_txt_btn = tk.Button(janela, text='Limpar', command=lambda: limpar())
con_txt_btn.place(x=260, y=10, width=50)
# ---------------------------------------------------------------------------------------------------------------------
con_txt_btn = tk.Button(janela, text='Converter texto -> Morse', command=lambda: text_to_morse())
con_txt_btn.place(x=10, y=104, width=300)
# ---------------------------------------------------------------------------------------------------------------------
con_morse_btn = tk.Button(janela, text='Converter Morse -> Texto', command=lambda: morse_to_text())
con_morse_btn.place(x=10, y=134, width=300)
# ---------------------------------------------------------------------------------------------------------------------
ouvir_btn = tk.Button(janela, text='Ouvir', command=lambda: som())
ouvir_btn.place(x=10, y=164, width=300)
# ---------------------------------------------------------------------------------------------------------------------
kb.on_press_key('ESC', lambda _: janela.destroy())  # comando para fechar a janela
# ---------------------------------------------------------------------------------------------------------------------
janela.mainloop()  # mantem a janela aberta
