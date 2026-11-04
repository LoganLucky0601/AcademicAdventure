import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc72 = [
    pygame.image.load("assets/sprites/alunos/npc72/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc72/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc72/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc72/top4.png")
]

spr_baixo_npc72 = [
    pygame.image.load("assets/sprites/alunos/npc72/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc72/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc72/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc72/bottom4.png")
]

spr_esquerda_npc72 = [
    pygame.image.load("assets/sprites/alunos/npc72/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc72/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc72/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc72/left4.png")
]

spr_direita_npc72 = [
    pygame.image.load("assets/sprites/alunos/npc72/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc72/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc72/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc72/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc72 = NPC(
    685,  # npc_x
    660,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc72,
        "esquerda": spr_esquerda_npc72,
        "cima": spr_cima_npc72,
        "baixo": spr_baixo_npc72
    },
    "cima"  # direção inicial
)

spr_atual_npc72 = npc72.animacoes["cima"][0]

npc72_rect = pygame.Rect(
    npc72.npc_x, 
    npc72.npc_y, 
    spr_atual_npc72.get_width(), 
    spr_atual_npc72.get_height()
)