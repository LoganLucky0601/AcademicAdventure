import pygame
from scripts.settings import *
from scripts.font import *

'''
Sistema de exibição de mensagens de texto na tela
'''

# Variáveis usadas nas funções parágrafo e dialogo
counter = 0
done = False

# Imagem do balão de fala
dialog_box = pygame.image.load("assets/img/interface/dialog_box.png")  

# Função diálogo
active_message = 0

# Imagem do balão de fala
dialog_box = pygame.image.load("assets/img/interface/dialog_box.png")  

# Função diálogo
def dialogo(screen, messages, active_message, counter, x=20, y=820, font_path="assets/fonts/PixelifySansRegular.ttf", font_size=35, speed=3, text_color='black'):
    pixelify = pygame.font.Font(font_path, font_size)

    # Certifique-se de que a mensagem atual existe
    if active_message < len(messages):
        message = messages[active_message]
    else:
        return active_message, counter, True  # Se não houver mais mensagens, retorna

    done = False

    # Controle da velocidade da exibição da mensagem
    if counter < speed * len(message):
        counter += 1
    else:
        done = True  # Marca como concluído quando o texto for completamente renderizado

    # Renderiza a parte da mensagem atual
    snip = pixelify.render(message[0:counter // speed], True, text_color)  # Usa a cor do texto definida
    screen.blit(snip, (x, y))  # Ajusta a posição do texto na tela com base nas coordenadas x e y

    return active_message, counter, done










# Função de texto em parágrafo
active_text = 0
text_done = False  # Inicializa a variável como False, indicando que o texto não terminou

def paragrafo(screen, textos, active_text, counter, line_height=74, font_path="assets/fonts/PixelifySansRegular.ttf", font_size=40, speed=1, text_color='black'):
    pixelify = pygame.font.Font(font_path, font_size)
    done = False

    # Renderiza todas as mensagens até a mensagem atual
    for i in range(active_text + 1):
        msg = textos[i]
        y_position = 335 + (i * line_height)

        # Controle da velocidade da exibição da mensagem
        if i == active_text:
            if counter < speed * len(msg):  # Enquanto o texto não foi exibido completamente
                counter += 1
            else:
                done = True  # Quando a mensagem for exibida completamente, marca como 'feito'
            msg = msg[0:counter // speed]
        
        # Renderiza a parte da mensagem atual
        snip = pixelify.render(msg, True, text_color)  # Usa a cor do texto definida
        screen.blit(snip, (85, y_position))  # Ajusta a posição de cada mensagem com base na linha

    return active_text, counter, done







# Variáveis da caixa de texto
caixa_nome = False
caixa_texto = pygame.Rect(607, 393, 800, 1)
hitbox_caixa_texto = pygame.Rect(600, 370, 1236, 120)
texto = ""
ativo = False
nome = ""  # Nome do jogador
