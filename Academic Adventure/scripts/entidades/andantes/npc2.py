import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc2 = [
    pygame.image.load("assets/sprites/andantes/npc2/top1.png"),
    pygame.image.load("assets/sprites/andantes/npc2/top2.png"),
    pygame.image.load("assets/sprites/andantes/npc2/top3.png"),
    pygame.image.load("assets/sprites/andantes/npc2/top4.png")
]

spr_baixo_npc2 = [
    pygame.image.load("assets/sprites/andantes/npc2/bottom1.png"),
    pygame.image.load("assets/sprites/andantes/npc2/bottom2.png"),
    pygame.image.load("assets/sprites/andantes/npc2/bottom3.png"),
    pygame.image.load("assets/sprites/andantes/npc2/bottom4.png")
]

spr_esquerda_npc2 = [
    pygame.image.load("assets/sprites/andantes/npc2/left1.png"),
    pygame.image.load("assets/sprites/andantes/npc2/left2.png"),
    pygame.image.load("assets/sprites/andantes/npc2/left3.png"),
    pygame.image.load("assets/sprites/andantes/npc2/left4.png")
]

spr_direita_npc2 = [
    pygame.image.load("assets/sprites/andantes/npc2/right1.png"),
    pygame.image.load("assets/sprites/andantes/npc2/right2.png"),
    pygame.image.load("assets/sprites/andantes/npc2/right3.png"),
    pygame.image.load("assets/sprites/andantes/npc2/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc2 = NPC(
    3600,  # npc_x
    650,  # npc_y
    1.4,  # velocidade
    -999999,  # limite_esquerda
    1400,  # limite_direita
    {
        "direita": spr_direita_npc2,
        "esquerda": spr_esquerda_npc2,
        "cima": spr_cima_npc2,
        "baixo": spr_baixo_npc2
    },
    "esquerda"  # direção inicial
)

spr_atual_npc2 = npc2.animacoes["esquerda"][0]

npc2_rect = pygame.Rect(
    npc2.npc_x,
    npc2.npc_y,
    spr_atual_npc2.get_width(),
    spr_atual_npc2.get_height()
)