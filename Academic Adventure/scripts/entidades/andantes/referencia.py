import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_referencia = [
    pygame.image.load("assets/sprites/andantes/referencia/ref.png"),
    pygame.image.load("assets/sprites/andantes/referencia/ref.png"),
    pygame.image.load("assets/sprites/andantes/referencia/ref.png"),
    pygame.image.load("assets/sprites/andantes/referencia/ref.png")
]

spr_baixo_referencia = [
    pygame.image.load("assets/sprites/andantes/referencia/ref.png"),
    pygame.image.load("assets/sprites/andantes/referencia/ref.png"),
    pygame.image.load("assets/sprites/andantes/referencia/ref.png"),
    pygame.image.load("assets/sprites/andantes/referencia/ref.png")
]

spr_esquerda_referencia = [
    pygame.image.load("assets/sprites/andantes/referencia/ref.png"),
    pygame.image.load("assets/sprites/andantes/referencia/ref.png"),
    pygame.image.load("assets/sprites/andantes/referencia/ref.png"),
    pygame.image.load("assets/sprites/andantes/referencia/ref.png")
]

spr_direita_referencia = [
    pygame.image.load("assets/sprites/andantes/referencia/ref.png"),
    pygame.image.load("assets/sprites/andantes/referencia/ref.png"),
    pygame.image.load("assets/sprites/andantes/referencia/ref.png"),
    pygame.image.load("assets/sprites/andantes/referencia/ref.png")
]

# Crie uma instância do NPC usando a classe NPC
referencia = NPC(
    2000,  # npc_x
    650,  # npc_y
    1,  # velocidade
    -99999999999999999999999999999999999999,  # limite_esquerda
    999999,  # limite_direita
    {
        "direita": spr_direita_referencia,
        "esquerda": spr_esquerda_referencia,
        "cima": spr_cima_referencia,
        "baixo": spr_baixo_referencia
    },
    "esquerda"  # direção inicial
)

spr_atual_referencia = referencia.animacoes["esquerda"][0]

referencia_rect = pygame.Rect(
    referencia.npc_x,
    referencia.npc_y,
    spr_atual_referencia.get_width(),
    spr_atual_referencia.get_height()
)