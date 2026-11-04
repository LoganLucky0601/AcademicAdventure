import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc69 = [
    pygame.image.load("assets/sprites/alunos/npc69/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc69/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc69/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc69/top4.png")
]

spr_baixo_npc69 = [
    pygame.image.load("assets/sprites/alunos/npc69/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc69/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc69/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc69/bottom4.png")
]

spr_esquerda_npc69 = [
    pygame.image.load("assets/sprites/alunos/npc69/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc69/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc69/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc69/left4.png")
]

spr_direita_npc69 = [
    pygame.image.load("assets/sprites/alunos/npc69/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc69/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc69/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc69/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc69 = NPC(
    685,  # npc_x
    660,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc69,
        "esquerda": spr_esquerda_npc69,
        "cima": spr_cima_npc69,
        "baixo": spr_baixo_npc69
    },
    "cima"  # direção inicial
)

spr_atual_npc69 = npc69.animacoes["cima"][0]

npc69_rect = pygame.Rect(
    npc69.npc_x, 
    npc69.npc_y, 
    spr_atual_npc69.get_width(), 
    spr_atual_npc69.get_height()
)