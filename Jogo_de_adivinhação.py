from random import randint

# Jogo de Adivinhação

'''
--> Escolher nº inteiro de [0,50]; # Validado
--> Dicas de acima/abaixo; # Validado
--> Apenas 10 tentativas # Falta validar

'''
computador = randint(0,50) # Gerar um numero random de 0 a 50
print('Acabei de pensar em um nuemero entre 0 e 50 \nConsegues adivinhar qual foi? \nSó tens 10 tentativas ')
acertou = False # Atribuir Falso para poder realizar "loop" até acertar
palpite = 0 # Criar uma variavel para palpite para poder contabilizar 
nacertou = True

while not acertou:
    numero = int(input('Qual o seu palpite '))  # Jogador dá palpite
    palpite += 1 # Adiciono um paplite caso o jogador falhe
    if numero == computador: # Se numero de jogador é igual ao random do computador entao o "acertou" é "True"
        acertou = True
    else: # Mais, se o numero é menor do que o random entao "print mais", caso contrario "print menos"
        if numero < computador:
            print('Mais... Tente novamente')
        elif numero > computador:
            print('Menos... Tente novamente')

print('Acertou com {} tentativas. Parabéns!'.format(palpite)) # Caso o jogador acerte irá indicar o numero de palpites

