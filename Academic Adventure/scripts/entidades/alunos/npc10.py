import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc10 = [
    pygame.image.load("assets/sprites/alunos/npc10/top1.png"),
    pygame.image.load("assets/sprites/alunos/npc10/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc10/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc10/top4.png")
]

spr_baixo_npc10 = [
    pygame.image.load("assets/sprites/alunos/npc10/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc10/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc10/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc10/bottom4.png")
]

spr_esquerda_npc10 = [
    pygame.image.load("assets/sprites/alunos/npc10/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc10/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc10/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc10/left4.png")
]

spr_direita_npc10 = [
    pygame.image.load("assets/sprites/alunos/npc10/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc10/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc10/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc10/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc10 = NPC(
    -2100,  # npc_x
    630,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    860,  # limite_direita
    {
        "direita": spr_direita_npc10,
        "esquerda": spr_esquerda_npc10,
        "cima": spr_cima_npc10,
        "baixo": spr_baixo_npc10
    },
    "direita"  # direção inicial
)

spr_atual_npc10 = npc10.animacoes["direita"][0]

npc10_rect = pygame.Rect(
    npc10.npc_x, 
    npc10.npc_y, 
    spr_atual_npc10.get_width(), 
    spr_atual_npc10.get_height()
)