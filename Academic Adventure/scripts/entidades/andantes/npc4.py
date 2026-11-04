import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc4 = [
    pygame.image.load("assets/sprites/andantes/npc4/top1.png"),
    pygame.image.load("assets/sprites/andantes/npc4/top2.png"),
    pygame.image.load("assets/sprites/andantes/npc4/top3.png"),
    pygame.image.load("assets/sprites/andantes/npc4/top4.png")
]

spr_baixo_npc4 = [
    pygame.image.load("assets/sprites/andantes/npc4/bottom1.png"),
    pygame.image.load("assets/sprites/andantes/npc4/bottom2.png"),
    pygame.image.load("assets/sprites/andantes/npc4/bottom3.png"),
    pygame.image.load("assets/sprites/andantes/npc4/bottom4.png")
]

spr_esquerda_npc4 = [
    pygame.image.load("assets/sprites/andantes/npc4/left1.png"),
    pygame.image.load("assets/sprites/andantes/npc4/left2.png"),
    pygame.image.load("assets/sprites/andantes/npc4/left3.png"),
    pygame.image.load("assets/sprites/andantes/npc4/left4.png")
]

spr_direita_npc4 = [
    pygame.image.load("assets/sprites/andantes/npc4/right1.png"),
    pygame.image.load("assets/sprites/andantes/npc4/right2.png"),
    pygame.image.load("assets/sprites/andantes/npc4/right3.png"),
    pygame.image.load("assets/sprites/andantes/npc4/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc4 = NPC(
    4400,  # npc_x
    620,  # npc_y
    1.2,  # velocidade
    -9999999,  # limite_esquerda
    1901,  # limite_direita
    {
        "direita": spr_direita_npc4,
        "esquerda": spr_esquerda_npc4,
        "cima": spr_cima_npc4,
        "baixo": spr_baixo_npc4
    },
    "esquerda"  # direção inicial
)

spr_atual_npc4 = npc4.animacoes["esquerda"][0]

npc4_rect = pygame.Rect(
    npc4.npc_x,
    npc4.npc_y,
    spr_atual_npc4.get_width(),
    spr_atual_npc4.get_height()
)