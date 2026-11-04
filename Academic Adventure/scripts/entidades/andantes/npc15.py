import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc15 = [
    pygame.image.load("assets/sprites/andantes/npc15/top1.png"),
    pygame.image.load("assets/sprites/andantes/npc15/top2.png"),
    pygame.image.load("assets/sprites/andantes/npc15/top3.png"),
    pygame.image.load("assets/sprites/andantes/npc15/top4.png")
]

spr_baixo_npc15 = [
    pygame.image.load("assets/sprites/andantes/npc15/bottom1.png"),
    pygame.image.load("assets/sprites/andantes/npc15/bottom2.png"),
    pygame.image.load("assets/sprites/andantes/npc15/bottom3.png"),
    pygame.image.load("assets/sprites/andantes/npc15/bottom4.png")
]

spr_esquerda_npc15 = [
    pygame.image.load("assets/sprites/andantes/npc15/left1.png"),
    pygame.image.load("assets/sprites/andantes/npc15/left2.png"),
    pygame.image.load("assets/sprites/andantes/npc15/left3.png"),
    pygame.image.load("assets/sprites/andantes/npc15/left4.png")
]

spr_direita_npc15 = [
    pygame.image.load("assets/sprites/andantes/npc15/right1.png"),
    pygame.image.load("assets/sprites/andantes/npc15/right2.png"),
    pygame.image.load("assets/sprites/andantes/npc15/right3.png"),
    pygame.image.load("assets/sprites/andantes/npc15/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc15 = NPC(
    -6800,  # npc_x
    670,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc15,
        "esquerda": spr_esquerda_npc15,
        "cima": spr_cima_npc15,
        "baixo": spr_baixo_npc15
    },
    "direita"  # direção inicial
)

spr_atual_npc15 = npc15.animacoes["direita"][0]

npc15_rect = pygame.Rect(
    npc15.npc_x,
    npc15.npc_y,
    spr_atual_npc15.get_width(),
    spr_atual_npc15.get_height()
)