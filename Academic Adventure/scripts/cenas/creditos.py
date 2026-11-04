import pygame

# Inicializar o Pygame
pygame.init()

'''# Configurações da tela
LARGURA, ALTURA = 1920, 1080
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Créditos")'''


# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

fonte = pygame.font.Font(None, 60)

# Fonte e texto
creditos_texto = [
    "Criado por: Turma 0043.",
    " ",
    "Inspirado em: Pokémon Fire Red.",
    " ",
    "Desenvolvimento e programação do jogo: Marcelo Junior e Caio Carolino.",
    " ",
    "Programação do site: Lucas Gabriel, Ludmila Regina, Vitória Larissa e Samuel Martins.",
    " ",
    "Sprites e cenários: Lucas Gabriel, Wendell Henrique, Logan Lucky,",
    "Lincoln Luciano e Gleiciene Fernandes, Samuel Martins.",
    " ",
    "Áudio e Música: Lucas Gabriel.",
    " ",
    "Ferramentas utilizadas: Linguagem Python, biblioteca pygame, softwares de edição gráfica,",
    "HTML, CSS, PHP e Java Script.",
    " ",
    "Obrigado por dedicar seu tempo para explorar este jogo.",
    " ",
    "Que sua jornada pelo conhecimento da Tecnologia da Informação seja tão incrível", 
    "quanto foi criar este projeto!",
]

# Preparar texto dos créditos
creditos_render = [fonte.render(linha, True, BRANCO) for linha in creditos_texto]

# Posição inicial dos créditos (fora da tela)
posicao_y = 1080

# Relógio para controle de FPS
relogio = pygame.time.Clock()

# Velocidade de rolagem
velocidade = 1