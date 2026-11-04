import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc81 = [
    pygame.image.load("assets/sprites/alunos/npc81/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc81/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc81/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc81/top4.png")
]

spr_baixo_npc81 = [
    pygame.image.load("assets/sprites/alunos/npc81/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc81/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc81/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc81/bottom4.png")
]

spr_esquerda_npc81 = [
    pygame.image.load("assets/sprites/alunos/npc81/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc81/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc81/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc81/left4.png")
]

spr_direita_npc81 = [
    pygame.image.load("assets/sprites/alunos/npc81/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc81/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc81/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc81/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc81 = NPC(
    685,  # npc_x
    660,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc81,
        "esquerda": spr_esquerda_npc81,
        "cima": spr_cima_npc81,
        "baixo": spr_baixo_npc81
    },
    "cima"  # direção inicial
)

spr_atual_npc81 = npc81.animacoes["cima"][0]

npc81_rect = pygame.Rect(
    npc81.npc_x, 
    npc81.npc_y, 
    spr_atual_npc81.get_width(), 
    spr_atual_npc81.get_height()
)