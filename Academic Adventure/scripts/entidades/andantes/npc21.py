import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc21 = [
    pygame.image.load("assets/sprites/andantes/npc21/top1.png"),
    pygame.image.load("assets/sprites/andantes/npc21/top2.png"),
    pygame.image.load("assets/sprites/andantes/npc21/top3.png"),
    pygame.image.load("assets/sprites/andantes/npc21/top4.png")
]

spr_baixo_npc21 = [
    pygame.image.load("assets/sprites/andantes/npc21/bottom1.png"),
    pygame.image.load("assets/sprites/andantes/npc21/bottom2.png"),
    pygame.image.load("assets/sprites/andantes/npc21/bottom3.png"),
    pygame.image.load("assets/sprites/andantes/npc21/bottom4.png")
]

spr_esquerda_npc21 = [
    pygame.image.load("assets/sprites/andantes/npc21/left1.png"),
    pygame.image.load("assets/sprites/andantes/npc21/left2.png"),
    pygame.image.load("assets/sprites/andantes/npc21/left3.png"),
    pygame.image.load("assets/sprites/andantes/npc21/left4.png")
]

spr_direita_npc21 = [
    pygame.image.load("assets/sprites/andantes/npc21/right1.png"),
    pygame.image.load("assets/sprites/andantes/npc21/right2.png"),
    pygame.image.load("assets/sprites/andantes/npc21/right3.png"),
    pygame.image.load("assets/sprites/andantes/npc21/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc21 = NPC(
    -17000,  # npc_x
    650,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc21,
        "esquerda": spr_esquerda_npc21,
        "cima": spr_cima_npc21,
        "baixo": spr_baixo_npc21
    },
    "direita"  # direção inicial
)

spr_atual_npc21 = npc21.animacoes["direita"][0]

npc21_rect = pygame.Rect(
    npc21.npc_x,
    npc21.npc_y,
    spr_atual_npc21.get_width(),
    spr_atual_npc21.get_height()
)