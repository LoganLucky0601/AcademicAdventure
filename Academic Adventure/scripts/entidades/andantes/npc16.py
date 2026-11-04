import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc16 = [
    pygame.image.load("assets/sprites/andantes/npc16/top1.png"),
    pygame.image.load("assets/sprites/andantes/npc16/top2.png"),
    pygame.image.load("assets/sprites/andantes/npc16/top3.png"),
    pygame.image.load("assets/sprites/andantes/npc16/top4.png")
]

spr_baixo_npc16 = [
    pygame.image.load("assets/sprites/andantes/npc16/bottom1.png"),
    pygame.image.load("assets/sprites/andantes/npc16/bottom2.png"),
    pygame.image.load("assets/sprites/andantes/npc16/bottom3.png"),
    pygame.image.load("assets/sprites/andantes/npc16/bottom4.png")
]

spr_esquerda_npc16 = [
    pygame.image.load("assets/sprites/andantes/npc16/left1.png"),
    pygame.image.load("assets/sprites/andantes/npc16/left2.png"),
    pygame.image.load("assets/sprites/andantes/npc16/left3.png"),
    pygame.image.load("assets/sprites/andantes/npc16/left4.png")
]

spr_direita_npc16 = [
    pygame.image.load("assets/sprites/andantes/npc16/right1.png"),
    pygame.image.load("assets/sprites/andantes/npc16/right2.png"),
    pygame.image.load("assets/sprites/andantes/npc16/right3.png"),
    pygame.image.load("assets/sprites/andantes/npc16/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc16 = NPC(
    8500,  # npc_x
    630,  # npc_y
    1,  # velocidade
    -9999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc16,
        "esquerda": spr_esquerda_npc16,
        "cima": spr_cima_npc16,
        "baixo": spr_baixo_npc16
    },
    "esquerda"  # direção inicial
)

spr_atual_npc16 = npc16.animacoes["esquerda"][0]

npc16_rect = pygame.Rect(
    npc16.npc_x,
    npc16.npc_y,
    spr_atual_npc16.get_width(),
    spr_atual_npc16.get_height()
)