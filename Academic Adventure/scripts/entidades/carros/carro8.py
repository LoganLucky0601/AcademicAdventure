import pygame
from scripts.carro import Carro

# Carrega os sprites do carro
spr_esquerda_carro8 = [
    pygame.image.load("assets/sprites/carros/carro3/left1.png"),
    pygame.image.load("assets/sprites/carros/carro3/left2.png"),
    pygame.image.load("assets/sprites/carros/carro3/left3.png"),
    pygame.image.load("assets/sprites/carros/carro3/left4.png"),
]

spr_direita_carro8 = [
    pygame.image.load("assets/sprites/carros/carro3/right1.png"),
    pygame.image.load("assets/sprites/carros/carro3/right2.png"),
    pygame.image.load("assets/sprites/carros/carro3/right3.png"),
    pygame.image.load("assets/sprites/carros/carro3/right4.png"),
]

# Crie uma instância do carro usando a classe Carro
carro8 = Carro(
    54000,  # carro_x
    850,  # carro_y
    10,  # velocidade
    -999999,  # limite_esquerda
    10,  # limite_direita
    {
        "esquerda": spr_esquerda_carro8,
        "direita": spr_direita_carro8
    },
    "esquerda"  # direção inicial
)

spr_atual_carro8 = carro8.animacoes["esquerda"][0]

carro8_rect = pygame.Rect(
    carro8.carro_x,
    carro8.carro_y,
    spr_atual_carro8.get_width(),
    spr_atual_carro8.get_height()
)