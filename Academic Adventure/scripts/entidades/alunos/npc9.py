import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc9 = [
    pygame.image.load("assets/sprites/alunos/npc9/top1.png"),
    pygame.image.load("assets/sprites/alunos/npc9/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc9/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc9/top4.png")
]

spr_baixo_npc9 = [
    pygame.image.load("assets/sprites/alunos/npc9/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc9/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc9/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc9/bottom4.png")
]

spr_esquerda_npc9 = [
    pygame.image.load("assets/sprites/alunos/npc9/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc9/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc9/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc9/left4.png")
]

spr_direita_npc9 = [
    pygame.image.load("assets/sprites/alunos/npc9/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc9/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc9/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc9/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc9 = NPC(
    -2800,  # npc_x
    680,  # npc_y
    1,  # velocidade
    -1500,  # limite_esquerda
    845,  # limite_direita
    {
        "direita": spr_direita_npc9,
        "esquerda": spr_esquerda_npc9,
        "cima": spr_cima_npc9,
        "baixo": spr_baixo_npc9
    },
    "direita"  # direção inicial
)

spr_atual_npc9 = npc9.animacoes["direita"][0]

npc9_rect = pygame.Rect(
    npc9.npc_x, 
    npc9.npc_y, 
    spr_atual_npc9.get_width(), 
    spr_atual_npc9.get_height()
)