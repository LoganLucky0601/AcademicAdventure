import pygame
from scripts.carro import Carro

# Carrega os sprites do carro
spr_esquerda_carro11 = [
    pygame.image.load("assets/sprites/carros/carro11/left1.png"),
    pygame.image.load("assets/sprites/carros/carro11/left2.png"),
    pygame.image.load("assets/sprites/carros/carro11/left3.png"),
    pygame.image.load("assets/sprites/carros/carro11/left4.png"),
]

spr_direita_carro11 = [
    pygame.image.load("assets/sprites/carros/carro11/right1.png"),
    pygame.image.load("assets/sprites/carros/carro11/right2.png"),
    pygame.image.load("assets/sprites/carros/carro11/right3.png"),
    pygame.image.load("assets/sprites/carros/carro11/right4.png"),
]

# Crie uma instância do carro usando a classe Carro
carro11 = Carro(
    78000,  # carro_x
    850,  # carro_y
    10,  # velocidade
    -999999,  # limite_esquerda
    10,  # limite_direita
    {
        "esquerda": spr_esquerda_carro11,
        "direita": spr_direita_carro11
    },
    "esquerda"  # direção inicial
)

spr_atual_carro11 = carro11.animacoes["esquerda"][0]

carro11_rect = pygame.Rect(
    carro11.carro_x,
    carro11.carro_y,
    spr_atual_carro11.get_width(),
    spr_atual_carro11.get_height()
)