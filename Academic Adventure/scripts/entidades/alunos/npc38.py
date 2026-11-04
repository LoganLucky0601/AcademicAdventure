import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc38 = [
    pygame.image.load("assets/sprites/alunos/npc38/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc38/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc38/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc38/top4.png")
]

spr_baixo_npc38 = [
    pygame.image.load("assets/sprites/alunos/npc38/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc38/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc38/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc38/bottom4.png")
]

spr_esquerda_npc38 = [
    pygame.image.load("assets/sprites/alunos/npc38/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc38/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc38/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc38/left4.png")
]

spr_direita_npc38 = [
    pygame.image.load("assets/sprites/alunos/npc38/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc38/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc38/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc38/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc38 = NPC(
    1095,  # npc_x
    460,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc38,
        "esquerda": spr_esquerda_npc38,
        "cima": spr_cima_npc38,
        "baixo": spr_baixo_npc38
    },
    "cima"  # direção inicial
)

spr_atual_npc38 = npc38.animacoes["cima"][0]

npc38_rect = pygame.Rect(
    npc38.npc_x, 
    npc38.npc_y, 
    spr_atual_npc38.get_width(), 
    spr_atual_npc38.get_height()
)