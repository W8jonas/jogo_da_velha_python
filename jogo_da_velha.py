import pygame
from pygame.locals import *
import sys

largura = 500
altura = 500
preto = (0, 0, 0)
branco = (255, 255, 255)
ponto_mouse_cor = (0, 0, 0)
tamanho = largura / 3.334
posicoes = []
respostas = [1, 1, 1, 1, 1, 1, 1, 1, 1]
imagem_de_fundo = preto
pygame.init()
relogio = pygame.time.Clock()
imagem_O = pygame.image.load('imagens/jogo_da_velha_modelos_O_azul.png')
imagem_X = pygame.image.load('imagens/jogo_da_velha_modelos_X_vermelho.png')


def jogo():
    global posicoes
    global respostas
    tela = pygame.display.set_mode([largura, altura])
    tela.fill(imagem_de_fundo)
    cont_posi = 0
    for i in range(0, 3):
        posicoes.append(pygame.Rect(largura / 40 + (tamanho + largura / 40) * i, altura / 40, tamanho, tamanho))
        cont_posi += 1
    cont_posi = 0
    for i in range(4, 7):
        posicoes.append(
            pygame.Rect(largura / 40 + (tamanho + largura / 40) * cont_posi, altura / 40 + (tamanho + altura / 40),
                        tamanho, tamanho))
        cont_posi += 1
    cont_posi = 0
    for i in range(7, 10):
        posicoes.append(
            pygame.Rect(largura / 40 + (tamanho + largura / 40) * cont_posi, altura / 40 + (tamanho + altura / 40) * 2,
                        tamanho, tamanho))
        cont_posi += 1

    ponto_mouse = pygame.Rect(100, 100, 1, 1)
    jogador_atual = jogador_1
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(0, 9):
                    if (ponto_mouse.colliderect(posicoes[i])) and (respostas[i] == 1):
                        respostas[i] = jogador_atual
                        if jogador_atual == jogador_1:
                            jogador_atual = jogador_2
                        else:
                            jogador_atual = jogador_1

        for i in range(0, 9):
            pygame.draw.rect(tela, branco, posicoes[i])
            position_eixo_x = posicoes[i].left
            position_eixo_y = posicoes[i].top
            if respostas[i] == 'X':
                tela.blit(imagem_X, (position_eixo_x, position_eixo_y))
            if respostas[i] == 'O':
                tela.blit(imagem_O, (position_eixo_x, position_eixo_y))

        (ponto_mouse.left, ponto_mouse.top) = pygame.mouse.get_pos()
        pygame.draw.rect(tela, ponto_mouse_cor, ponto_mouse)

        pygame.display.update()
        relogio.tick(50)


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

jogo()
