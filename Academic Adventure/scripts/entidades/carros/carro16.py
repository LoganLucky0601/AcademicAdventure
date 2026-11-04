import pygame
from scripts.carro import Carro

# Carrega os sprites do carro
spr_esquerda_carro16 = [
    pygame.image.load("assets/sprites/carros/carro16/left1.png"),
    pygame.image.load("assets/sprites/carros/carro16/left2.png"),
    pygame.image.load("assets/sprites/carros/carro16/left3.png"),
    pygame.image.load("assets/sprites/carros/carro16/left4.png"),
]

spr_direita_carro16 = [
    pygame.image.load("assets/sprites/carros/carro16/right1.png"),
    pygame.image.load("assets/sprites/carros/carro16/right2.png"),
    pygame.image.load("assets/sprites/carros/carro16/right3.png"),
    pygame.image.load("assets/sprites/carros/carro16/right4.png"),
]

# Crie uma instância do carro usando a classe Carro
carro16 = Carro(
    118000,  # carro_x
    850,  # carro_y
    10,  # velocidade
    -999999,  # limite_esquerda
    10,  # limite_direita
    {
        "esquerda": spr_esquerda_carro16,
        "direita": spr_direita_carro16
    },
    "esquerda"  # direção inicial
)

spr_atual_carro16 = carro16.animacoes["esquerda"][0]

carro16_rect = pygame.Rect(
    carro16.carro_x,
    carro16.carro_y,
    spr_atual_carro16.get_width(),
    spr_atual_carro16.get_height()
)