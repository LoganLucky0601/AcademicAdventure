import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc60 = [
    pygame.image.load("assets/sprites/alunos/npc60/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc60/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc60/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc60/top4.png")
]

spr_baixo_npc60 = [
    pygame.image.load("assets/sprites/alunos/npc60/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc60/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc60/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc60/bottom4.png")
]

spr_esquerda_npc60 = [
    pygame.image.load("assets/sprites/alunos/npc60/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc60/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc60/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc60/left4.png")
]

spr_direita_npc60 = [
    pygame.image.load("assets/sprites/alunos/npc60/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc60/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc60/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc60/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc60 = NPC(
    1300,  # npc_x
    445,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc60,
        "esquerda": spr_esquerda_npc60,
        "cima": spr_cima_npc60,
        "baixo": spr_baixo_npc60
    },
    "cima"  # direção inicial
)

spr_atual_npc60 = npc60.animacoes["cima"][0]

npc60_rect = pygame.Rect(
    npc60.npc_x, 
    npc60.npc_y, 
    spr_atual_npc60.get_width(), 
    spr_atual_npc60.get_height()
)