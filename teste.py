from random import choice
from tkinter import *
from random import randint

itens = ("PEDRA", "PAPEL", "TESOURA")
computador = randint(0, 2)


def escolherMovimento():
    jogador = int(input("Qual sua jogada? "))

    texto = f'''
    Computador escolheu: {computador}
    Jogador: escolheu: {jogador}

    '''

    texto_resultado["text"] = texto


janela = Tk()
janela.title("JO..KEN..PO!!!")

texto_orientacao = Label(janela, text="Clique no botão para escolher seu movimento")
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="PEDRA", command=escolherMovimento)
botao.grid(column=0, row=1, padx=10, pady=10)

botao = Button(janela, text="PAPEL", )
botao.grid(column=0, row=2, padx=10, pady=10)

botao = Button(janela, text="TESOURA", )
botao.grid(column=0, row=3, padx=10, pady=10)

texto_resultado = Label(janela, text="")
texto_resultado.grid(column=0, row=4, padx=10, pady=10)

janela.mainloop()