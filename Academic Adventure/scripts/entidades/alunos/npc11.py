import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc11 = [
    pygame.image.load("assets/sprites/alunos/npc11/top1.png"),
    pygame.image.load("assets/sprites/alunos/npc11/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc11/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc11/top4.png")
]

spr_baixo_npc11 = [
    pygame.image.load("assets/sprites/alunos/npc11/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc11/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc11/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc11/bottom4.png")
]

spr_esquerda_npc11 = [
    pygame.image.load("assets/sprites/alunos/npc11/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc11/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc11/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc11/left4.png")
]

spr_direita_npc11 = [
    pygame.image.load("assets/sprites/alunos/npc11/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc11/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc11/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc11/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc11 = NPC(
    -2130,  # npc_x
    670,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    860,  # limite_direita
    {
        "direita": spr_direita_npc11,
        "esquerda": spr_esquerda_npc11,
        "cima": spr_cima_npc11,
        "baixo": spr_baixo_npc11
    },
    "direita"  # direção inicial
)

spr_atual_npc11 = npc11.animacoes["direita"][0]

npc11_rect = pygame.Rect(
    npc11.npc_x, 
    npc11.npc_y, 
    spr_atual_npc11.get_width(), 
    spr_atual_npc11.get_height()
)