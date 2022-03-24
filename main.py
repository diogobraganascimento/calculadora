from tkinter import *
from tkinter import ttk
from conf import *


# Cores
preto = "#1e1f1e"
branco = "#feffff"
azul = "#38576b"
cinza = "#ECEFF1"
laranja = "#FF7F00"

# Funções
def entrar_valores(event):
    global todos_valores

    todos_valores = todos_valores + str(event)

    valor_texto.set(todos_valores)


def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    todos_valores = str(resultado)
    valor_texto.set(str(resultado))


def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

janela = Tk()

# Criação da janela (titulo/tamanho/fundo)
janela.title("Calculadora")
janela.geometry("320x330")
janela.config(bg=preto)

# Criação do mostrador
frame_display = Frame(janela, width=320, height=70, bg=azul)
frame_display.grid(row=0, column=0)

# Criação do corpo
frame_corpo = Frame(janela, width=320, height=260)
frame_corpo.grid(row=1, column=0)

todos_valores = ''
valor_texto = StringVar()

# Criando label
app_label = Label(frame_display, textvariable=valor_texto, width=21, height=3, padx=15, relief=FLAT, anchor="e", justify=RIGHT, font='Ivy 18', bg=azul, fg=branco)
app_label.place(x=0, y=0)

# Criar os botões
# Primeira linha (limpar / percentual / divisão)
limpar = Button(frame_corpo, text="C", width=15, height=2, bg=cinza, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=limpar_tela)
limpar.place(x=0, y=0)

percentual = Button(frame_corpo, text="%", width=7, height=2, bg=cinza, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores("%"))
percentual.place(x=160, y=0)

dividir = Button(frame_corpo, text="/", width=7, height=2, bg=laranja, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores("/"))
dividir.place(x=240, y=0)

# Segunda linha (7 / 8 / 9 / multiplicar)
sete = Button(frame_corpo, text="7", width=7, height=2, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores("7"))
sete.place(x=0, y=52)

oito = Button(frame_corpo, text="8", width=7, height=2, fg=preto, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores("8"))
oito.place(x=80, y=52)

nove = Button(frame_corpo, text="9", width=7, height=2, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores("9"))
nove.place(x=160, y=52)

multiplicar = Button(frame_corpo, text="*", width=7, height=2, fg=preto, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores("*"))
multiplicar.place(x=240, y=52)

# Terceira linha (4 / 5 / 6 / subtrair)
quatro = Button(frame_corpo, text="4", width=7, height=2, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores("4"))
quatro.place(x=0, y=104)

cinco = Button(frame_corpo, text="5", width=7, height=2, fg=preto, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores("5"))
cinco.place(x=80, y=104)

seis = Button(frame_corpo, text="6", width=7, height=2, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores("6"))
seis.place(x=160, y=104)

subtrair = Button(frame_corpo, text="-", width=7, height=2, fg=preto, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores("-"))
subtrair.place(x=240, y=104)

# Quarta linha (1 / 2 / 3 / soma)
um = Button(frame_corpo, text="1", width=7, height=2, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores("1"))
um.place(x=0, y=156)

dois = Button(frame_corpo, text="2", width=7, height=2, fg=preto, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores("2"))
dois.place(x=80, y=156)

tres = Button(frame_corpo, text="3", width=7, height=2, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores("3"))
tres.place(x=160, y=156)

somar = Button(frame_corpo, text="+", width=7, height=2, fg=preto, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores("+"))
somar.place(x=240, y=156)

# Quinta linha (0 / . / resultado)
zero = Button(frame_corpo, text="0", width=15, height=2, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores("0"))
zero.place(x=0, y=208)

ponto = Button(frame_corpo, text=".", width=7, height=2, fg=preto, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores("."))
ponto.place(x=160, y=208)

resultado = Button(frame_corpo, text="=", width=7, height=2, fg=preto, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE, command=calcular)
resultado.place(x=240, y=208)

janela.mainloop()
