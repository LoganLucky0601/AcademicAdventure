import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc44 = [
    pygame.image.load("assets/sprites/alunos/npc44/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc44/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc44/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc44/top4.png")
]

spr_baixo_npc44 = [
    pygame.image.load("assets/sprites/alunos/npc44/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc44/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc44/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc44/bottom4.png")
]

spr_esquerda_npc44 = [
    pygame.image.load("assets/sprites/alunos/npc44/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc44/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc44/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc44/left4.png")
]

spr_direita_npc44 = [
    pygame.image.load("assets/sprites/alunos/npc44/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc44/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc44/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc44/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc44 = NPC(
    1300,  # npc_x
    665,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc44,
        "esquerda": spr_esquerda_npc44,
        "cima": spr_cima_npc44,
        "baixo": spr_baixo_npc44
    },
    "cima"  # direção inicial
)

spr_atual_npc44 = npc44.animacoes["cima"][0]

npc44_rect = pygame.Rect(
    npc44.npc_x, 
    npc44.npc_y, 
    spr_atual_npc44.get_width(), 
    spr_atual_npc44.get_height()
)