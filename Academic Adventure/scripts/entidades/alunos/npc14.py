import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc14 = [
    pygame.image.load("assets/sprites/alunos/npc14/top1.png"),
    pygame.image.load("assets/sprites/alunos/npc14/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc14/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc14/top4.png")
]

spr_baixo_npc14 = [
    pygame.image.load("assets/sprites/alunos/npc14/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc14/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc14/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc14/bottom4.png")
]

spr_esquerda_npc14 = [
    pygame.image.load("assets/sprites/alunos/npc14/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc14/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc14/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc14/left4.png")
]

spr_direita_npc14 = [
    pygame.image.load("assets/sprites/alunos/npc14/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc14/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc14/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc14/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc14 = NPC(
    7000,  # npc_x
    650,  # npc_y
    1,  # velocidade
    865,  # limite_esquerda
    99999999,  # limite_direita
    {
        "direita": spr_direita_npc14,
        "esquerda": spr_esquerda_npc14,
        "cima": spr_cima_npc14,
        "baixo": spr_baixo_npc14
    },
    "esquerda"  # direção inicial
)

spr_atual_npc14 = npc14.animacoes["esquerda"][0]

npc14_rect = pygame.Rect(
    npc14.npc_x, 
    npc14.npc_y, 
    spr_atual_npc14.get_width(), 
    spr_atual_npc14.get_height()
)