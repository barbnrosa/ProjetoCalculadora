#importando tkinter
from tkinter import *
from tkinter import ttk

# importando a biblioteca math~
import math

#cores
cor1 = "#41001d"  # vinho
cor2 = "#ffdce4"  # rosa clarinho
cor3 = "#e891b0"  # rosa médio
cor4 ="#c627c5"   # rosa
cor5 = "#8f4f62" # vinho claro

#criando janela principal
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x290")
janela.config(bg=cor1)

#criando frames
frame_tela = Frame(janela, width=300, height=56, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_cientifica = Frame(janela, width=300, height=86)
frame_cientifica.grid(row=1, column=0)

frame_corpo = Frame(janela, width=300, height=340)
frame_corpo.grid(row=2, column=0)

# parte operacional/ funções

global todos_valores

todos_valores = ''    # isso porque quero que na tela seja apresentado uma string vazia
texto = StringVar()

#função entrar valores na tela
def entrar_valores(evento):
    global todos_valores

    todos_valores = todos_valores + str(evento)   # isso para que os valores sejam reservados dentro dele mesmo e os valores que entrarem serão adicionados com valores que entrarão na calculadora
    texto.set(todos_valores)

# função calcular
def calcular():
    global todos_valores
   
    modulos =['math.tan', 'math.sin', 'math.cos', 'math.sqrt', 'math.log', 'math.log10', 'math.e', 'math.pow', 'math.pi']

    for i in modulos:
        if i=='math.tan':
            todos_valores = todos_valores.replace('tan', i)
        if i=='math.sin':
            todos_valores = todos_valores.replace('sin', i)
        if i=='math.cos':
            todos_valores = todos_valores.replace('cos', i)
        if i=='math.sqrt':
            todos_valores = todos_valores.replace('sqrt', i)

        # -----------------------------------------------

        if i=='math.log':
            todos_valores = todos_valores.replace('log', i)
        if i=='math.log10':
            todos_valores = todos_valores.replace('log10', i)
        if i=='math.e':
            todos_valores = todos_valores.replace('e', i)
        if i=='math.pow':
            todos_valores = todos_valores.replace('pow', i)

        # -----------------------------------------------
        if i=='math.pi':
            todos_valores = todos_valores.replace('pi', i)  


        resultado = str(eval(todos_valores))
        texto.set(resultado)

        todos_valores = ''

#função limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ''
    texto.set("")


# configurando o frame tela
label_tela = Label(frame_tela, textvariable=texto, width=16, height=2,  padx=7, anchor='e', bd=0, justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
label_tela.place(x=0, y=0)

# configurando o frame científico
b_0 = Button(frame_cientifica, command=lambda:entrar_valores('tan'), text='tan', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=0)
b_1 = Button(frame_cientifica, command=lambda:entrar_valores('sin'), text='sin', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=60, y=0)
b_2 = Button(frame_cientifica, command=lambda:entrar_valores('cos'), text='cos', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_2.place(x=120 , y=0)
b_3 = Button(frame_cientifica, command=lambda:entrar_valores('sqrt'), text='sqrt', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_3.place(x=180, y=0)

b_0 = Button(frame_cientifica, command=lambda:entrar_valores('log'), text='log', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=30)
b_1 = Button(frame_cientifica, command=lambda:entrar_valores('log10'), text='log10', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=60, y=30)
b_2 = Button(frame_cientifica, command=lambda:entrar_valores('e'), text='e', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_2.place(x=120, y=30)
b_3 = Button(frame_cientifica, command=lambda:entrar_valores('pow'), text='pow', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_3.place(x=180, y=30)

b_0 = Button(frame_cientifica, command=lambda:entrar_valores('pi'), text='pi', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=60)
b_1 = Button(frame_cientifica, command=lambda:entrar_valores(','), text=',', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=60, y=60)
b_2 = Button(frame_cientifica, command=lambda:entrar_valores('('), text='(', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_2.place(x=120, y=60)
b_3 = Button(frame_cientifica, command=lambda:entrar_valores(')'), text=')', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_3.place(x=180, y=60)

#frame corpo

b_0 = Button(frame_corpo, command=limpar_tela, text='c', width=14, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor5, fg=cor2)
b_0.place(x=0, y=0)
b_1 = Button(frame_corpo, command=lambda:entrar_valores('%'), text='%', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor5, fg=cor2)
b_1.place(x=120, y=0)
b_2 = Button(frame_corpo, command=lambda:entrar_valores('/'), text='/', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor5, fg=cor2)
b_2.place(x=180, y=0)

b_0 = Button(frame_corpo, command=lambda:entrar_valores('7'), text='7', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=30)
b_1 = Button(frame_corpo, command=lambda:entrar_valores('8'), text='8', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=60, y=30)
b_2 = Button(frame_corpo, command=lambda:entrar_valores('9'), text='9', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_2.place(x=120, y=30)
b_3 = Button(frame_corpo, command=lambda:entrar_valores('*'), text='*', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor5, fg=cor2)
b_3.place(x=180, y=30)

b_0 = Button(frame_corpo, command=lambda:entrar_valores('4'), text='4', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=60)
b_1 = Button(frame_corpo, command=lambda:entrar_valores('5'), text='5', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=60, y=60)
b_2 = Button(frame_corpo, command=lambda:entrar_valores('6'), text='6', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_2.place(x=120, y=60)
b_3 = Button(frame_corpo, command=lambda:entrar_valores('-'), text='-', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor5, fg=cor2)
b_3.place(x=180, y=60)

b_0 = Button(frame_corpo, command=lambda:entrar_valores('1'), text='1', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=90)
b_1 = Button(frame_corpo, command=lambda:entrar_valores('2'), text='2', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=60, y=90)
b_2 = Button(frame_corpo, command=lambda:entrar_valores('3'), text='3', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_2.place(x=120, y=90)
b_3 = Button(frame_corpo, command=lambda:entrar_valores('+'), text='+', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor5, fg=cor2)
b_3.place(x=180, y=90)

b_0 = Button(frame_corpo, command=lambda:entrar_valores('0'), text='0', width=14, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=120)
b_1 = Button(frame_corpo, command=lambda:entrar_valores('.'), text='.', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=120, y=120)
b_2 = Button(frame_corpo, command=calcular, text='=', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor5, fg=cor2)
b_2.place(x=180, y=120)


janela.mainloop()