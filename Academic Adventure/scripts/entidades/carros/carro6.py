import pygame
from scripts.carro import Carro

# Carrega os sprites do carro
spr_esquerda_carro6 = [
    pygame.image.load("assets/sprites/carros/carro1/left1.png"),
    pygame.image.load("assets/sprites/carros/carro1/left2.png"),
    pygame.image.load("assets/sprites/carros/carro1/left3.png"),
    pygame.image.load("assets/sprites/carros/carro1/left4.png"),
]

spr_direita_carro6 = [
    pygame.image.load("assets/sprites/carros/carro1/right1.png"),
    pygame.image.load("assets/sprites/carros/carro1/right2.png"),
    pygame.image.load("assets/sprites/carros/carro1/right3.png"),
    pygame.image.load("assets/sprites/carros/carro1/right4.png"),
]

# Crie uma instância do carro usando a classe Carro
carro6 = Carro(
    38000,  # carro_x
    850,  # carro_y
    10,  # velocidade
    -999999,  # limite_esquerda
    10,  # limite_direita
    {
        "esquerda": spr_esquerda_carro6,
        "direita": spr_direita_carro6
    },
    "esquerda"  # direção inicial
)

spr_atual_carro6 = carro6.animacoes["esquerda"][0]

carro6_rect = pygame.Rect(
    carro6.carro_x,
    carro6.carro_y,
    spr_atual_carro6.get_width(),
    spr_atual_carro6.get_height()
)