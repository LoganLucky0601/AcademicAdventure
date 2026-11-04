import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc62 = [
    pygame.image.load("assets/sprites/alunos/npc62/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc62/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc62/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc62/top4.png")
]

spr_baixo_npc62 = [
    pygame.image.load("assets/sprites/alunos/npc62/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc62/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc62/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc62/bottom4.png")
]

spr_esquerda_npc62 = [
    pygame.image.load("assets/sprites/alunos/npc62/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc62/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc62/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc62/left4.png")
]

spr_direita_npc62 = [
    pygame.image.load("assets/sprites/alunos/npc62/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc62/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc62/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc62/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc62 = NPC(
    690,  # npc_x
    560,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc62,
        "esquerda": spr_esquerda_npc62,
        "cima": spr_cima_npc62,
        "baixo": spr_baixo_npc62
    },
    "cima"  # direção inicial
)

spr_atual_npc62 = npc62.animacoes["cima"][0]

npc62_rect = pygame.Rect(
    npc62.npc_x, 
    npc62.npc_y, 
    spr_atual_npc62.get_width(), 
    spr_atual_npc62.get_height()
)