
import random

"""

TicTacToe


"""

player1 = input("Nome primeiro jogador: ")
player2 = input("Nome do segundo jogador: ")

lancamento = random.randrange(0,1)


if lancamento == 0:
    player_coin1 = "cara"
    player_coin2 = "coroa"

else:
    player_coin2 = "cara"
    player_coin1 = "coroa"

print(f'{player1} é {player_coin1}')
print(f'{player2} é {player_coin2}')

lancamento2 = random.randrange(0,1)

if lancamento2 == 0:
    print('Começa primeiro o jogador que saiu cara')
else:
    print('Começa primeiro o jogador que saiu coroa')


# A partir daqui já sabemos quem é o primeiro a jogar

jogo_acabou = False
while not jogo_acabou:
    if lancamento2 == 0:
        jogada = input("Jogador {} diz a tua jogada".format(player1))
        # aplicas a jogada
        jogada = input("Jogador {} diz a tua jogada".format(player2))
        # aplicas a jogada
    else:
        jogada = input("Jogador {} diz a tua jogada".format(player2))
        # aplicas a jogada
        jogada = input("Jogador {} diz a tua jogada".format(player1))
        # aplicas a jogada
