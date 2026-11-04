import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc17 = [
    pygame.image.load("assets/sprites/alunos/npc17/top1.png"),
    pygame.image.load("assets/sprites/alunos/npc17/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc17/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc17/top4.png")
]

spr_baixo_npc17 = [
    pygame.image.load("assets/sprites/alunos/npc17/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc17/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc17/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc17/bottom4.png")
]

spr_esquerda_npc17 = [
    pygame.image.load("assets/sprites/alunos/npc17/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc17/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc17/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc17/left4.png")
]

spr_direita_npc17 = [
    pygame.image.load("assets/sprites/alunos/npc17/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc17/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc17/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc17/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc17 = NPC(
    13000,  # npc_x
    690,  # npc_y
    1,  # velocidade
   865 ,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc17,
        "esquerda": spr_esquerda_npc17,
        "cima": spr_cima_npc17,
        "baixo": spr_baixo_npc17
    },
    "esquerda"  # direção inicial
)

spr_atual_npc17 = npc17.animacoes["esquerda"][0]

npc17_rect = pygame.Rect(
    npc17.npc_x, 
    npc17.npc_y, 
    spr_atual_npc17.get_width(), 
    spr_atual_npc17.get_height()
)