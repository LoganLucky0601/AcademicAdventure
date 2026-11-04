import pygame
from scripts.carro import Carro

# Carrega os sprites do carro
spr_esquerda_carro9 = [
    pygame.image.load("assets/sprites/carros/carro4/left1.png"),
    pygame.image.load("assets/sprites/carros/carro4/left2.png"),
    pygame.image.load("assets/sprites/carros/carro4/left3.png"),
    pygame.image.load("assets/sprites/carros/carro4/left4.png"),
]

spr_direita_carro9 = [
    pygame.image.load("assets/sprites/carros/carro4/right1.png"),
    pygame.image.load("assets/sprites/carros/carro4/right2.png"),
    pygame.image.load("assets/sprites/carros/carro4/right3.png"),
    pygame.image.load("assets/sprites/carros/carro4/right4.png"),
]

# Crie uma instância do carro usando a classe Carro
carro9 = Carro(
    62000,  # carro_x
    850,  # carro_y
    10,  # velocidade
    -999999,  # limite_esquerda
    10,  # limite_direita
    {
        "esquerda": spr_esquerda_carro9,
        "direita": spr_direita_carro9
    },
    "esquerda"  # direção inicial
)

spr_atual_carro9 = carro9.animacoes["esquerda"][0]

carro9_rect = pygame.Rect(
    carro9.carro_x,
    carro9.carro_y,
    spr_atual_carro9.get_width(),
    spr_atual_carro9.get_height()
)