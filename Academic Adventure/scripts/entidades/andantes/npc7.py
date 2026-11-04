import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc7 = [
    pygame.image.load("assets/sprites/andantes/npc7/top1.png"),
    pygame.image.load("assets/sprites/andantes/npc7/top2.png"),
    pygame.image.load("assets/sprites/andantes/npc7/top3.png"),
    pygame.image.load("assets/sprites/andantes/npc7/top4.png")
]

spr_baixo_npc7 = [
    pygame.image.load("assets/sprites/andantes/npc7/bottom1.png"),
    pygame.image.load("assets/sprites/andantes/npc7/bottom2.png"),
    pygame.image.load("assets/sprites/andantes/npc7/bottom3.png"),
    pygame.image.load("assets/sprites/andantes/npc7/bottom4.png")
]

spr_esquerda_npc7 = [
    pygame.image.load("assets/sprites/andantes/npc7/left1.png"),
    pygame.image.load("assets/sprites/andantes/npc7/left2.png"),
    pygame.image.load("assets/sprites/andantes/npc7/left3.png"),
    pygame.image.load("assets/sprites/andantes/npc7/left4.png")
]

spr_direita_npc7 = [
    pygame.image.load("assets/sprites/andantes/npc7/right1.png"),
    pygame.image.load("assets/sprites/andantes/npc7/right2.png"),
    pygame.image.load("assets/sprites/andantes/npc7/right3.png"),
    pygame.image.load("assets/sprites/andantes/npc7/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc7 = NPC(
    -500,  # npc_x
    690,  # npc_y
    1,  # velocidade
    -900,  # limite_esquerda
    -999999,  # limite_direita
    {
        "direita": spr_direita_npc7,
        "esquerda": spr_esquerda_npc7,
        "cima": spr_cima_npc7,
        "baixo": spr_baixo_npc7
    },
    "direita"  # direção inicial
)

spr_atual_npc7 = npc7.animacoes["direita"][0]

npc7_rect = pygame.Rect(
    npc7.npc_x,
    npc7.npc_y,
    spr_atual_npc7.get_width(),
    spr_atual_npc7.get_height()
)