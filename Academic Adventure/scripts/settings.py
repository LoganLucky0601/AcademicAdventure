import pygame

# Dimensões e definição da tela
width = 1920
height = 1080

# Janela do jogo
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

pygame.mouse.set_pos(960, 540)


# Sistema de pause
pause = False


# Variáveis de controle do jogo
loop = True

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA_CLARO = (200, 200, 200)



mouse_pos = pygame.mouse.get_pos()




# Defina o tempo de atraso (em milissegundos) # CENA DIPLOMA
delay_time = 10000  # 2000 milissegundos = 2 segundos
time_started = pygame.time.get_ticks()  # Registra o tempo inicial
on_screen = False  # Define se o texto está na tela ou não