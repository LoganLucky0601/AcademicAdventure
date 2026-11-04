import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc75 = [
    pygame.image.load("assets/sprites/alunos/npc75/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc75/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc75/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc75/top4.png")
]

spr_baixo_npc75 = [
    pygame.image.load("assets/sprites/alunos/npc75/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc75/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc75/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc75/bottom4.png")
]

spr_esquerda_npc75 = [
    pygame.image.load("assets/sprites/alunos/npc75/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc75/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc75/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc75/left4.png")
]

spr_direita_npc75 = [
    pygame.image.load("assets/sprites/alunos/npc75/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc75/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc75/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc75/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc75 = NPC(
    685,  # npc_x
    660,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc75,
        "esquerda": spr_esquerda_npc75,
        "cima": spr_cima_npc75,
        "baixo": spr_baixo_npc75
    },
    "cima"  # direção inicial
)

spr_atual_npc75 = npc75.animacoes["cima"][0]

npc75_rect = pygame.Rect(
    npc75.npc_x, 
    npc75.npc_y, 
    spr_atual_npc75.get_width(), 
    spr_atual_npc75.get_height()
)