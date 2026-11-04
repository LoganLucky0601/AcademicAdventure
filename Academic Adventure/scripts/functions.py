import pygame
import sys
from scripts.font import *
from scripts.settings import *
from scripts.interface import *
from scripts.cenas.personagem import *
from scripts.portrait import *
from scripts.dialog import *

def jogar():
    global cena
    cena = "cena3"

def limpar_e_desenhar(img):
    screen.fill([255, 255, 255])
    screen.blit(img, (0, 0))

def desenhar_img(img, x, y):
    screen.blit(img, (x, y))
    
def atualizar_tela():
    pygame.display.flip()
    clock.tick(60)



botao_continue = pygame.Rect(124, 343, 634, 115)
botao_sair = pygame.Rect(124, 480, 634, 115)

def draw_pause(screen, menu_pause, pixelify, nome, personagem_escolhido):
    # Desenha o menu de pausa na tela
    screen.blit(menu_pause, (0, 0))  # Ajuste as coordenadas conforme a posição desejada
    
    if personagem_escolhido == "menino":
        screen.blit(idle_mainchar, (1490, 445))
    elif personagem_escolhido == "menina":
        screen.blit(idle_fmainchar, (1490, 460))
    
    # Renderiza o texto (nome)
    nick = pixelify.render(nome, True, (255, 255, 255))
    
    # Obtenha o retângulo do texto renderizado (nick)
    nick_rect = nick.get_rect()

    # Calcular a largura da caixa baseado no texto
    name_box_width = nick.get_width() + 20  # Adicionando margem lateral
    name_box_height = 40
    
    # Verifica o comprimento do nome e define a posição da name_box de acordo
    if len(nome) < 10:
        name_box = pygame.Rect(1600, 379, name_box_width, name_box_height)  # Nome menor que 10
    elif len(nome) >= 10 and len(nome) <= 20:
        name_box = pygame.Rect(1565, 379, name_box_width, name_box_height)  # Nome entre 10 e 20
    elif len(nome) > 20 and len(nome) <= 30:
        name_box = pygame.Rect(1500, 379, name_box_width, name_box_height)  # Nome entre 20 e 30
    else:  # Caso o nome tenha mais de 30 caracteres
        name_box = pygame.Rect(1450, 379, name_box_width, name_box_height)  # Nome maior que 30


    # Cor cinza escuro para o fundo da namebox
    box_color = (50, 50, 50)  # Cor cinza escuro

    # Desenha o fundo (rect) da namebox
    pygame.draw.rect(screen, box_color, name_box)  # Desenha a caixa de fundo

    # Centraliza o texto dentro da name_box
    nick_rect.center = name_box.center

    # Desenha o texto no centro da name_box
    screen.blit(nick, nick_rect.topleft)











