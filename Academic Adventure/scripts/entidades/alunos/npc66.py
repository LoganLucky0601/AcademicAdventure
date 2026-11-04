import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc66 = [
    pygame.image.load("assets/sprites/alunos/npc66/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc66/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc66/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc66/top4.png")
]

spr_baixo_npc66 = [
    pygame.image.load("assets/sprites/alunos/npc66/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc66/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc66/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc66/bottom4.png")
]

spr_esquerda_npc66 = [
    pygame.image.load("assets/sprites/alunos/npc66/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc66/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc66/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc66/left4.png")
]

spr_direita_npc66 = [
    pygame.image.load("assets/sprites/alunos/npc66/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc66/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc66/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc66/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc66 = NPC(
    1090,  # npc_x
    560,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc66,
        "esquerda": spr_esquerda_npc66,
        "cima": spr_cima_npc66,
        "baixo": spr_baixo_npc66
    },
    "cima"  # direção inicial
)

spr_atual_npc66 = npc66.animacoes["cima"][0]

npc66_rect = pygame.Rect(
    npc66.npc_x, 
    npc66.npc_y, 
    spr_atual_npc66.get_width(), 
    spr_atual_npc66.get_height()
)