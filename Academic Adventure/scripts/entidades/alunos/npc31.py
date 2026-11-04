import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc31 = [
    pygame.image.load("assets/sprites/alunos/npc31/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc31/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc31/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc31/top4.png")
]

spr_baixo_npc31 = [
    pygame.image.load("assets/sprites/alunos/npc31/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc31/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc31/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc31/top4.png")
]

spr_esquerda_npc31 = [
    pygame.image.load("assets/sprites/alunos/npc31/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc31/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc31/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc31/top4.png")
]

spr_direita_npc31 = [
    pygame.image.load("assets/sprites/alunos/npc31/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc31/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc31/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc31/top4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc31 = NPC(
    690,  # npc_x
    340,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc31,
        "esquerda": spr_esquerda_npc31,
        "cima": spr_cima_npc31,
        "baixo": spr_baixo_npc31
    },
    "cima"  # direção inicial
)

spr_atual_npc31 = npc31.animacoes["cima"][0]

npc31_rect = pygame.Rect(
    npc31.npc_x, 
    npc31.npc_y, 
    spr_atual_npc31.get_width(), 
    spr_atual_npc31.get_height()
)