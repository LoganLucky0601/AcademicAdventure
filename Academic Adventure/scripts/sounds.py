import pygame

# Inicializando Pygame e mixer
pygame.init()
pygame.mixer.init()

# Carregando e tocando o som
musica_inicial = pygame.mixer.Sound("assets/sounds/menusound.wav")
musica_tocando = False

# Carregando o som da cena introdução (som de digitação)
typing = pygame.mixer.Sound("assets/sounds/typing.wav")
typing_tocando = False

