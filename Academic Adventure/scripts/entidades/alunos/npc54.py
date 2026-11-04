import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc54 = [
    pygame.image.load("assets/sprites/alunos/npc54/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc54/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc54/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc54/top4.png")
]

spr_baixo_npc54 = [
    pygame.image.load("assets/sprites/alunos/npc54/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc54/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc54/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc54/bottom4.png")
]

spr_esquerda_npc54 = [
    pygame.image.load("assets/sprites/alunos/npc54/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc54/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc54/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc54/left4.png")
]

spr_direita_npc54 = [
    pygame.image.load("assets/sprites/alunos/npc54/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc54/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc54/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc54/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc54 = NPC(
    1300,  # npc_x
    340,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc54,
        "esquerda": spr_esquerda_npc54,
        "cima": spr_cima_npc54,
        "baixo": spr_baixo_npc54
    },
    "cima"  # direção inicial
)

spr_atual_npc54 = npc54.animacoes["cima"][0]

npc54_rect = pygame.Rect(
    npc54.npc_x, 
    npc54.npc_y, 
    spr_atual_npc54.get_width(), 
    spr_atual_npc54.get_height()
)