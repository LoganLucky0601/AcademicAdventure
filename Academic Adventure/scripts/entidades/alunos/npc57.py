import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc57 = [
    pygame.image.load("assets/sprites/alunos/npc57/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc57/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc57/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc57/top4.png")
]

spr_baixo_npc57 = [
    pygame.image.load("assets/sprites/alunos/npc57/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc57/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc57/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc57/bottom4.png")
]

spr_esquerda_npc57 = [
    pygame.image.load("assets/sprites/alunos/npc57/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc57/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc57/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc57/left4.png")
]

spr_direita_npc57 = [
    pygame.image.load("assets/sprites/alunos/npc57/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc57/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc57/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc57/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc57 = NPC(
    695,  # npc_x
    450,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc57,
        "esquerda": spr_esquerda_npc57,
        "cima": spr_cima_npc57,
        "baixo": spr_baixo_npc57
    },
    "cima"  # direção inicial
)

spr_atual_npc57 = npc57.animacoes["cima"][0]

npc57_rect = pygame.Rect(
    npc57.npc_x, 
    npc57.npc_y, 
    spr_atual_npc57.get_width(), 
    spr_atual_npc57.get_height()
)