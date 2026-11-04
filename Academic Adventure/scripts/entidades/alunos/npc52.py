import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc52 = [
    pygame.image.load("assets/sprites/alunos/npc52/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc52/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc52/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc52/top4.png")
]

spr_baixo_npc52 = [
    pygame.image.load("assets/sprites/alunos/npc52/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc52/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc52/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc52/top4.png")
]

spr_esquerda_npc52 = [
    pygame.image.load("assets/sprites/alunos/npc52/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc52/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc52/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc52/top4.png")
]

spr_direita_npc52 = [
    pygame.image.load("assets/sprites/alunos/npc52/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc52/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc52/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc52/top4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc52 = NPC(
    495,  # npc_x
    340,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc52,
        "esquerda": spr_esquerda_npc52,
        "cima": spr_cima_npc52,
        "baixo": spr_baixo_npc52
    },
    "cima"  # direção inicial
)

spr_atual_npc52 = npc52.animacoes["cima"][0]

npc52_rect = pygame.Rect(
    npc52.npc_x, 
    npc52.npc_y, 
    spr_atual_npc52.get_width(), 
    spr_atual_npc52.get_height()
)