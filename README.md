# Ceep2025
desenvolvimento de sistemas 
#Daniel Labaig Tavares N5
import random
#biblioteca para efetivar o sorteio do numero, ja pronto, apenas iremos informar posteriormente o inter do jogo
import os
#biblioteca do sistema oprecional, para limpar a tela, se windows cls, no linux clear
erros=0
sorteado=random.randrange(0,100)
jogador=int(input("digite seu numero! "))
while(sorteado!=jogador):
    os.system("cls")
    if(sorteado<jogador):
        print("O numero digitado é maior que o sorteado")
    else:
        print("O numero digitado é"  " menor que o sorteado")
    erros=erros+1
    jogador=int(input("digite seu numero! "))                   
print("Parabens voce acertou o numero sorteado foi {} com {} erros".format(sorteado,erros)) 
