import pygame
from scripts.carro import Carro

# Carrega os sprites do carro
spr_esquerda_carro2 = [
    pygame.image.load("assets/sprites/carros/carro2/left1.png"),
    pygame.image.load("assets/sprites/carros/carro2/left2.png"),
    pygame.image.load("assets/sprites/carros/carro2/left3.png"),
    pygame.image.load("assets/sprites/carros/carro2/left4.png"),
]

spr_direita_carro2 = [
    pygame.image.load("assets/sprites/carros/carro2/right1.png"),
    pygame.image.load("assets/sprites/carros/carro2/right2.png"),
    pygame.image.load("assets/sprites/carros/carro2/right3.png"),
    pygame.image.load("assets/sprites/carros/carro2/right4.png"),
]

# Crie uma instância do carro usando a classe Carro
carro2 = Carro(
    10000,  # carro_x
    850,  # carro_y
    10,  # velocidade
    -999999,  # limite_esquerda
    10,  # limite_direita
    {
        "esquerda": spr_esquerda_carro2,
        "direita": spr_direita_carro2
    },
    "esquerda"  # direção inicial
)

spr_atual_carro2 = carro2.animacoes["esquerda"][0]

carro2_rect = pygame.Rect(
    carro2.carro_x,
    carro2.carro_y,
    spr_atual_carro2.get_width(),
    spr_atual_carro2.get_height()
)