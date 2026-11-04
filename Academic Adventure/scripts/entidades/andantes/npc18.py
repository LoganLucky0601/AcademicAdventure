import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc18 = [
    pygame.image.load("assets/sprites/andantes/npc18/top1.png"),
    pygame.image.load("assets/sprites/andantes/npc18/top2.png"),
    pygame.image.load("assets/sprites/andantes/npc18/top3.png"),
    pygame.image.load("assets/sprites/andantes/npc18/top4.png")
]

spr_baixo_npc18 = [
    pygame.image.load("assets/sprites/andantes/npc18/bottom1.png"),
    pygame.image.load("assets/sprites/andantes/npc18/bottom2.png"),
    pygame.image.load("assets/sprites/andantes/npc18/bottom3.png"),
    pygame.image.load("assets/sprites/andantes/npc18/bottom4.png")
]

spr_esquerda_npc18 = [
    pygame.image.load("assets/sprites/andantes/npc18/left1.png"),
    pygame.image.load("assets/sprites/andantes/npc18/left2.png"),
    pygame.image.load("assets/sprites/andantes/npc18/left3.png"),
    pygame.image.load("assets/sprites/andantes/npc18/left4.png")
]

spr_direita_npc18 = [
    pygame.image.load("assets/sprites/andantes/npc18/right1.png"),
    pygame.image.load("assets/sprites/andantes/npc18/right2.png"),
    pygame.image.load("assets/sprites/andantes/npc18/right3.png"),
    pygame.image.load("assets/sprites/andantes/npc18/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc18 = NPC(
    -12000,  # npc_x
    650,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc18,
        "esquerda": spr_esquerda_npc18,
        "cima": spr_cima_npc18,
        "baixo": spr_baixo_npc18
    },
    "direita"  # direção inicial
)

spr_atual_npc18 = npc18.animacoes["direita"][0]

npc18_rect = pygame.Rect(
    npc18.npc_x,
    npc18.npc_y,
    spr_atual_npc18.get_width(),
    spr_atual_npc18.get_height()
)