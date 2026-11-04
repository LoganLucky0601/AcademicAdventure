import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_npc64 = [
    pygame.image.load("assets/sprites/alunos/npc64/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc64/top4.png"),
    pygame.image.load("assets/sprites/alunos/npc64/top3.png"),
    pygame.image.load("assets/sprites/alunos/npc64/top4.png")
]

spr_baixo_npc64 = [
    pygame.image.load("assets/sprites/alunos/npc64/bottom1.png"),
    pygame.image.load("assets/sprites/alunos/npc64/bottom2.png"),
    pygame.image.load("assets/sprites/alunos/npc64/bottom3.png"),
    pygame.image.load("assets/sprites/alunos/npc64/bottom4.png")
]

spr_esquerda_npc64 = [
    pygame.image.load("assets/sprites/alunos/npc64/left1.png"),
    pygame.image.load("assets/sprites/alunos/npc64/left2.png"),
    pygame.image.load("assets/sprites/alunos/npc64/left3.png"),
    pygame.image.load("assets/sprites/alunos/npc64/left4.png")
]

spr_direita_npc64 = [
    pygame.image.load("assets/sprites/alunos/npc64/right1.png"),
    pygame.image.load("assets/sprites/alunos/npc64/right2.png"),
    pygame.image.load("assets/sprites/alunos/npc64/right3.png"),
    pygame.image.load("assets/sprites/alunos/npc64/right4.png")
]

# Crie uma instância do NPC usando a classe NPC
npc64 = NPC(
    475,  # npc_x
    565,  # npc_y
    1,  # velocidade
    -99999,  # limite_esquerda
    99999,  # limite_direita
    {
        "direita": spr_direita_npc64,
        "esquerda": spr_esquerda_npc64,
        "cima": spr_cima_npc64,
        "baixo": spr_baixo_npc64
    },
    "cima"  # direção inicial
)

spr_atual_npc64 = npc64.animacoes["cima"][0]

npc64_rect = pygame.Rect(
    npc64.npc_x, 
    npc64.npc_y, 
    spr_atual_npc64.get_width(), 
    spr_atual_npc64.get_height()
)