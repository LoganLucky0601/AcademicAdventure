import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc22 = [
    pygame.image.load("assets/sprites/alunos/npc22/top1.png"),
    pygame.image.load("assets/sprites/alunos/npc22/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc22/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc22/top4.png")
]

spr_baixo_npc22 = [
    pygame.image.load("assets/sprites/alunos/npc22/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc22/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc22/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc22/bottom4.png")
]

spr_esquerda_npc22 = [
    pygame.image.load("assets/sprites/alunos/npc22/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc22/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc22/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc22/left4.png")
]

spr_direita_npc22 = [
    pygame.image.load("assets/sprites/alunos/npc22/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc22/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc22/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc22/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc22 = NPC(
    -20000,  # npc_x
    650,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc22,
        "esquerda": spr_esquerda_npc22,
        "cima": spr_cima_npc22,
        "baixo": spr_baixo_npc22
    },
    "direita"  # direção inicial
)

spr_atual_npc22 = npc22.animacoes["direita"][0]

npc22_rect = pygame.Rect(
    npc22.npc_x, 
    npc22.npc_y, 
    spr_atual_npc22.get_width(), 
    spr_atual_npc22.get_height()
)