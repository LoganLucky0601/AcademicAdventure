import pygame
from scripts.carro import Carro

# Carrega os sprites do carro
spr_esquerda_carro13 = [
    pygame.image.load("assets/sprites/carros/carro13/left1.png"),
    pygame.image.load("assets/sprites/carros/carro13/left2.png"),
    pygame.image.load("assets/sprites/carros/carro13/left3.png"),
    pygame.image.load("assets/sprites/carros/carro13/left4.png"),
]

spr_direita_carro13 = [
    pygame.image.load("assets/sprites/carros/carro13/right1.png"),
    pygame.image.load("assets/sprites/carros/carro13/right2.png"),
    pygame.image.load("assets/sprites/carros/carro13/right3.png"),
    pygame.image.load("assets/sprites/carros/carro13/right4.png"),
]

# Crie uma instância do carro usando a classe Carro
carro13 = Carro(
    94000,  # carro_x
    850,  # carro_y
    10,  # velocidade
    -999999,  # limite_esquerda
    10,  # limite_direita
    {
        "esquerda": spr_esquerda_carro13,
        "direita": spr_direita_carro13
    },
    "esquerda"  # direção inicial
)

spr_atual_carro13 = carro13.animacoes["esquerda"][0]

carro13_rect = pygame.Rect(
    carro13.carro_x,
    carro13.carro_y,
    spr_atual_carro13.get_width(),
    spr_atual_carro13.get_height()
)