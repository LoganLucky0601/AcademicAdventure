import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc46 = [
    pygame.image.load("assets/sprites/alunos/npc46/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc46/top2.png"),
    pygame.image.load("assets/sprites/alunos/npc46/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc46/top4.png")
]

spr_baixo_npc46 = [
    pygame.image.load("assets/sprites/alunos/npc46/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc46/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc46/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc46/bottom4.png")
]

spr_esquerda_npc46 = [
    pygame.image.load("assets/sprites/alunos/npc46/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc46/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc46/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc46/left4.png")
]

spr_direita_npc46 = [
    pygame.image.load("assets/sprites/alunos/npc46/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc46/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc46/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc46/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc46 = NPC(
    495,  # npc_x
    665,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc46,
        "esquerda": spr_esquerda_npc46,
        "cima": spr_cima_npc46,
        "baixo": spr_baixo_npc46
    },
    "cima"  # direção inicial
)

spr_atual_npc46 = npc46.animacoes["cima"][0]

npc46_rect = pygame.Rect(
    npc46.npc_x, 
    npc46.npc_y, 
    spr_atual_npc46.get_width(), 
    spr_atual_npc46.get_height()
)