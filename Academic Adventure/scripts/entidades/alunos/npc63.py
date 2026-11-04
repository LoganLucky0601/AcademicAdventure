import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc63 = [
    pygame.image.load("assets/sprites/alunos/npc63/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc63/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc63/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc63/top4.png")
]

spr_baixo_npc63 = [
    pygame.image.load("assets/sprites/alunos/npc63/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc63/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc63/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc63/bottom4.png")
]

spr_esquerda_npc63 = [
    pygame.image.load("assets/sprites/alunos/npc63/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc63/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc63/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc63/left4.png")
]

spr_direita_npc63 = [
    pygame.image.load("assets/sprites/alunos/npc63/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc63/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc63/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc63/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc63 = NPC(
    880,  # npc_x
    565,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc63,
        "esquerda": spr_esquerda_npc63,
        "cima": spr_cima_npc63,
        "baixo": spr_baixo_npc63
    },
    "cima"  # direção inicial
)

spr_atual_npc63 = npc63.animacoes["cima"][0]

npc63_rect = pygame.Rect(
    npc63.npc_x, 
    npc63.npc_y, 
    spr_atual_npc63.get_width(), 
    spr_atual_npc63.get_height()
)