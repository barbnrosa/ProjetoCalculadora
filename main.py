#importando tkinter
from tkinter import *
from tkinter import ttk

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

# configurando o frame tela
label_tela = Label(frame_tela, text='123456789', width=16, height=2,  padx=7, anchor='e', bd=0, justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
label_tela.place(x=0, y=0)

# configurando o frame científico
b_0 = Button(frame_cientifica, text='tan', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=0)
b_1 = Button(frame_cientifica, text='sin', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=60, y=0)
b_2 = Button(frame_cientifica, text='cos', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_2.place(x=120 , y=0)
b_3 = Button(frame_cientifica, text='sqrt', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_3.place(x=180, y=0)

b_0 = Button(frame_cientifica, text='log', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=30)
b_1 = Button(frame_cientifica, text='log10', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=60, y=30)
b_2 = Button(frame_cientifica, text='e', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_2.place(x=120, y=30)
b_3 = Button(frame_cientifica, text='pow', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_3.place(x=180, y=30)

b_0 = Button(frame_cientifica, text='pi', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=60)
b_1 = Button(frame_cientifica, text=',', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=60, y=60)
b_2 = Button(frame_cientifica, text='(', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_2.place(x=120, y=60)
b_3 = Button(frame_cientifica, text=')', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_3.place(x=180, y=60)

#frame corpo

b_0 = Button(frame_corpo, text='c', width=14, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor5, fg=cor2)
b_0.place(x=0, y=0)
b_1 = Button(frame_corpo, text='%', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor5, fg=cor2)
b_1.place(x=120, y=0)
b_2 = Button(frame_corpo, text='/', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor5, fg=cor2)
b_2.place(x=180, y=0)

b_0 = Button(frame_corpo, text='7', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=30)
b_1 = Button(frame_corpo, text='8', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=60, y=30)
b_2 = Button(frame_corpo, text='9', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_2.place(x=120, y=30)
b_3 = Button(frame_corpo, text='*', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor5, fg=cor2)
b_3.place(x=180, y=30)

b_0 = Button(frame_corpo, text='4', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=60)
b_1 = Button(frame_corpo, text='5', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=60, y=60)
b_2 = Button(frame_corpo, text='6', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_2.place(x=120, y=60)
b_3 = Button(frame_corpo, text='-', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor5, fg=cor2)
b_3.place(x=180, y=60)

b_0 = Button(frame_corpo, text='1', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=90)
b_1 = Button(frame_corpo, text='2', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=60, y=90)
b_2 = Button(frame_corpo, text='3', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_2.place(x=120, y=90)
b_3 = Button(frame_corpo, text='+', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor5, fg=cor2)
b_3.place(x=180, y=90)

b_0 = Button(frame_corpo, text='0', width=14, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=120)
b_1 = Button(frame_corpo, text='.', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=120, y=120)
b_2 = Button(frame_corpo, text='=', width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor5, fg=cor2)
b_2.place(x=180, y=120)


janela.mainloop()