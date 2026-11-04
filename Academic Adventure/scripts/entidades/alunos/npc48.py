import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc48 = [
    pygame.image.load("assets/sprites/alunos/npc48/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc48/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc48/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc48/top4.png")
]

spr_baixo_npc48 = [
    pygame.image.load("assets/sprites/alunos/npc48/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc48/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc48/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc48/bottom4.png")
]

spr_esquerda_npc48 = [
    pygame.image.load("assets/sprites/alunos/npc48/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc48/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc48/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc48/left4.png")
]

spr_direita_npc48 = [
    pygame.image.load("assets/sprites/alunos/npc48/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc48/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc48/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc48/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc48 = NPC(
    690,  # npc_x
    665,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc48,
        "esquerda": spr_esquerda_npc48,
        "cima": spr_cima_npc48,
        "baixo": spr_baixo_npc48
    },
    "cima"  # direção inicial
)

spr_atual_npc48 = npc48.animacoes["cima"][0]

npc48_rect = pygame.Rect(
    npc48.npc_x, 
    npc48.npc_y, 
    spr_atual_npc48.get_width(), 
    spr_atual_npc48.get_height()
)