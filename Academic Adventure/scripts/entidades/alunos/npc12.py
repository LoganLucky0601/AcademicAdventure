import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc12 = [
    pygame.image.load("assets/sprites/alunos/npc12/top1.png"),
    pygame.image.load("assets/sprites/alunos/npc12/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc12/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc12/top4.png")
]

spr_baixo_npc12 = [
    pygame.image.load("assets/sprites/alunos/npc12/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc12/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc12/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc12/bottom4.png")
]

spr_esquerda_npc12 = [
    pygame.image.load("assets/sprites/alunos/npc12/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc12/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc12/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc12/left4.png")
]

spr_direita_npc12 = [
    pygame.image.load("assets/sprites/alunos/npc12/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc12/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc12/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc12/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc12 = NPC(
    1200,  # npc_x
    320,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    1760,  # limite_direita
    {
        "direita": spr_direita_npc12,
        "esquerda": spr_esquerda_npc12,
        "cima": spr_cima_npc12,
        "baixo": spr_baixo_npc12
    },
    "direita"  # direção inicial
)

spr_atual_npc12 = npc12.animacoes["direita"][0]

npc12_rect = pygame.Rect(
    npc12.npc_x, 
    npc12.npc_y, 
    spr_atual_npc12.get_width(), 
    spr_atual_npc12.get_height()
)