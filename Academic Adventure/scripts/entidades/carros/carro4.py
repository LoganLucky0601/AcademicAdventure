import pygame
from scripts.carro import Carro

# Carrega os sprites do carro
spr_esquerda_carro4 = [
    pygame.image.load("assets/sprites/carros/carro4/left1.png"),
    pygame.image.load("assets/sprites/carros/carro4/left2.png"),
    pygame.image.load("assets/sprites/carros/carro4/left3.png"),
    pygame.image.load("assets/sprites/carros/carro4/left4.png"),
]

spr_direita_carro4 = [
    pygame.image.load("assets/sprites/carros/carro4/right1.png"),
    pygame.image.load("assets/sprites/carros/carro4/right2.png"),
    pygame.image.load("assets/sprites/carros/carro4/right3.png"),
    pygame.image.load("assets/sprites/carros/carro4/right4.png"),
]

# Crie uma instância do carro usando a classe Carro
carro4 = Carro(
    22000,  # carro_x
    850,  # carro_y
    10,  # velocidade
    -999999,  # limite_esquerda
    10,  # limite_direita
    {
        "esquerda": spr_esquerda_carro4,
        "direita": spr_direita_carro4
    },
    "esquerda"  # direção inicial
)

spr_atual_carro4 = carro4.animacoes["esquerda"][0]

carro4_rect = pygame.Rect(
    carro4.carro_x,
    carro4.carro_y,
    spr_atual_carro4.get_width(),
    spr_atual_carro4.get_height()
)