import pygame
from scripts.carro import Carro

# Carrega os sprites do carro
spr_esquerda_carro3 = [
    pygame.image.load("assets/sprites/carros/carro3/left1.png"),
    pygame.image.load("assets/sprites/carros/carro3/left2.png"),
    pygame.image.load("assets/sprites/carros/carro3/left3.png"),
    pygame.image.load("assets/sprites/carros/carro3/left4.png"),
]

spr_direita_carro3 = [
    pygame.image.load("assets/sprites/carros/carro3/right1.png"),
    pygame.image.load("assets/sprites/carros/carro3/right2.png"),
    pygame.image.load("assets/sprites/carros/carro3/right3.png"),
    pygame.image.load("assets/sprites/carros/carro3/right4.png"),
]

# Crie uma instância do carro usando a classe Carro
carro3 = Carro(
    16000,  # carro_x
    850,  # carro_y
    10,  # velocidade
    -999999,  # limite_esquerda
    10,  # limite_direita
    {
        "esquerda": spr_esquerda_carro3,
        "direita": spr_direita_carro3
    },
    "esquerda"  # direção inicial
)

spr_atual_carro3 = carro3.animacoes["esquerda"][0]

carro3_rect = pygame.Rect(
    carro3.carro_x,
    carro3.carro_y,
    spr_atual_carro3.get_width(),
    spr_atual_carro3.get_height()
)