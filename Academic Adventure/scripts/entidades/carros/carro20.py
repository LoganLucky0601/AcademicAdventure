import pygame
from scripts.carro import Carro

# Carrega os sprites do carro
spr_esquerda_carro20 = [
    pygame.image.load("assets/sprites/carros/carro20/left1.png"),
    pygame.image.load("assets/sprites/carros/carro20/left2.png"),
    pygame.image.load("assets/sprites/carros/carro20/left3.png"),
    pygame.image.load("assets/sprites/carros/carro20/left4.png"),
]

spr_direita_carro20 = [
    pygame.image.load("assets/sprites/carros/carro20/right1.png"),
    pygame.image.load("assets/sprites/carros/carro20/right2.png"),
    pygame.image.load("assets/sprites/carros/carro20/right3.png"),
    pygame.image.load("assets/sprites/carros/carro20/right4.png"),
]

# Crie uma instância do carro usando a classe Carro
carro20 = Carro(
    150000,  # carro_x
    850,  # carro_y
    10,  # velocidade
    -999999,  # limite_esquerda
    10,  # limite_direita
    {
        "esquerda": spr_esquerda_carro20,
        "direita": spr_direita_carro20
    },
    "esquerda"  # direção inicial
)

spr_atual_carro20 = carro20.animacoes["esquerda"][0]

carro20_rect = pygame.Rect(
    carro20.carro_x,
    carro20.carro_y,
    spr_atual_carro20.get_width(),
    spr_atual_carro20.get_height()
)