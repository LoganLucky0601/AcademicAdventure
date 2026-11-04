import pygame
from scripts.carro import Carro

# Carrega os sprites do carro
spr_esquerda_carro18 = [
    pygame.image.load("assets/sprites/carros/carro18/left1.png"),
    pygame.image.load("assets/sprites/carros/carro18/left2.png"),
    pygame.image.load("assets/sprites/carros/carro18/left3.png"),
    pygame.image.load("assets/sprites/carros/carro18/left4.png"),
]

spr_direita_carro18 = [
    pygame.image.load("assets/sprites/carros/carro18/right1.png"),
    pygame.image.load("assets/sprites/carros/carro18/right2.png"),
    pygame.image.load("assets/sprites/carros/carro18/right3.png"),
    pygame.image.load("assets/sprites/carros/carro18/right4.png"),
]

# Crie uma instância do carro usando a classe Carro
carro18 = Carro(
    134000,  # carro_x
    850,  # carro_y
    10,  # velocidade
    -999999,  # limite_esquerda
    10,  # limite_direita
    {
        "esquerda": spr_esquerda_carro18,
        "direita": spr_direita_carro18
    },
    "esquerda"  # direção inicial
)

spr_atual_carro18 = carro18.animacoes["esquerda"][0]

carro18_rect = pygame.Rect(
    carro18.carro_x,
    carro18.carro_y,
    spr_atual_carro18.get_width(),
    spr_atual_carro18.get_height()
)