import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc55 = [
    pygame.image.load("assets/sprites/alunos/npc55/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc55/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc55/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc55/top4.png")
]

spr_baixo_npc55 = [
    pygame.image.load("assets/sprites/alunos/npc55/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc55/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc55/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc55/bottom4.png")
]

spr_esquerda_npc55 = [
    pygame.image.load("assets/sprites/alunos/npc55/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc55/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc55/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc55/left4.png")
]

spr_direita_npc55 = [
    pygame.image.load("assets/sprites/alunos/npc55/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc55/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc55/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc55/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc55 = NPC(
    495,  # npc_x
    445,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc55,
        "esquerda": spr_esquerda_npc55,
        "cima": spr_cima_npc55,
        "baixo": spr_baixo_npc55
    },
    "cima"  # direção inicial
)

spr_atual_npc55 = npc55.animacoes["cima"][0]

npc55_rect = pygame.Rect(
    npc55.npc_x, 
    npc55.npc_y, 
    spr_atual_npc55.get_width(), 
    spr_atual_npc55.get_height()
)