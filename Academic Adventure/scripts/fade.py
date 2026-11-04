import pygame

def fade_screen(screen, fade_type, color=(0, 0, 0), duration=1000):
    """
    Aplica um efeito de fade na tela.
    
    :param screen: Surface principal do jogo.
    :param fade_type: 'in' para fade in ou 'out' para fade out.
    :param color: Cor do fade (padrão preto).
    :param duration: Duração do fade em milissegundos.
    """
    fade_surface = pygame.Surface(screen.get_size())
    fade_surface.fill(color)
    alpha_step = 255 / (duration / (1000 / 60))  # Calcula o incremento do alfa por frame.

    clock = pygame.time.Clock()
    alpha = 255 if fade_type == 'in' else 0

    while (fade_type == 'in' and alpha > 0) or (fade_type == 'out' and alpha < 255):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        if fade_type == 'in':
            alpha = max(0, alpha - alpha_step)
        else:  # 'out'
            alpha = min(255, alpha + alpha_step)
        
        fade_surface.set_alpha(alpha)
        screen.fill((0, 0, 0))  # Fundo preto para evitar artefatos.
        screen.blit(fade_surface, (0, 0))
        pygame.display.flip()
        clock.tick(60)


# Fade in
fade_in_img = pygame.Surface((1920, 1080)).convert_alpha()
fade_in = fade_in_img.get_rect()
fade_in_img.fill("black")
fade_alpha_in = 255



# Texto de press to play
alpha_text = 100
fade_direction_text = 255


# Fade Out
fade_out = False
fade_out_img = pygame.Surface((1920, 1080)).convert_alpha()
fade_out_img.fill("black")
fade_alpha_out = 0  # O fade começa invisível (totalmente transparente)



fade_alpha = 255
fade_in_surface = pygame.Surface((1920, 1080)).convert_alpha()

def aplicar_fade(screen, fade_surface, fade_alpha):
    if fade_alpha > 0:
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0, 0))
        fade_alpha -= 0.6
    return fade_alpha


