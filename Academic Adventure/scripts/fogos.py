import pygame

fundo_fogos = pygame.image.load("assets/img/fogos/fundo_fogos.png")
parabens = pygame.image.load("assets/img/fogos/parabens.png")
fogo_laranja1 = pygame.image.load("assets/img/fogos/fogo_laranja1.png")
fogo_laranja2 = pygame.image.load("assets/img/fogos/fogo_laranja2.png")
fogo_roxo1 = pygame.image.load("assets/img/fogos/fogo_roxo1.png")
fogo_roxo2 = pygame.image.load("assets/img/fogos/fogo_roxo2.png")
fogo_roxo3 = pygame.image.load("assets/img/fogos/fogo_roxo3.png")
fogo_azul = pygame.image.load("assets/img/fogos/fogo_azul.png")
fogo_amarelo = pygame.image.load("assets/img/fogos/fogo_amarelo.png")
fogo_verde = pygame.image.load("assets/img/fogos/fogo_verde.png")

# Laranja
# Variáveis para controlar o piscar
piscar_laranja = 500  # Intervalo de piscar em milissegundos 
ultimo_tempo_laranja = 0  # Último momento em que alterna a visibilidade
laranja_visivel = True  # Controle de visibilidade do retângulo

# Roxo
# Variáveis para controlar o piscar
piscar_roxo = 800  # Intervalo de piscar em milissegundos 
ultimo_tempo_roxo = 0  # Último momento em que alterna a visibilidade
roxo_visivel = True  # Controle de visibilidade do retângulo

# Azul
# Variáveis para controlar o piscar
piscar_azul = 1000  # Intervalo de piscar em milissegundos 
ultimo_tempo_azul = 0  # Último momento em que alterna a visibilidade
fogo_azul_visivel = True  # Controle de visibilidade do retângulo

# Amarelo
# Variáveis para controlar o piscar
piscar_amarelo = 400  # Intervalo de piscar em milissegundos 
ultimo_tempo_amarelo = 0  # Último momento em que alterna a visibilidade
amarelo_visivel = True  # Controle de visibilidade do retângulo

# Verde
# Variáveis para controlar o piscar
piscar_verde = 900  # Intervalo de piscar em milissegundos 
ultimo_tempo_verde = 0  # Último momento em que alterna a visibilidade
verde_visivel = True  # Controle de visibilidade do retângulo

# Parabéns
piscar_parabens = 200  # Intervalo de piscar em milissegundos 
ultimo_tempo_parabens = 1  # Último momento em que alterna a visibilidade
parabens_visivel = True  # Controle de visibilidade do retângulo


