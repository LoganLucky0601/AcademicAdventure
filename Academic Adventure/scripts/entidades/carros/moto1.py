import pygame
from scripts.carro import Carro

# Carrega os sprites da moto
spr_esquerda_moto1 = [
    pygame.image.load("assets/sprites/carros/moto1/left1.png"),
    pygame.image.load("assets/sprites/carros/moto1/left2.png"),
    pygame.image.load("assets/sprites/carros/moto1/left3.png"),
    pygame.image.load("assets/sprites/carros/moto1/left4.png"),
]

spr_direita_moto1 = [
    pygame.image.load("assets/sprites/carros/moto1/right1.png"),
    pygame.image.load("assets/sprites/carros/moto1/right2.png"),
    pygame.image.load("assets/sprites/carros/moto1/right3.png"),
    pygame.image.load("assets/sprites/carros/moto1/right4.png"),
]

# Crie uma instância da moto usando a classe Moto
moto1 = Carro(
    4000,  # moto_x
    850,  # moto_y
    15,  # velocidade
    -999999,  # limite_esquerda
    10,  # limite_direita
    {
        "esquerda": spr_esquerda_moto1,
        "direita": spr_direita_moto1
    },
    "esquerda"  # direção inicial
)

spr_atual_moto1 = moto1.animacoes["esquerda"][0]

moto1_rect = pygame.Rect(
    moto1.carro_x,
    moto1.carro_y,
    spr_atual_moto1.get_width(),
    spr_atual_moto1.get_height()
)