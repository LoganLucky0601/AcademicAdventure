import pygame
from scripts.carro import Carro

# Carrega os sprites do carro
spr_esquerda_carro15 = [
    pygame.image.load("assets/sprites/carros/carro15/left1.png"),
    pygame.image.load("assets/sprites/carros/carro15/left2.png"),
    pygame.image.load("assets/sprites/carros/carro15/left3.png"),
    pygame.image.load("assets/sprites/carros/carro15/left4.png"),
]

spr_direita_carro15 = [
    pygame.image.load("assets/sprites/carros/carro15/right1.png"),
    pygame.image.load("assets/sprites/carros/carro15/right2.png"),
    pygame.image.load("assets/sprites/carros/carro15/right3.png"),
    pygame.image.load("assets/sprites/carros/carro15/right4.png"),
]

# Crie uma instância do carro usando a classe Carro
carro15 = Carro(
    110000,  # carro_x
    850,  # carro_y
    10,  # velocidade
    -999999,  # limite_esquerda
    10,  # limite_direita
    {
        "esquerda": spr_esquerda_carro15,
        "direita": spr_direita_carro15
    },
    "esquerda"  # direção inicial
)

spr_atual_carro15 = carro15.animacoes["esquerda"][0]

carro15_rect = pygame.Rect(
    carro15.carro_x,
    carro15.carro_y,
    spr_atual_carro15.get_width(),
    spr_atual_carro15.get_height()
)