import pygame

# scene 6: Sala de Informática
sala_informatica1 = pygame.image.load("assets/img/scenes/informatica/sala_informatica.jpg")
sala_informatica_vazia = pygame.image.load("assets/img/scenes/informatica/sala_informatica_vazia.jpg")
parede_sala_informatica = pygame.image.load("assets/img/scenes/informatica/parede_sala_informatica.png")

# HITBOXES
hitboxes_informatica1 = [
    pygame.Rect(345, 205, 1260, 1),   # parede superior
    pygame.Rect(320, 995, 1261, 1),   # parede inferior
    pygame.Rect(1559, 151, 1, 845),   # parede direita
    pygame.Rect(342, 151, 1, 845),   # parede esquerda
    
    # Mesa (esquerda para direita)
    pygame.Rect(349, 364, 95, 600),   # mesa 1
    pygame.Rect(855, 406, 185, 600),   # mesa 2 e 3
    pygame.Rect(1467, 365, 103, 600),   # mesa 4
    
    pygame.Rect(520, 248, 60, 59),   # mesa professor
    pygame.Rect(461, 251, 40, 40),   # cadeira professor
    
    # Armário
    pygame.Rect(347, 284, 45, 62),   # armário cinza
    
    # Fila de cadeiras
    pygame.Rect(463, 386, 35, 505),   # 1
    pygame.Rect(785, 450, 35, 452),   # 2
    pygame.Rect(1063, 405, 35, 470),   # 3
    pygame.Rect(1400, 350, 35, 535),   # 4
    
    # Professor
    #pygame.Rect(750, 205, 65, 56),   # hitbox de fala do professor
]

# Diálogo com professor
interacao_professor = pygame.Rect(690, 170, 169, 130),   # hitbox de fala do professor
hitbox_professor =  pygame.Rect(750, 205, 65, 56),   # hitbox do professor
sala_vazia_on = False


# Saída da sala de informática 1
sair_da_sala_inf1 = pygame.Rect(1390, 240, 45, 1)
sair_da_sala_inf1_x = 800
sair_da_sala_inf1_y = 310


informatica_txt = pygame.image.load("assets/img/scenes/informatica/informatica1_txt.png")
hitbox_pc = pygame.Rect(764, 418, 176, 78)


# Variáveis para controlar o piscar
intervalo_piscar = 500  # Intervalo de piscar em milissegundos (0.5 segundo)
ultimo_tempo_piscar = 0  # Último momento em que alternamos a visibilidade
azul_visivel = True  # Controle de visibilidade do retângulo
seta_azul  = pygame.image.load("assets/img/interface/seta_azul.png")


bola_azul = pygame.image.load("assets/img/interface/bola_azul.png")
segunda_atividade = pygame.image.load("assets/img/scenes/informatica/segunda_atividade.png")

entrou_inf1 = False

dialogo_final_concluido = False

