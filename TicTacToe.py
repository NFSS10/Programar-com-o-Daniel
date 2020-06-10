import random

"""

TicTacToe

"""

player1 = input("Nome primeiro jogador: ")
player2 = input("Nome do segundo jogador: ")

lancamento = random.randrange(0,2) # Fiz alteracao do 1 para 2 para que ao correr o random o numero "1" tambem surgir


if lancamento == 0:
    player_coin1 = "cara"
    player_coin2 = "coroa"

else:
    player_coin2 = "cara"
    player_coin1 = "coroa"

print(f'{player1} é {player_coin1}')
print(f'{player2} é {player_coin2}')

lancamento2 = random.randrange(0,2) # Fiz alteracao do 1 para 2 para que ao correr o random o numero "1" tambem surgir

if lancamento2 == 0:
    print('Começa primeiro o jogador que saiu cara')
else:
    print('Começa primeiro o jogador que saiu coroa')
