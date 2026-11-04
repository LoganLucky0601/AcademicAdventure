import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc23 = [
    pygame.image.load("assets/sprites/alunos/npc23/top1.png"),
    pygame.image.load("assets/sprites/alunos/npc23/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc23/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc23/top4.png")
]

spr_baixo_npc23 = [
    pygame.image.load("assets/sprites/alunos/npc23/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc23/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc23/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc23/bottom4.png")
]

spr_esquerda_npc23 = [
    pygame.image.load("assets/sprites/alunos/npc23/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc23/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc23/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc23/left4.png")
]

spr_direita_npc23 = [
    pygame.image.load("assets/sprites/alunos/npc23/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc23/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc23/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc23/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc23 = NPC(
    -23000,  # npc_x
    650,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc23,
        "esquerda": spr_esquerda_npc23,
        "cima": spr_cima_npc23,
        "baixo": spr_baixo_npc23
    },
    "direita"  # direção inicial
)

spr_atual_npc23 = npc23.animacoes["direita"][0]

npc23_rect = pygame.Rect(
    npc23.npc_x, 
    npc23.npc_y, 
    spr_atual_npc23.get_width(), 
    spr_atual_npc23.get_height()
)