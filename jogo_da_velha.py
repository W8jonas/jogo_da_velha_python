import pygame
from pygame.locals import *
import sys
import random
import time

#####   Variaveis caralho  #####

largura = 600
altura = 470

imagem_de_fundo = pygame.image.load('imagens/jogo_da_velha_modelo_3.png')

pygame.init()
relogio = pygame.time.Clock()

jogador_1 = input(print('Escolha X ou O'))
jogador_1 = jogador_1.upper()

if jogador_1 == 'X' or jogador_1 == 'O':

    if jogador_1 == 'X':
        jogador_2 = 'O'
    else:
        jogador_2 = 'X'

else:
    print("Você é retardado e digitou errado")
    print("Nesse caso,")
    jogador_1 = 'X'
    jogador_2 = 'O'

print(f'O jogador 1 fica com {jogador_1}')
print(f'E o jogador 2 fica com {jogador_2}')


def jogo():
    tela = pygame.display.set_mode([largura, altura])
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        tela.blit(imagem_de_fundo, (0, 0))
        pygame.display.update()
        relogio.tick(50)

jogo()

# ler valor da posição do mouse e do click, cada hora alterar entre X ou O e marcar numa matriz os valores escritos
# depois comparar os valores da matriz com os valores para ganhar.
# finalizar o projeto
# IDEIA NOVA
# Usar fundo preto e colocar cada quadrado branco formando a tabuleiro
