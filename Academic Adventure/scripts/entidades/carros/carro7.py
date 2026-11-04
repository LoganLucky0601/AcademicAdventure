import pygame
from scripts.carro import Carro

# Carrega os sprites do carro
spr_esquerda_carro7 = [
    pygame.image.load("assets/sprites/carros/carro2/left1.png"),
    pygame.image.load("assets/sprites/carros/carro2/left2.png"),
    pygame.image.load("assets/sprites/carros/carro2/left3.png"),
    pygame.image.load("assets/sprites/carros/carro2/left4.png"),
]

spr_direita_carro7 = [
    pygame.image.load("assets/sprites/carros/carro2/right1.png"),
    pygame.image.load("assets/sprites/carros/carro2/right2.png"),
    pygame.image.load("assets/sprites/carros/carro2/right3.png"),
    pygame.image.load("assets/sprites/carros/carro2/right4.png"),
]

# Crie uma instância do carro usando a classe Carro
carro7 = Carro(
    46000,  # carro_x
    850,  # carro_y
    10,  # velocidade
    -999999,  # limite_esquerda
    10,  # limite_direita
    {
        "esquerda": spr_esquerda_carro7,
        "direita": spr_direita_carro7
    },
    "esquerda"  # direção inicial
)

spr_atual_carro7 = carro7.animacoes["esquerda"][0]

carro7_rect = pygame.Rect(
    carro7.carro_x,
    carro7.carro_y,
    spr_atual_carro7.get_width(),
    spr_atual_carro7.get_height()
)