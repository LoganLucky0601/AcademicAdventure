import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc40 = [
    pygame.image.load("assets/sprites/alunos/npc40/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc40/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc40/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc40/top4.png")
]

spr_baixo_npc40 = [
    pygame.image.load("assets/sprites/alunos/npc40/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc40/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc40/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc40/bottom4.png")
]

spr_esquerda_npc40 = [
    pygame.image.load("assets/sprites/alunos/npc40/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc40/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc40/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc40/left4.png")
]

spr_direita_npc40 = [
    pygame.image.load("assets/sprites/alunos/npc40/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc40/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc40/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc40/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc40 = NPC(
    490,  # npc_x
    560,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc40,
        "esquerda": spr_esquerda_npc40,
        "cima": spr_cima_npc40,
        "baixo": spr_baixo_npc40
    },
    "cima"  # direção inicial
)

spr_atual_npc40 = npc40.animacoes["cima"][0]

npc40_rect = pygame.Rect(
    npc40.npc_x, 
    npc40.npc_y, 
    spr_atual_npc40.get_width(), 
    spr_atual_npc40.get_height()
)