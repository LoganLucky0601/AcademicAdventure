import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc3 = [
    pygame.image.load("assets/sprites/professores/npc3/top1.png"),
    pygame.image.load("assets/sprites/professores/npc3/top2.png"),
    pygame.image.load("assets/sprites/professores/npc3/top3.png"),
    pygame.image.load("assets/sprites/professores/npc3/top4.png")
]

spr_baixo_npc3 = [
    pygame.image.load("assets/sprites/professores/npc3/bottom1.png"),
    pygame.image.load("assets/sprites/professores/npc3/bottom2.png"),
    pygame.image.load("assets/sprites/professores/npc3/bottom3.png"),
    pygame.image.load("assets/sprites/professores/npc3/bottom4.png")
]

spr_esquerda_npc3 = [
    pygame.image.load("assets/sprites/professores/npc3/left1.png"),
    pygame.image.load("assets/sprites/professores/npc3/left2.png"),
    pygame.image.load("assets/sprites/professores/npc3/left3.png"),
    pygame.image.load("assets/sprites/professores/npc3/left4.png")
]

spr_direita_npc3 = [
    pygame.image.load("assets/sprites/professores/npc3/right1.png"),
    pygame.image.load("assets/sprites/professores/npc3/right2.png"),
    pygame.image.load("assets/sprites/professores/npc3/right3.png"),
    pygame.image.load("assets/sprites/professores/npc3/right4.png")
]

# Crie uma instância do NPC usando a classe Npc
npc3 = NPC(
    850,  # npc_x
    520,  # npc_y
    1,  # velocidade
    9999999999,  # limite_direita
    999999999,  # limite_esquerda
    {
        "cima": spr_cima_npc3,
        "baixo": spr_baixo_npc3,
        "esquerda": spr_esquerda_npc3,
        "direita": spr_direita_npc3
    },
    "cima"  # direção inicial
)

spr_atual_npc3 = npc3.animacoes["cima"][0]

npc3_rect = pygame.Rect(
    npc3.npc_x,
    npc3.npc_y,
    spr_atual_npc3.get_width(),
    spr_atual_npc3.get_height()
)