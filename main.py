from tkinter import *
from tkinter import ttk

# Cores
preto = "#1e1f1e"
branco = "#feffff"
azul = "#38576b"
cinza = "#ECEFF1"
laranja = "#FF7F00"

janela = Tk()

# Criação da janela (titulo/tamanho/conf/etc)
janela.title("Calculadora")
janela.geometry("252x287")
janela.config(bg=preto)

# Criação do mostrador
frame_display = Frame(janela, width=252, height=52, bg=azul)
frame_display.grid(row=0, column=0)

# Criação do corpo
frame_corpo = Frame(janela, width=252, height=240)
frame_corpo.grid(row=1, column=0)

todos_valores = ''
valor_texto = StringVar()


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


# Criando label
app_label = Label(frame_display,
                  textvariable=valor_texto,
                  width=22,
                  height=3,
                  padx=7,
                  relief=FLAT,
                  anchor="e",
                  justify=RIGHT,
                  font='Ivy 18',
                  bg=azul,
                  fg=branco)
app_label.place(x=0, y=0)

# Criar os botões
# Primeira linha
limpar = Button(frame_corpo,
                text="C",
                width=10,
                height=2,
                bg=cinza,
                font='Ivy 13 bold',
                relief=RAISED,
                overrelief=RIDGE,
                command=limpar_tela)
limpar.place(x=0, y=0)
percentual = Button(frame_corpo,
                    text="%",
                    width=3,
                    height=2,
                    bg=cinza,
                    font='Ivy 13 bold',
                    relief=RAISED,
                    overrelief=RIDGE,
                    command=lambda: entrar_valores("%"))
percentual.place(x=126, y=0)
dividir = Button(frame_corpo,
                 text="/",
                 width=3,
                 height=2,
                 bg=laranja,
                 font='Ivy 13 bold',
                 relief=RAISED,
                 overrelief=RIDGE,
                 command=lambda: entrar_valores("/"))
dividir.place(x=189, y=0)

# Segunda linha
sete = Button(frame_corpo,
              text="7",
              width=3,
              height=2,
              font='Ivy 13 bold',
              relief=RAISED,
              overrelief=RIDGE,
              command=lambda: entrar_valores("7"))
sete.place(x=0, y=46)
oito = Button(frame_corpo,
              text="8",
              width=3,
              height=2,
              fg=preto,
              font='Ivy 13 bold',
              relief=RAISED,
              overrelief=RIDGE,
              command=lambda: entrar_valores("8"))
oito.place(x=63, y=46)
nove = Button(frame_corpo,
              text="9",
              width=3,
              height=2,
              font='Ivy 13 bold',
              relief=RAISED,
              overrelief=RIDGE,
              command=lambda: entrar_valores("9"))
nove.place(x=126, y=46)
multiplicar = Button(frame_corpo,
                     text="*",
                     width=3,
                     height=2,
                     fg=preto,
                     font='Ivy 13 bold',
                     relief=RAISED,
                     overrelief=RIDGE,
                     command=lambda: entrar_valores("*"))
multiplicar.place(x=189, y=46)

# Terceira linha
quatro = Button(frame_corpo,
                text="4",
                width=3,
                height=2,
                font='Ivy 13 bold',
                relief=RAISED,
                overrelief=RIDGE,
                command=lambda: entrar_valores("4"))
quatro.place(x=0, y=92)
cinco = Button(frame_corpo,
               text="5",
               width=3,
               height=2,
               fg=preto,
               font='Ivy 13 bold',
               relief=RAISED,
               overrelief=RIDGE,
               command=lambda: entrar_valores("5"))
cinco.place(x=63, y=92)
seis = Button(frame_corpo,
              text="6",
              width=3,
              height=2,
              font='Ivy 13 bold',
              relief=RAISED,
              overrelief=RIDGE,
              command=lambda: entrar_valores("6"))
seis.place(x=126, y=92)
subtrair = Button(frame_corpo,
                  text="-",
                  width=3,
                  height=2,
                  fg=preto,
                  font='Ivy 13 bold',
                  relief=RAISED,
                  overrelief=RIDGE,
                  command=lambda: entrar_valores("-"))
subtrair.place(x=189, y=92)

# Quarta linha
um = Button(frame_corpo,
            text="1",
            width=3,
            height=2,
            font='Ivy 13 bold',
            relief=RAISED,
            overrelief=RIDGE,
            command=lambda: entrar_valores("1"))
um.place(x=0, y=138)
dois = Button(frame_corpo,
              text="2",
              width=3,
              height=2,
              fg=preto,
              font='Ivy 13 bold',
              relief=RAISED,
              overrelief=RIDGE,
              command=lambda: entrar_valores("2"))
dois.place(x=63, y=138)
tres = Button(frame_corpo,
              text="3",
              width=3,
              height=2,
              font='Ivy 13 bold',
              relief=RAISED,
              overrelief=RIDGE,
              command=lambda: entrar_valores("3"))
tres.place(x=126, y=138)
somar = Button(frame_corpo,
               text="+",
               width=3,
               height=2,
               fg=preto,
               font='Ivy 13 bold',
               relief=RAISED,
               overrelief=RIDGE,
               command=lambda: entrar_valores("+"))
somar.place(x=189, y=138)

# Quinta linha
zero = Button(frame_corpo,
              text="0",
              width=10,
              height=2,
              font='Ivy 13 bold',
              relief=RAISED,
              overrelief=RIDGE,
              command=lambda: entrar_valores("0"))
zero.place(x=0, y=184)
ponto = Button(frame_corpo,
               text=".",
               width=3,
               height=2,
               fg=preto,
               font='Ivy 13 bold',
               relief=RAISED,
               overrelief=RIDGE,
               command=lambda: entrar_valores("."))
ponto.place(x=126, y=184)
resultado = Button(frame_corpo,
                   text="=",
                   width=3,
                   height=2,
                   fg=preto,
                   font='Ivy 13 bold',
                   relief=RAISED,
                   overrelief=RIDGE,
                   command=calcular)
resultado.place(x=189, y=184)

janela.mainloop()
