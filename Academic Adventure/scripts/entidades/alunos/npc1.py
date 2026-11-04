import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc1 = [
    pygame.image.load("assets/sprites/alunos/npc1/top1.png"),
    pygame.image.load("assets/sprites/alunos/npc1/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc1/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc1/top4.png")
]

spr_baixo_npc1 = [
    pygame.image.load("assets/sprites/alunos/npc1/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc1/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc1/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc1/bottom4.png")
]

spr_esquerda_npc1 = [
    pygame.image.load("assets/sprites/alunos/npc1/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc1/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc1/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc1/left4.png")
]

spr_direita_npc1 = [
    pygame.image.load("assets/sprites/alunos/npc1/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc1/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc1/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc1/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc1 = NPC(
    2000,  # npc_x
    650,  # npc_y
    1,  # velocidade
    865,  # limite_esquerda
    999999,  # limite_direita
    {
        "direita": spr_direita_npc1,
        "esquerda": spr_esquerda_npc1,
        "cima": spr_cima_npc1,
        "baixo": spr_baixo_npc1
    },
    "esquerda"  # direção inicial
)

spr_atual_npc1 = npc1.animacoes["esquerda"][0]

npc1_rect = pygame.Rect(
    npc1.npc_x, 
    npc1.npc_y, 
    spr_atual_npc1.get_width(), 
    spr_atual_npc1.get_height()
)
