import pygame
from scripts.npc import NPC

# Carrega os sprites do NPC
spr_cima_faxineira = [
    pygame.image.load("assets/sprites/funcionarios/faxineira/left1.png"),
    pygame.image.load("assets/sprites/funcionarios/faxineira/left2.png"),
    pygame.image.load("assets/sprites/funcionarios/faxineira/left3.png"),
    pygame.image.load("assets/sprites/funcionarios/faxineira/left4.png")
]

spr_baixo_faxineira = [
    pygame.image.load("assets/sprites/funcionarios/faxineira/left1.png"),
    pygame.image.load("assets/sprites/funcionarios/faxineira/left1.png"),
    pygame.image.load("assets/sprites/funcionarios/faxineira/left1.png"),
    pygame.image.load("assets/sprites/funcionarios/faxineira/left1.png")
]

spr_esquerda_faxineira = [
    pygame.image.load("assets/sprites/funcionarios/faxineira/left1.png"),
    pygame.image.load("assets/sprites/funcionarios/faxineira/left2.png"),
    pygame.image.load("assets/sprites/funcionarios/faxineira/left3.png"),
    pygame.image.load("assets/sprites/funcionarios/faxineira/left4.png")
]

spr_direita_faxineira = [
    pygame.image.load("assets/sprites/funcionarios/faxineira/right1.png"),
    pygame.image.load("assets/sprites/funcionarios/faxineira/right2.png"),
    pygame.image.load("assets/sprites/funcionarios/faxineira/right3.png"),
    pygame.image.load("assets/sprites/funcionarios/faxineira/right4.png")
]

spr_idle_faxineira = [
    pygame.image.load("assets/sprites/funcionarios/faxineira/left1.png"),
    pygame.image.load("assets/sprites/funcionarios/faxineira/left1.png"),
    pygame.image.load("assets/sprites/funcionarios/faxineira/left1.png"),
    pygame.image.load("assets/sprites/funcionarios/faxineira/left1.png"),
]

# Crie uma instância do NPC usando a classe NPC
faxineira = NPC(
    1420,  # npc_x
    420,  # npc_y
    1,  # velocidade
    -600,  # limite_esquerda
    2600,  # limite_direita
    {
        "direita": spr_direita_faxineira,
        "esquerda": spr_esquerda_faxineira,
        "cima": spr_cima_faxineira,
        "baixo": spr_baixo_faxineira,
        "idle": spr_idle_faxineira
    },
    "esquerda"  # direção inicial
)
spr_atual_faxineira = faxineira.animacoes["idle"][2]

faxineira_rect = pygame.Rect(
    faxineira.npc_x, 
    faxineira.npc_y, 
    spr_atual_faxineira.get_width(), 
    spr_atual_faxineira.get_height()
)
