import pygame
from scripts.settings import screen

# Botões sim e não
botao_sim = pygame.image.load("assets/img/interface/botao_sim.png")
botao_nao = pygame.image.load("assets/img/interface/botao_nao.png")

# Hitbox dos botões
hitbox_sim = pygame.Rect(1620, 850, 210, 72)
hitbox_nao = pygame.Rect(1620, 950, 210, 72)

# Variável de controle
botoes__visible = True
# Controle de tempo para o piscar
intervalo_blink_botoes = 1000  # Em milissegundos
last_blink_botoes = pygame.time.get_ticks()

# Tela de escolha de personagem
tela_char = pygame.image.load("assets/img/scenes/personagem/escolha_char.png")
femalechar_on = pygame.image.load("assets/img/scenes/personagem/femalechar_on.png")
malechar_on = pygame.image.load("assets/img/scenes/personagem/malechar_on.png")

# Imagens de tutoriais de Teclas
keys = pygame.image.load("assets/img/tutorial/keys.png")
press_e = pygame.image.load("assets/img/tutorial/press_e.png")
press_enter = pygame.image.load("assets/img/tutorial/press_enter.png")
press_p = pygame.image.load("assets/img/tutorial/press_p.png")
press_e_pross = pygame.image.load("assets/img/tutorial/press_e_pross.png")
press_enter_name = pygame.image.load("assets/img/tutorial/press_enter_name.png")
press_mouse_enter = pygame.image.load("assets/img/tutorial/press_mouse_enter.png")
press_mouse = pygame.image.load("assets/img/tutorial/press_mouse.png")

desenhar_bind = False
def draw_teclas():
  screen.blit(keys, (1215, 900))

# Imagem do menu de pausa

menu_pause = pygame.image.load("assets/img/interface/menu_pause.png")

tempo_atual = pygame.time.get_ticks()
intervalo = 500  # Intervalo de piscar em milissegundos (0.5 segundo)
last_time = 0  # Último momento em que alternamos a visibilidade
visivel = True  # Controle de visibilidade do retângulo


# Lógica para alternar a visibilidade do balão de diálogo
'''tempo_atual = pygame.time.get_ticks()  # Obtém o tempo atual em milissegundos
if tempo_atual - last_time >= intervalo:  # Verifica o intervalo
  visivel = not visivel  # Alterna a visibilidade
  last_time = tempo_atual  # Atualiza o último momento de alteração'''


fogo_azul = pygame.image.load("assets/img/interface/fogo_azul.png")
  
  
  
