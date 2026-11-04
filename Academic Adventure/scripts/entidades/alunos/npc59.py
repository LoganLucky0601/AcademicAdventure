import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc59 = [
    pygame.image.load("assets/sprites/alunos/npc59/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc59/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc59/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc59/top4.png")
]

spr_baixo_npc59 = [
    pygame.image.load("assets/sprites/alunos/npc59/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc59/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc59/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc59/bottom4.png")
]

spr_esquerda_npc59 = [
    pygame.image.load("assets/sprites/alunos/npc59/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc59/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc59/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc59/left4.png")
]

spr_direita_npc59 = [
    pygame.image.load("assets/sprites/alunos/npc59/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc59/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc59/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc59/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc59 = NPC(
    1095,  # npc_x
    450,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc59,
        "esquerda": spr_esquerda_npc59,
        "cima": spr_cima_npc59,
        "baixo": spr_baixo_npc59
    },
    "cima"  # direção inicial
)

spr_atual_npc59 = npc59.animacoes["cima"][0]

npc59_rect = pygame.Rect(
    npc59.npc_x, 
    npc59.npc_y, 
    spr_atual_npc59.get_width(), 
    spr_atual_npc59.get_height()
)