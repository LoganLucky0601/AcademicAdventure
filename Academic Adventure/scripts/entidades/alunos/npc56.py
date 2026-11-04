import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc56 = [
    pygame.image.load("assets/sprites/alunos/npc56/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc56/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc56/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc56/top4.png")
]

spr_baixo_npc56 = [
    pygame.image.load("assets/sprites/alunos/npc56/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc56/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc56/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc56/bottom4.png")
]

spr_esquerda_npc56 = [
    pygame.image.load("assets/sprites/alunos/npc56/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc56/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc56/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc56/left4.png")
]

spr_direita_npc56 = [
    pygame.image.load("assets/sprites/alunos/npc56/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc56/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc56/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc56/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc56 = NPC(
    695,  # npc_x
    450,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc56,
        "esquerda": spr_esquerda_npc56,
        "cima": spr_cima_npc56,
        "baixo": spr_baixo_npc56
    },
    "cima"  # direção inicial
)

spr_atual_npc56 = npc56.animacoes["cima"][0]

npc56_rect = pygame.Rect(
    npc56.npc_x, 
    npc56.npc_y, 
    spr_atual_npc56.get_width(), 
    spr_atual_npc56.get_height()
)