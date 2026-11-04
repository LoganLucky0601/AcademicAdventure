import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc41 = [
    pygame.image.load("assets/sprites/alunos/npc41/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc41/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc41/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc41/top4.png")
]

spr_baixo_npc41 = [
    pygame.image.load("assets/sprites/alunos/npc41/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc41/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc41/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc41/bottom4.png")
]

spr_esquerda_npc41 = [
    pygame.image.load("assets/sprites/alunos/npc41/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc41/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc41/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc41/left4.png")
]

spr_direita_npc41 = [
    pygame.image.load("assets/sprites/alunos/npc41/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc41/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc41/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc41/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc41 = NPC(
    690,  # npc_x
    560,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc41,
        "esquerda": spr_esquerda_npc41,
        "cima": spr_cima_npc41,
        "baixo": spr_baixo_npc41
    },
    "cima"  # direção inicial
)

spr_atual_npc41 = npc41.animacoes["cima"][0]

npc41_rect = pygame.Rect(
    npc41.npc_x, 
    npc41.npc_y, 
    spr_atual_npc41.get_width(), 
    spr_atual_npc41.get_height()
)