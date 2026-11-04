import pygame
from scripts.carro import Carro

# Carrega os sprites do carro
spr_esquerda_carro14 = [
    pygame.image.load("assets/sprites/carros/carro14/left1.png"),
    pygame.image.load("assets/sprites/carros/carro14/left2.png"),
    pygame.image.load("assets/sprites/carros/carro14/left3.png"),
    pygame.image.load("assets/sprites/carros/carro14/left4.png"),
]

spr_direita_carro14 = [
    pygame.image.load("assets/sprites/carros/carro14/right1.png"),
    pygame.image.load("assets/sprites/carros/carro14/right2.png"),
    pygame.image.load("assets/sprites/carros/carro14/right3.png"),
    pygame.image.load("assets/sprites/carros/carro14/right4.png"),
]

# Crie uma instância do carro usando a classe Carro
carro14 = Carro(
    102000,  # carro_x
    850,  # carro_y
    10,  # velocidade
    -999999,  # limite_esquerda
    10,  # limite_direita
    {
        "esquerda": spr_esquerda_carro14,
        "direita": spr_direita_carro14
    },
    "esquerda"  # direção inicial
)

spr_atual_carro14 = carro14.animacoes["esquerda"][0]

carro14_rect = pygame.Rect(
    carro14.carro_x,
    carro14.carro_y,
    spr_atual_carro14.get_width(),
    spr_atual_carro14.get_height()
)