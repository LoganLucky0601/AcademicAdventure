import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc30 = [
    pygame.image.load("assets/sprites/alunos/npc30/top1.png"),
    pygame.image.load("assets/sprites/alunos/npc30/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc30/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc30/top4.png")
]

spr_baixo_npc30 = [
    pygame.image.load("assets/sprites/alunos/npc30/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc30/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc30/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc30/bottom4.png")
]

spr_esquerda_npc30 = [
    pygame.image.load("assets/sprites/alunos/npc30/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc30/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc30/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc30/left4.png")
]

spr_direita_npc30 = [
    pygame.image.load("assets/sprites/alunos/npc30/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc30/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc30/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc30/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc30 = NPC(
    490,  # npc_x
    340,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc30,
        "esquerda": spr_esquerda_npc30,
        "cima": spr_cima_npc30,
        "baixo": spr_baixo_npc30
    },
    "cima"  # direção inicial
)

spr_atual_npc30 = npc30.animacoes["cima"][0]

npc30_rect = pygame.Rect(
    npc30.npc_x, 
    npc30.npc_y, 
    spr_atual_npc30.get_width(), 
    spr_atual_npc30.get_height()
)