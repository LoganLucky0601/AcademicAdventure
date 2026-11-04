import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc51 = [
    pygame.image.load("assets/sprites/alunos/npc51/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc51/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc51/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc51/top4.png")
]

spr_baixo_npc51 = [
    pygame.image.load("assets/sprites/alunos/npc51/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc51/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc51/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc51/top4.png")
]

spr_esquerda_npc51 = [
    pygame.image.load("assets/sprites/alunos/npc51/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc51/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc51/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc51/top4.png")
]

spr_direita_npc51 = [
    pygame.image.load("assets/sprites/alunos/npc51/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc51/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc51/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc51/top4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc51 = NPC(
    695,  # npc_x
    340,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc51,
        "esquerda": spr_esquerda_npc51,
        "cima": spr_cima_npc51,
        "baixo": spr_baixo_npc51
    },
    "cima"  # direção inicial
)

spr_atual_npc51 = npc51.animacoes["cima"][0]

npc51_rect = pygame.Rect(
    npc51.npc_x, 
    npc51.npc_y, 
    spr_atual_npc51.get_width(), 
    spr_atual_npc51.get_height()
)