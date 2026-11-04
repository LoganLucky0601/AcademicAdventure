import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc50 = [
    pygame.image.load("assets/sprites/alunos/npc50/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc50/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc50/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc50/top4.png")
]

spr_baixo_npc50 = [
    pygame.image.load("assets/sprites/alunos/npc50/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc50/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc50/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc50/bottom4.png")
]

spr_esquerda_npc50 = [
    pygame.image.load("assets/sprites/alunos/npc50/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc50/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc50/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc50/left4.png")
]

spr_direita_npc50 = [
    pygame.image.load("assets/sprites/alunos/npc50/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc50/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc50/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc50/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc50 = NPC(
    895,  # npc_x
    665,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc50,
        "esquerda": spr_esquerda_npc50,
        "cima": spr_cima_npc50,
        "baixo": spr_baixo_npc50
    },
    "cima"  # direção inicial
)

spr_atual_npc50 = npc50.animacoes["cima"][0]

npc50_rect = pygame.Rect(
    npc50.npc_x, 
    npc50.npc_y, 
    spr_atual_npc50.get_width(), 
    spr_atual_npc50.get_height()
)