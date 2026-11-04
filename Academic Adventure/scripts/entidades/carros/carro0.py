import pygame
from scripts.carro import Carro

# Carrega os sprites do carro
spr_esquerda_carro0 = [
    pygame.image.load("assets/sprites/carros/carro0/left1.png"),
    pygame.image.load("assets/sprites/carros/carro0/left2.png"),
    pygame.image.load("assets/sprites/carros/carro0/left3.png"),
    pygame.image.load("assets/sprites/carros/carro0/left4.png"),
]

spr_direita_carro0 = [
    pygame.image.load("assets/sprites/carros/carro0/left1.png"),
    pygame.image.load("assets/sprites/carros/carro0/left1.png"),
    pygame.image.load("assets/sprites/carros/carro0/left1.png"),
    pygame.image.load("assets/sprites/carros/carro0/left1.png"),
]

spr_parado_carro0 = [
    pygame.image.load("assets/sprites/carros/carro0/left1.png"),
    pygame.image.load("assets/sprites/carros/carro0/left1.png"),
    pygame.image.load("assets/sprites/carros/carro0/left1.png"),
    pygame.image.load("assets/sprites/carros/carro0/left1.png"),
]

# Crie uma instância do carro usando a classe Carro
carro0 = Carro(
    1920,  # carro_x
    730,  # carro_y
    5,  # velocidade
    -999999,  # limite_esquerda
    10,  # limite_direita
    {
        "esquerda": spr_esquerda_carro0,
        "direita": spr_direita_carro0,
        "parado": spr_parado_carro0,
    },
    "esquerda"  # direção inicial
)

spr_atual_carro0 = carro0.animacoes["esquerda"][0]

carro0_rect = pygame.Rect(
    carro0.carro_x,
    carro0.carro_y,
    spr_atual_carro0.get_width(),
    spr_atual_carro0.get_height()
)