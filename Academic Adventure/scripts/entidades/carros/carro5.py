import pygame
from scripts.carro import Carro

# Carrega os sprites do carro
spr_esquerda_carro5 = [
    pygame.image.load("assets/sprites/carros/carro5/left1.png"),
    pygame.image.load("assets/sprites/carros/carro5/left2.png"),
    pygame.image.load("assets/sprites/carros/carro5/left3.png"),
    pygame.image.load("assets/sprites/carros/carro5/left4.png"),
]

spr_direita_carro5 = [
    pygame.image.load("assets/sprites/carros/carro5/right1.png"),
    pygame.image.load("assets/sprites/carros/carro5/right2.png"),
    pygame.image.load("assets/sprites/carros/carro5/right3.png"),
    pygame.image.load("assets/sprites/carros/carro5/right4.png"),
]

# Crie uma instância do carro usando a classe Carro
carro5 = Carro(
    30000,  # carro_x
    850,  # carro_y
    10,  # velocidade
    -999999,  # limite_esquerda
    10,  # limite_direita
    {
        "esquerda": spr_esquerda_carro5,
        "direita": spr_direita_carro5
    },
    "esquerda"  # direção inicial
)

spr_atual_carro5 = carro5.animacoes["esquerda"][0]

carro5_rect = pygame.Rect(
    carro5.carro_x,
    carro5.carro_y,
    spr_atual_carro5.get_width(),
    spr_atual_carro5.get_height()
)