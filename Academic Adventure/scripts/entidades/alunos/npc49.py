import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc49 = [
    pygame.image.load("assets/sprites/alunos/npc49/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc49/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc49/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc49/top4.png")
]

spr_baixo_npc49 = [
    pygame.image.load("assets/sprites/alunos/npc49/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc49/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc49/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc49/bottom4.png")
]

spr_esquerda_npc49 = [
    pygame.image.load("assets/sprites/alunos/npc49/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc49/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc49/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc49/left4.png")
]

spr_direita_npc49 = [
    pygame.image.load("assets/sprites/alunos/npc49/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc49/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc49/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc49/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc49 = NPC(
    895,  # npc_x
    665,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc49,
        "esquerda": spr_esquerda_npc49,
        "cima": spr_cima_npc49,
        "baixo": spr_baixo_npc49
    },
    "cima"  # direção inicial
)

spr_atual_npc49 = npc49.animacoes["cima"][0]

npc49_rect = pygame.Rect(
    npc49.npc_x, 
    npc49.npc_y, 
    spr_atual_npc49.get_width(), 
    spr_atual_npc49.get_height()
)