import pygame
from pygame.locals import *
import time
import sys

largura = 500
altura = 500
preto = (0, 0, 0)
branco = (255, 255, 255)
tamanho = largura / 3.334
posicoes = []
respostas = [1, 1, 1, 1, 1, 1, 1, 1, 1]
imagem_de_fundo = preto
ponto_mouse_cor = imagem_de_fundo
cor_x = "preto"
cor_o = "preto"
pygame.init()
relogio = pygame.time.Clock()
contador = 0
condicao = True
ganhou = '-'


def vitoria(valor_de_teste):
    global ganhou
    global contador
    contador += 1
    if respostas[0] == valor_de_teste and respostas[1] == valor_de_teste and respostas[2] == valor_de_teste:
        ganhou = valor_de_teste

    elif respostas[3] == valor_de_teste and respostas[4] == valor_de_teste and respostas[5] == valor_de_teste:
        ganhou = valor_de_teste

    elif respostas[6] == valor_de_teste and respostas[7] == valor_de_teste and respostas[8] == valor_de_teste:
        ganhou = valor_de_teste

    elif respostas[0] == valor_de_teste and respostas[3] == valor_de_teste and respostas[6] == valor_de_teste:
        ganhou = valor_de_teste

    elif respostas[1] == valor_de_teste and respostas[4] == valor_de_teste and respostas[7] == valor_de_teste:
        ganhou = valor_de_teste

    elif respostas[2] == valor_de_teste and respostas[5] == valor_de_teste and respostas[8] == valor_de_teste:
        ganhou = valor_de_teste

    elif respostas[0] == valor_de_teste and respostas[4] == valor_de_teste and respostas[8] == valor_de_teste:
        ganhou = valor_de_teste

    elif respostas[2] == valor_de_teste and respostas[4] == valor_de_teste and respostas[6] == valor_de_teste:
        ganhou = valor_de_teste
    elif contador == 9:
        ganhou = "e"
    return ganhou


def jogo():
    global condicao
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
    while condicao:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(0, 9):
                    if (ponto_mouse.colliderect(posicoes[i])) and (respostas[i] == 1):
                        respostas[i] = jogador_atual
                        if vitoria(jogador_atual) is not '-':
                            if ganhou == 'X':
                                print('O X ganhou a rodada')
                            elif ganhou == 'O':
                                print('O O ganhou a rodada')
                            elif ganhou == 'e':
                                print('Deu velha')
                            condicao = False
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
    time.sleep(5)
    pygame.quit()
    sys.exit()


jogador_1 = input(print('Escolha X ou O'))
jogador_1 = jogador_1.upper()

if jogador_1 == 'X' or jogador_1 == 'O':

    if jogador_1 == 'X':
        jogador_2 = 'O'
        cor_x = input(
            print("Jogador 1, escolha a cor do seu X   (Azul, vermelho, verde, preto, amarelo, laranja, roxo)"))
        cor_o = input(print("Jogador 2, escolha a cor da sua O"))
    else:
        jogador_2 = 'X'
        cor_o = input(print("Jogador 1, escolha a cor da sua O"))
        cor_x = input(print("Jogador 2, escolha a cor do seu X"))

else:
    print("Você digitou errado. Nesse caso:")
    jogador_1 = 'X'
    jogador_2 = 'O'
    cor_x = input(print("Jogador 1, escolha a cor do seu X   (Azul, vermelho, verde, preto, amarelo, laranja, roxo)"))
    cor_o = input(print("Jogador 2, escolha a cor da sua O"))

cor_x = cor_x.lower()
cor_o = cor_o.lower()
print(f'O jogador 1 fica com {jogador_1} {cor_x} e o jogador 2 fica com {jogador_2} {cor_o}')

print(cor_x)
print(cor_o)
texto1 = "imagens/jogo_da_velha_modelos_O_" + cor_o + ".png"
texto2 = "imagens/jogo_da_velha_modelos_X_" + cor_x + ".png"
imagem_O = pygame.image.load(texto1)
imagem_X = pygame.image.load(texto2)

imagem_O = pygame.transform.smoothscale(imagem_O, (int(largura / 3.334), int(largura / 3.334)))
imagem_X = pygame.transform.smoothscale(imagem_X, (int(largura / 3.334), int(largura / 3.334)))

jogo()
