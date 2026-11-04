import pygame
from scripts.carro import Carro

# Carrega os sprites do carro
spr_esquerda_carro17 = [
    pygame.image.load("assets/sprites/carros/carro17/left1.png"),
    pygame.image.load("assets/sprites/carros/carro17/left2.png"),
    pygame.image.load("assets/sprites/carros/carro17/left3.png"),
    pygame.image.load("assets/sprites/carros/carro17/left4.png"),
]

spr_direita_carro17 = [
    pygame.image.load("assets/sprites/carros/carro17/right1.png"),
    pygame.image.load("assets/sprites/carros/carro17/right2.png"),
    pygame.image.load("assets/sprites/carros/carro17/right3.png"),
    pygame.image.load("assets/sprites/carros/carro17/right4.png"),
]

# Crie uma instância do carro usando a classe Carro
carro17 = Carro(
    126000,  # carro_x
    850,  # carro_y
    10,  # velocidade
    -999999,  # limite_esquerda
    10,  # limite_direita
    {
        "esquerda": spr_esquerda_carro17,
        "direita": spr_direita_carro17
    },
    "esquerda"  # direção inicial
)

spr_atual_carro17 = carro17.animacoes["esquerda"][0]

carro17_rect = pygame.Rect(
    carro17.carro_x,
    carro17.carro_y,
    spr_atual_carro17.get_width(),
    spr_atual_carro17.get_height()
)