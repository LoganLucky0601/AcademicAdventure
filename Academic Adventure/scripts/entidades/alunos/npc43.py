import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc43 = [
    pygame.image.load("assets/sprites/alunos/npc43/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc43/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc43/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc43/top4.png")
]

spr_baixo_npc43 = [
    pygame.image.load("assets/sprites/alunos/npc43/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc43/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc43/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc43/bottom4.png")
]

spr_esquerda_npc43 = [
    pygame.image.load("assets/sprites/alunos/npc43/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc43/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc43/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc43/left4.png")
]

spr_direita_npc43 = [
    pygame.image.load("assets/sprites/alunos/npc43/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc43/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc43/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc43/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc43 = NPC(
    895,  # npc_x
    325,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc43,
        "esquerda": spr_esquerda_npc43,
        "cima": spr_cima_npc43,
        "baixo": spr_baixo_npc43
    },
    "cima"  # direção inicial
)

spr_atual_npc43 = npc43.animacoes["cima"][0]

npc43_rect = pygame.Rect(
    npc43.npc_x, 
    npc43.npc_y, 
    spr_atual_npc43.get_width(), 
    spr_atual_npc43.get_height()
)