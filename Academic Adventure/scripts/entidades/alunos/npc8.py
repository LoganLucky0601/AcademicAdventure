import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc8 = [
    pygame.image.load("assets/sprites/alunos/npc8/top1.png"),
    pygame.image.load("assets/sprites/alunos/npc8/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc8/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc8/top4.png")
]

spr_baixo_npc8 = [
    pygame.image.load("assets/sprites/alunos/npc8/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc8/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc8/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc8/bottom4.png")
]

spr_esquerda_npc8 = [
    pygame.image.load("assets/sprites/alunos/npc8/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc8/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc8/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc8/left4.png")
]

spr_direita_npc8 = [
    pygame.image.load("assets/sprites/alunos/npc8/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc8/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc8/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc8/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc8 = NPC(
    -2800,  # npc_x
    610,  # npc_y
    1,  # velocidade
    -1500,  # limite_esquerda
    845,  # limite_direita
    {
        "direita": spr_direita_npc8,
        "esquerda": spr_esquerda_npc8,
        "cima": spr_cima_npc8,
        "baixo": spr_baixo_npc8
    },
    "direita"  # direção inicial
)

spr_atual_npc8 = npc8.animacoes["direita"][0]

npc8_rect = pygame.Rect(
    npc8.npc_x, 
    npc8.npc_y, 
    spr_atual_npc8.get_width(), 
    spr_atual_npc8.get_height()
)