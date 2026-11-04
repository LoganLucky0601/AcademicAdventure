import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc39 = [
    pygame.image.load("assets/sprites/alunos/npc39/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc39/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc39/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc39/top4.png")
]

spr_baixo_npc39 = [
    pygame.image.load("assets/sprites/alunos/npc39/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc39/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc39/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc39/bottom4.png")
]

spr_esquerda_npc39 = [
    pygame.image.load("assets/sprites/alunos/npc39/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc39/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc39/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc39/left4.png")
]

spr_direita_npc39 = [
    pygame.image.load("assets/sprites/alunos/npc39/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc39/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc39/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc39/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc39 = NPC(
    1300,  # npc_x
    450,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc39,
        "esquerda": spr_esquerda_npc39,
        "cima": spr_cima_npc39,
        "baixo": spr_baixo_npc39
    },
    "cima"  # direção inicial
)

spr_atual_npc39 = npc39.animacoes["cima"][0]

npc39_rect = pygame.Rect(
    npc39.npc_x, 
    npc39.npc_y, 
    spr_atual_npc39.get_width(), 
    spr_atual_npc39.get_height()
)