import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc13 = [
    pygame.image.load("assets/sprites/alunos/npc13/top1.png"),
    pygame.image.load("assets/sprites/alunos/npc13/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc13/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc13/top4.png")
]

spr_baixo_npc13 = [
    pygame.image.load("assets/sprites/alunos/npc13/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc13/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc13/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc13/bottom4.png")
]

spr_esquerda_npc13 = [
    pygame.image.load("assets/sprites/alunos/npc13/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc13/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc13/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc13/left4.png")
]

spr_direita_npc13 = [
    pygame.image.load("assets/sprites/alunos/npc13/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc13/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc13/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc13/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc13 = NPC(
    1270,  # npc_x
    335,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    1760,  # limite_direita
    {
        "direita": spr_direita_npc13,
        "esquerda": spr_esquerda_npc13,
        "cima": spr_cima_npc13,
        "baixo": spr_baixo_npc13
    },
    "esquerda"  # direção inicial
)

spr_atual_npc13 = npc13.animacoes["esquerda"][0]

npc13_rect = pygame.Rect(
    npc13.npc_x, 
    npc13.npc_y, 
    spr_atual_npc13.get_width(), 
    spr_atual_npc13.get_height()
)