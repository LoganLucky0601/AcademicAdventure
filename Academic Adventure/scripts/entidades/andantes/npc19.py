import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc19 = [
    pygame.image.load("assets/sprites/andantes/npc19/top1.png"),
    pygame.image.load("assets/sprites/andantes/npc19/top2.png"),
    pygame.image.load("assets/sprites/andantes/npc19/top3.png"),
    pygame.image.load("assets/sprites/andantes/npc19/top4.png")
]

spr_baixo_npc19 = [
    pygame.image.load("assets/sprites/andantes/npc19/bottom1.png"),
    pygame.image.load("assets/sprites/andantes/npc19/bottom2.png"),
    pygame.image.load("assets/sprites/andantes/npc19/bottom3.png"),
    pygame.image.load("assets/sprites/andantes/npc19/bottom4.png")
]

spr_esquerda_npc19 = [
    pygame.image.load("assets/sprites/andantes/npc19/left1.png"),
    pygame.image.load("assets/sprites/andantes/npc19/left2.png"),
    pygame.image.load("assets/sprites/andantes/npc19/left3.png"),
    pygame.image.load("assets/sprites/andantes/npc19/left4.png")
]

spr_direita_npc19 = [
    pygame.image.load("assets/sprites/andantes/npc19/right1.png"),
    pygame.image.load("assets/sprites/andantes/npc19/right2.png"),
    pygame.image.load("assets/sprites/andantes/npc19/right3.png"),
    pygame.image.load("assets/sprites/andantes/npc19/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc19 = NPC(
    -15000,  # npc_x
    650,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc19,
        "esquerda": spr_esquerda_npc19,
        "cima": spr_cima_npc19,
        "baixo": spr_baixo_npc19
    },
    "direita"  # direção inicial
)

spr_atual_npc19 = npc19.animacoes["direita"][0]

npc19_rect = pygame.Rect(
    npc19.npc_x,
    npc19.npc_y,
    spr_atual_npc19.get_width(),
    spr_atual_npc19.get_height()
)