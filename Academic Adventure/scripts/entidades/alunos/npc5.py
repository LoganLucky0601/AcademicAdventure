import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc5 = [
    pygame.image.load("assets/sprites/alunos/npc5/top1.png"),
    pygame.image.load("assets/sprites/alunos/npc5/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc5/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc5/top4.png")
]

spr_baixo_npc5 = [
    pygame.image.load("assets/sprites/alunos/npc5/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc5/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc5/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc5/bottom4.png")
]

spr_esquerda_npc5 = [
    pygame.image.load("assets/sprites/alunos/npc5/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc5/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc5/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc5/left4.png")
]

spr_direita_npc5 = [
    pygame.image.load("assets/sprites/alunos/npc5/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc5/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc5/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc5/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc5 = NPC(
    6000,  # npc_x
    650,  # npc_y
    1,  # velocidade
    865,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc5,
        "esquerda": spr_esquerda_npc5,
        "cima": spr_cima_npc5,
        "baixo": spr_baixo_npc5
    },
    "esquerda"  # direção inicial
)

spr_atual_npc5 = npc5.animacoes["esquerda"][0]

npc5_rect = pygame.Rect(
    npc5.npc_x, 
    npc5.npc_y, 
    spr_atual_npc5.get_width(), 
    spr_atual_npc5.get_height()
)