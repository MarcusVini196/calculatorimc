from tkinter import *


# ---- Cores ----
cor0 = '#ffffff' #---- Branca / White----
cor1 = '#444466' #---- Preta / Black----
cor2 = '#4065a1' #---- Azul / Blue----

janela = Tk()
janela.geometry('295x230')
janela.title('Calculadora IMC')
janela.configure(bg=cor0)


frame_cima = Frame(janela, width=295, height=50, bg=cor0, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)


frame_baixo = Frame(janela, width=295, height=50, bg=cor0, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

# ----  CONFIGURANDO FRAME CIMA ----
app_name = Label(frame_cima, text='Calculadora IMC', width=23, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 16 bold'),bg=cor0, fg=cor1)
app_name.place(x=0, y=0)

app_linha =Label(frame_cima, text='', width=400, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 1'), bg=cor2, fg=cor1)
app_linha.place(x=0, y=35)

# --------- Função Calcular ---------
def calcular():
    peso = float(e_peso.get())
    altura = float(e_altura.get())
    imc = peso / altura**2

    resultado = imc

    if resultado < 18.5:
        l_resultado_texto['text'] = 'O IMC é: Abaixo do Peso' 
        
    elif resultado >= 18.5 and resultado < 25:
        l_resultado_texto['text'] = 'O IMC: Normal'
        
    elif resultado >= 25 and resultado <30:
        l_resultado_texto['text'] = 'O IMC é: SobrePeso'
        
    else:
        l_resultado_texto['text'] = 'O IMC é: Obesidade'


    l_resultado['text'] = "{:.{}f}".format(resultado, 2)
  
# ----  CONFIGURANDO DO PESO ----

l_peso = Label(frame_baixo, text='Insira seu peso', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=cor0, fg=cor1)
l_peso.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)

e_peso = Entry(frame_baixo,width=5, relief='solid', font=('Ivy 10 bold'), justify='center')
e_peso.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3)

l_altura = Label(frame_baixo, text='Insira sua altura', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=cor0, fg=cor1)
l_altura.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)

e_altura = Entry(frame_baixo,width=5, relief='solid', font=('Ivy 10 bold'), justify='center')
e_altura.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)


l_resultado = Label(frame_baixo, text='---',width=5, height=1, padx=6,pady=12, relief='flat', anchor='center', font=('Ivy 24 bold'), bg=cor2, fg=cor0)
l_resultado.place(x=175, y=10)

l_resultado_texto = Label(frame_baixo, text='',width=37, height=1, padx=0,pady=12, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=cor0, fg=cor1)
l_resultado_texto.place(x=0, y=90)

b_calcular = Button(frame_baixo,command=calcular, text='Calcular',width=34, height=1,overrelief=SOLID, relief='raised', anchor='center', font=('Ivy 10 bold'), bg=cor2, fg=cor0)
b_calcular.grid(row=4, column=0, sticky=NSEW, pady=60, padx=5, columnspan=40)


janela.mainloop()