#importando tkinter
from tkinter import *
from tkinter import ttk

#cores
cor1 = "#363434"  # black/preta
cor2 = "#feffff"  # white/branca
cor3 = "#37474F"  # black/preta
cor4 ="#424345"   # orange

#criando janela principal
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x289")
janela.config(bg=cor1)

#criando frames
frame_tela = Frame(janela, width=300, height=56, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_cientifica = Frame(janela, width=300, height=86)
frame_cientifica.grid(row=1, column=0)

frame_corpo = Frame(janela, width=300, height=340)
frame_corpo.grid(row=2, column=0)

# configurando o frame tela
label_tela = Label(janela, width=16, height=2, text='123456789', padx=7, anchor='e', bd=0, justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
frame_tela.place(x=0, y=0)

janela.mainloop()