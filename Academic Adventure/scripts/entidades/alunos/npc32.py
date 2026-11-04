import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc32 = [
    pygame.image.load("assets/sprites/alunos/npc32/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc32/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc32/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc32/top4.png")
]

spr_baixo_npc32 = [
    pygame.image.load("assets/sprites/alunos/npc32/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc32/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc32/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc32/top4.png")
]

spr_esquerda_npc32 = [
    pygame.image.load("assets/sprites/alunos/npc32/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc32/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc32/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc32/top4.png")
]

spr_direita_npc32 = [
    pygame.image.load("assets/sprites/alunos/npc32/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc32/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc32/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc32/top4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc32 = NPC(
    1100,  # npc_x
    340,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc32,
        "esquerda": spr_esquerda_npc32,
        "cima": spr_cima_npc32,
        "baixo": spr_baixo_npc32
    },
    "cima"  # direção inicial
)

spr_atual_npc32 = npc32.animacoes["cima"][0]

npc32_rect = pygame.Rect(
    npc32.npc_x, 
    npc32.npc_y, 
    spr_atual_npc32.get_width(), 
    spr_atual_npc32.get_height()
)