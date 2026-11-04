import pygame
from scripts.carro import Carro

# Carrega os sprites do carro
spr_esquerda_carro19 = [
    pygame.image.load("assets/sprites/carros/carro19/left1.png"),
    pygame.image.load("assets/sprites/carros/carro19/left2.png"),
    pygame.image.load("assets/sprites/carros/carro19/left3.png"),
    pygame.image.load("assets/sprites/carros/carro19/left4.png"),
]

spr_direita_carro19 = [
    pygame.image.load("assets/sprites/carros/carro19/right1.png"),
    pygame.image.load("assets/sprites/carros/carro19/right2.png"),
    pygame.image.load("assets/sprites/carros/carro19/right3.png"),
    pygame.image.load("assets/sprites/carros/carro19/right4.png"),
]

# Crie uma instância do carro usando a classe Carro
carro19 = Carro(
    142000,  # carro_x
    850,  # carro_y
    10,  # velocidade
    -999999,  # limite_esquerda
    10,  # limite_direita
    {
        "esquerda": spr_esquerda_carro19,
        "direita": spr_direita_carro19
    },
    "esquerda"  # direção inicial
)

spr_atual_carro19 = carro19.animacoes["esquerda"][0]

carro19_rect = pygame.Rect(
    carro19.carro_x,
    carro19.carro_y,
    spr_atual_carro19.get_width(),
    spr_atual_carro19.get_height()
)