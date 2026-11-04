import pygame
from scripts.carro import Carro

# Carrega os sprites do carro
spr_esquerda_carro12 = [
    pygame.image.load("assets/sprites/carros/carro12/left1.png"),
    pygame.image.load("assets/sprites/carros/carro12/left2.png"),
    pygame.image.load("assets/sprites/carros/carro12/left3.png"),
    pygame.image.load("assets/sprites/carros/carro12/left4.png"),
]

spr_direita_carro12 = [
    pygame.image.load("assets/sprites/carros/carro12/right1.png"),
    pygame.image.load("assets/sprites/carros/carro12/right2.png"),
    pygame.image.load("assets/sprites/carros/carro12/right3.png"),
    pygame.image.load("assets/sprites/carros/carro12/right4.png"),
]

# Crie uma instância do carro usando a classe Carro
carro12 = Carro(
    86000,  # carro_x
    850,  # carro_y
    10,  # velocidade
    -999999,  # limite_esquerda
    10,  # limite_direita
    {
        "esquerda": spr_esquerda_carro12,
        "direita": spr_direita_carro12
    },
    "esquerda"  # direção inicial
)

spr_atual_carro12 = carro12.animacoes["esquerda"][0]

carro12_rect = pygame.Rect(
    carro12.carro_x,
    carro12.carro_y,
    spr_atual_carro12.get_width(),
    spr_atual_carro12.get_height()
)