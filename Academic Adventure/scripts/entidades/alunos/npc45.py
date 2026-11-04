import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc45 = [
    pygame.image.load("assets/sprites/alunos/npc45/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc45/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc45/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc45/top4.png")
]

spr_baixo_npc45 = [
    pygame.image.load("assets/sprites/alunos/npc45/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc45/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc45/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc45/bottom4.png")
]

spr_esquerda_npc45 = [
    pygame.image.load("assets/sprites/alunos/npc45/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc45/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc45/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc45/left4.png")
]

spr_direita_npc45 = [
    pygame.image.load("assets/sprites/alunos/npc45/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc45/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc45/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc45/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc45 = NPC(
    1095,  # npc_x
    560,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc45,
        "esquerda": spr_esquerda_npc45,
        "cima": spr_cima_npc45,
        "baixo": spr_baixo_npc45
    },
    "cima"  # direção inicial
)

spr_atual_npc45 = npc45.animacoes["cima"][0]

npc45_rect = pygame.Rect(
    npc45.npc_x, 
    npc45.npc_y, 
    spr_atual_npc45.get_width(), 
    spr_atual_npc45.get_height()
)