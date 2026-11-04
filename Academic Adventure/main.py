import pygame, sys

from scripts.fogos import *
from scripts.settings import *
from scripts.portrait import *
from scripts.sounds import *
from scripts.puzzles.puzzle1 import *
from scripts.puzzles.puzzle2 import *
from scripts.puzzles.puzzle3 import *
from scripts.cenas import *
from scripts.interface import *
from scripts.functions import *
from scripts.malecharacter import *
from scripts.femalecharacter import *
from scripts.npc import *
from scripts.dialog import *
from scripts.falas import *
from scripts.carro import *
from scripts.entidades import * 
from scripts.fade import * 

pygame.init()
pygame.mixer.init()

cena = "inicial"  # inicial -> prologo -> introducao -> naming -> confirmacao -> personagem -> pre_jogo -> 
                     # rua -> terreo -> corredor -> biblioteca -> primeiro_andar -> informatica -> aprendizagem -> 
                     # segundo_andar -> sala_vazia1 -> auditorio -> fogos -> diploma -> creditos -> ...
                            
while loop:  # Início do loop principal do jogo
    
    if cena == "inicial":  # Verifica se estamos na cena inicial do jogo
    
        # Só começa a música se ainda não estiver tocando
        if not musica_tocando:  # Se a música não estiver tocando
            musica_inicial.play(loops=-1)  # Toca a música de fundo em loop
            musica_tocando = True  # Marca a variável para indicar que a música está tocando

        for event in pygame.event.get():  # Obtém todos os eventos do Pygame, como teclado e mouse
            if event.type == pygame.QUIT:  # Se o evento for o fechamento da janela
                loop = False  # Encerra o loop principal
                musica_inicial.stop()  # Para a música quando o jogo for fechado
                musica_tocando = False  # Resetar a variável de controle da música

            if event.type == pygame.KEYDOWN:  # Se uma tecla for pressionada
                if event.key == pygame.K_RETURN and not fade_out:  # Se pressionar ENTER e não estiver em fade-out
                    fade_out = True  # Inicia a transição de fade-out

            if event.type == pygame.MOUSEBUTTONDOWN:  # Se o mouse for pressionado
                mousepos = pygame.mouse.get_pos()  # Obtém a posição atual do mouse
                print(f'Coordenada: {mousepos}')  # Exibe a coordenada do mouse no terminal

        # Fade In
        if fade_alpha_in > 0:  # Se o valor da opacidade de fade for maior que zero
            fade_alpha_in -= 5  # Diminui a opacidade para um efeito de fade-in (transparente)
            fade_in_img.set_alpha(fade_alpha_in)  # Atualiza a opacidade da imagem de fade

        # Atualiza a tela com o fundo da cena inicial
        limpar_e_desenhar(tela_inicial)  # Função para limpar a tela e desenhar a cena inicial
        screen.blit(fade_in_img, (0, 0))  # Desenha a imagem do fade in na tela

        # Lógica do Fade-Out
        if fade_out:  # Se o fade-out estiver ativado
            fade_alpha_out += 5  # Aumenta a opacidade do fade-out para criar o efeito
            if fade_alpha_out > 255:  # Limita o valor máximo a 255
                fade_alpha_out = 255

            fade_out_img.set_alpha(fade_alpha_out)  # Atualiza a opacidade da imagem do fade-out
            screen.blit(fade_out_img, (0, 0))  # Desenha a imagem de fade na tela

            if fade_alpha_out == 255:  # Quando a opacidade chega ao máximo
                cena = "prologo"  # Muda para a cena de introdução
                musica_inicial.stop()  # Para a música de fundo
                musica_tocando = False  # Reseta a variável que controla a música
                fade_alpha_out = 0  # Prepara o valor da opacidade para o próximo uso
                fade_out = False  # Desativa o fade-out para evitar repetição

        # Lógica do efeito de transparência da imagem de press enter
        if fading_in:
            opacity += 7  # Aumenta a opacidade
            if opacity >= 255:
                opacity = 255
                fading_in = False  # Troca para "fade out"
        else:
            opacity -= 7  # Reduz a opacidade
            if opacity <= 0:
                opacity = 0
                fading_in = True  # Troca para "fade in"

        # Atualizar a transparência da imagem
        play.set_alpha(opacity)
        screen.blit(play, (850, 1000))

        atualizar_tela()  # Atualiza a tela do jogo com todas as alterações feitas

    elif cena == "prologo":  # Verifica se a cena atual é o prólogo do jogo
        if not typing_tocando:  # Verifica se o som de digitação está desativado
            typing.play()  # Inicia a reprodução do som de digitação
            typing_tocando = True  # Define que o som de digitação está ativo
                    
        for event in pygame.event.get():  # Processa a fila de eventos do Pygame
            if event.type == pygame.QUIT:  # Se o usuário tentar fechar a janela
                loop = False  # Finaliza o loop principal do jogo
                sys.exit()  # Fecha o programa completamente
                
            if event.type == pygame.KEYDOWN:  # Verifica se uma tecla foi pressionada
                if event.key == pygame.K_RETURN and not fade_out:  # Caso ENTER seja pressionado e não esteja em fade-out
                    fade_out = True  # Inicia o efeito de fade-out para a próxima cena

        limpar_e_desenhar(tela_prologo)  # Limpa a tela e desenha os elementos visuais do prólogo
            
        if active_text < len(prologo_text):  # Verifica se ainda há texto do prólogo a ser exibido
            # Atualiza o texto em exibição com base no índice atual (active_text),
            # no contador interno (counter) e no status de conclusão (done)
            active_text, counter, done = paragrafo(screen, prologo_text, active_text, counter)

            if done:  # Se o texto atual tiver sido exibido completamente
                if active_text == len(prologo_text) - 1:  # Verifica se é o último texto do prólogo
                    active_text = 0  # (Opcional) Reseta o índice do texto
                    counter = 0  # Reseta o contador interno
                    done = False  # Reseta o status de conclusão
                    cena = "introducao"  # Altera a cena para a introdução (menu)
                else:
                    active_text += 1  # Avança para o próximo texto
                    counter = 0  # Reseta o contador para reiniciar a exibição do texto
            
        atualizar_tela()  # Atualiza a tela para refletir mudanças nos elementos exibidos

    elif cena == "introducao":  # Verifica se a cena atual é a introdução
        for event in pygame.event.get():  # Processa os eventos capturados pelo Pygame
            if event.type == pygame.QUIT:  # Caso o jogador feche a janela do jogo
                loop = False  # Encerra o loop principal do jogo
            if event.type == pygame.KEYDOWN:  # Verifica se uma tecla foi pressionada
                if event.key == pygame.K_RETURN:  # Caso a tecla E seja pressionada
                    if done:  # Permite avançar somente se o texto atual estiver concluído
                        if caixa_nome:  # Verifica se está no estado de entrada do nome
                            caixa_nome = False  # Sai do estado de entrada do nome
                            cena = "naming"  # Define a cena seguinte como "naming"
                        else:  # Caso não esteja no estado de entrada do nome
                            if active_message < len(start_text) - 1:  # Se ainda há mensagens a serem exibidas
                                active_message += 1  # Avança para a próxima mensagem
                                counter = 0  # Reseta o contador de exibição
                                done = False  # Reseta o status de conclusão da mensagem atual

            if event.type == pygame.MOUSEBUTTONDOWN:  # Caso o jogador clique com o mouse
                mousepos = pygame.mouse.get_pos()  # Obtém as coordenadas do clique do mouse
                print(f'Coordenada: {mousepos}')  # Exibe as coordenadas do clique no console

        # Lógica para alternar a visibilidade da seta amarela de diálogo piscando
        current_time_seta = pygame.time.get_ticks()  # Obtém o tempo atual em milissegundos
        if current_time_seta - last_blink_time_seta >= blink_interval_seta:  # Verifica o intervalo
            is_pointer_visible = not is_pointer_visible  # Alterna a visibilidade da seta
            last_blink_time_seta = current_time_seta  # Atualiza o último momento de alteração

        # Fade In
        if fade_alpha_in > 0:  # Se o valor da opacidade de fade for maior que zero
            fade_alpha_in -= 1  # Diminui a opacidade para um efeito de fade-in (transparente)
            fade_in_img.set_alpha(fade_alpha_in)  # Atualiza a opacidade da imagem de fade

        # Atualiza a tela com o fundo da cena inicial
        limpar_e_desenhar(tela_introducao)  # Função para limpar a tela e desenhar a cena inicial
        screen.blit(portrait_professor, (900, 250))  # Adiciona o retrato do professor à tela
        screen.blit(dialog_box, (0, 800))  # Adiciona a caixa de diálogo à tela
        screen.blit(press_enter, key_position)  # Exibe a indicação de "Press ENTER"

        # Desenha a seta amarela piscando se estiver visível
        if is_pointer_visible:
            screen.blit(seta_azul, pointer_position)

        # Exibe e atualiza o diálogo na tela
        if active_message < len(start_text):  # Verifica se há mensagens para serem exibidas
            active_message, counter, done = dialogo(screen, start_text, active_message, counter, 
                                                    x=85, y=905, speed=3, text_color=(0, 0, 0))  # Configura o diálogo com texto em preto  # Configura o diálogo com texto em preto

        # Quando a última mensagem da introdução for exibida e concluída
        if done and active_message == len(start_text) - 1 and not nome:
            caixa_nome = True  # Ativa o estado para entrada do nome do jogador

        atualizar_tela()  # Atualiza a tela a cada iteração do loop

    elif cena == "naming":  # Verifica se a cena atual é a de entrada do nome
        confirmacao_nome[0] = ""  # Define a mensagem de confirmação para entrada do nome
        for event in pygame.event.get():  # Processa os eventos capturados pelo Pygame
            if event.type == pygame.QUIT:  # Caso o jogador feche a janela do jogo
                loop = False  # Encerra o loop principal do jogo
            if event.type == pygame.KEYDOWN:  # Verifica se uma tecla foi pressionada
                if caixa_nome and event.key == pygame.K_BACKSPACE:  # Se no estado de entrada do nome e BACKSPACE for pressionado
                    texto = texto[:-1]  # Remove o último caractere digitado
                elif caixa_nome and event.key != pygame.K_RETURN:  # Evita que a tecla ENTER seja adicionada ao texto
                    texto += event.unicode  # Adiciona o caractere correspondente à tecla pressionada ao texto
                if event.key == pygame.K_RETURN:  # Caso a tecla ENTER seja pressionada
                    if texto.strip():  # Verifica se algo foi digitado (removendo espaços)
                        caixa_nome = False  # Finaliza a entrada do nome
                        nome = texto.strip()  # Salva o nome digitado na variável 'nome', removendo espaços extras
                        confirmacao_nome[0] = f"Certo! Então seu nome é {nome}."
                        active_message = 0  # Reseta o índice para a lista de mensagens de confirmação
                        counter = 0  # Reseta o contador para exibição das mensagens
                        done = False  # Reseta o status de conclusão da mensagem atual
                        cena = "confirmacao"  # Avança para a cena seguinte
                    else:
                        pass  # Não faz nada se o nome estiver vazio

            if event.type == pygame.MOUSEBUTTONDOWN:  # Caso o jogador clique com o mouse
                mousepos = pygame.mouse.get_pos()  # Obtém as coordenadas do clique
                print(f'Coordenada: {mousepos}')  # Exibe as coordenadas no console para debug

        # Lógica para alternar a visibilidade da seta piscante
        current_time = pygame.time.get_ticks()  # Obtém o tempo atual em milissegundos
        if current_time - last_blink_time >= blink_interval:  # Verifica se o intervalo para piscar foi atingido
            seta_vermelha_visible = not seta_vermelha_visible  # Alterna a visibilidade do seta
            last_blink_time = current_time  # Atualiza o último momento de alteração

        # Atualiza a tela com o fundo da cena inicial
        limpar_e_desenhar(tela_naming)  # Função para limpar a tela e desenhar a cena inicial

        if seta_vermelha_visible:  # Se a seta estiver visível
            screen.blit(seta_vermelha, seta_vermelha_position)  # Desenha a seta na tela
        
        screen.blit(press_enter_name, (1200, 10))  # Desenha tutorial de entrada de nome na tela
        
        # Renderiza o nome digitado na caixa de texto
        inserir_nome = pixelify_big.render(texto, True, PRETO)  # Renderiza o texto em preto
        screen.blit(inserir_nome, (caixa_texto.x + 10, caixa_texto.y - 35))  # Posiciona o texto na tela

        # Exibe e atualiza a mensagem de confirmação na tela
        if active_message < len(confirmacao_nome):  # Verifica se há mensagens na lista de confirmação
            active_message, counter, done = dialogo(screen, confirmacao_nome, active_message, counter,
                                                    x=85, y=905, speed=3, text_color=(0, 0, 0))  # Configura o diálogo com texto em preto  # Configura e desenha a mensagem

        atualizar_tela()  # Atualiza a tela para refletir as alterações

    elif cena == "confirmacao":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    cena = "personagem"  # Muda a cena para "personagem" 

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                print(f'Coordenada: {mousepos}')  # Exibe as coordenadas no console
                
                # Verificando se o clique foi na área do botão "Sim"
                if hitbox_sim.collidepoint(event.pos):
                    # Aqui você pode finalizar a escolha ou tomar alguma outra ação
                    cena = "personagem"  # Muda a cena para "personagem"  
                    
                # Verificando se o clique foi na área do botão "Não"
                if hitbox_nao.collidepoint(event.pos):
                    # Redefine a cena para "naming", onde o jogador pode inserir o nome novamente
                    cena = "naming"  # Volta para a cena de "naming"
                    
                    # Resetar o estado e texto da cena "naming" para permitir nova inserção
                    texto = ""  # Limpa o nome inserido
                    caixa_nome = True  # Retorna a caixa de texto de nome visível
                    active_message = 0  # Reseta as mensagens de confirmação, se necessário
                    counter = 0  # Reseta o contador para as mensagens
                    done = False  # Reseta o status de conclusão da mensagem
        
        # Lógica para alternar a visibilidade dos botões sim e não piscando
        current_time_botoes = pygame.time.get_ticks()  # Obtém o tempo atual em milissegundos
        if current_time_botoes - last_blink_botoes >= intervalo_blink_botoes:  # Verifica o intervalo
            botoes__visible = not botoes__visible  # Alterna a visibilidade da seta
            last_blink_botoes = current_time_botoes  # Atualiza o último momento de alteração

        # Fade In
        if fade_alpha_in > 0:  # Se o valor da opacidade de fade for maior que zero
            fade_alpha_in -= 1  # Diminui a opacidade para um efeito de fade-in (transparente)
            fade_in_img.set_alpha(fade_alpha_in)  # Atualiza a opacidade da imagem de fade

        # Atualiza a tela com o fundo da cena inicial
        limpar_e_desenhar(tela_introducao)  # Função para limpar a tela e desenhar a cena inicial
        screen.blit(fade_in_img, (0, 0))  # Desenha a imagem do fade in na tela
        screen.blit(portrait_professor, (1220, 200))
        screen.blit(dialog_box, (0, 800))
        screen.blit(press_mouse_enter, (35, 750))
        
        # Lógica de exibição de texto
        if active_message < len(confirmacao_nome):
            active_message, counter, done = dialogo(screen, confirmacao_nome, active_message, counter, 
                                                    x=85, y=905, speed=3, text_color=(0, 0, 0))  # Configura o diálogo com texto em preto  # Texto em preto
        
        # Lógica de exibição dos botões  
        if done and active_message < len(confirmacao_nome) - 1:
            screen.blit(botao_sim, (1620, 850))  # Exibe o botão "Sim" na tela
            screen.blit(botao_nao, (1620, 950))  # Exibe o botão "Não" na tela
            # Desenha a seta amarela piscando se estiver visível
            if botoes__visible:
                screen.blit(seta_verde, (1560, 865))  # Exibe a seta verde do botão SIM
                screen.blit(seta_vermelha, (1560, 960))  # Desenha a seta vermelha do botão NÃO

        # Atualiza a tela
        atualizar_tela()  # Atualiza a tela a cada iteração

    elif cena == "personagem":
        # Loop de eventos da cena "personagem"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                sys.exit()  # Encerra o programa completamente
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and done:
                    if active_message < len(escolha_genero) - 1:  # Se ainda há mensagens a serem exibidas
                        active_message += 1  # Avança para a próxima mensagem
                        counter = 0  # Reseta o contador de exibição
                        done = False  # Reseta o status de conclusão da mensagem atual

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                print(f'Coordenada: {mousepos}')  # Exibe as coordenadas no console

                # Verificando se o clique foi na área do botão "Sim"
                if hitbox_boy.collidepoint(mousepos):
                    personagem_escolhido = "menino"  # Define o personagem escolhido como "menino"
                    player = MaleCharacter(x=855, y=650, velocidade=3.5, velocidade_animacao=10)  # Cria o personagem masculino
                    selecao_de_personagem = False  # Desativa a seleção de personagem
                    active_message = 0  # Reinicia para a primeira mensagem
                    counter = 0  # Reseta o contador
                    done = False  # Garante que o status de conclusão está desativado
                    cena = "pre_jogo"  # Muda a cena para "pre_jogo"
                elif hitbox_girl.collidepoint(mousepos):
                    personagem_escolhido = "menina"  # Define o personagem escolhido como "menina"
                    player = FemaleCharacter(x=855, y=650, velocidade=3.5, velocidade_animacao=10)  # Cria o personagem feminino
                    selecao_de_personagem = False  # Desativa a seleção de personagem
                    active_message = 0  # Reinicia para a primeira mensagem
                    counter = 0  # Reseta o contador
                    done = False  # Garante que o status de conclusão está desativado
                    cena = "pre_jogo"  # Muda a cena para "pre_jogo"

        # Lógica para alternar a visibilidade da seta amarela de diálogo piscando
        current_time_seta = pygame.time.get_ticks()  # Obtém o tempo atual em milissegundos
        if current_time_seta - last_blink_time_seta >= blink_interval_seta:  # Verifica o intervalo
            is_pointer_visible = not is_pointer_visible  # Alterna a visibilidade da seta
            last_blink_time_seta = current_time_seta  # Atualiza o último momento de alteração

        # Limpa a tela apenas quando a seleção de personagem não está ativa
        if not selecao_de_personagem:
            limpar_e_desenhar(tela_introducao)  # Função para limpar a tela e desenhar a cena inicial
            screen.blit(portrait_professor, (1220, 200))
            screen.blit(dialog_box, (0, 800))
            screen.blit(press_enter, key_position)  # Exibe a indicação de "Press E"
            # Desenha a seta amarela piscando se estiver visível
            if is_pointer_visible:
                screen.blit(seta_azul, pointer_position)

            # Lógica de exibição de texto
            if active_message < len(escolha_genero):
                active_message, counter, done = dialogo(
                    screen, escolha_genero, active_message, counter,
                    x=85, y=905, speed=3, text_color=(0, 0, 0))  # Configura o diálogo com texto em preto

            # Lógica para ativar a tela de seleção de personagem
            if done and active_message == len(escolha_genero) - 1:
                selecao_de_personagem = True
        else:
            # Quando a seleção de personagem está ativa
            screen.fill([255, 255, 255])  # Preenche a tela com branco para exibir a seleção de personagem
            screen.blit(tela_char, (0, 0))  # Exibe a tela de escolha de personagem

            mouse_pos = pygame.mouse.get_pos()
            if hitbox_boy.collidepoint(mouse_pos):
                screen.blit(malechar_on, (0, 0))

            elif hitbox_girl.collidepoint(mouse_pos):
                screen.blit(femalechar_on, (0, 0))
            else:
                screen.blit(tela_char, (0, 0))

        # Atualiza a tela
        atualizar_tela()

    elif cena == "pre_jogo":
        # Loop de eventos da cena "introducao"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Se o jogador clicar no botão de fechar a janela, o loop é encerrado
                loop = False
                sys.exit()  # Encerra o programa
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and done:
                    if active_message < len(finalizacao_jogo) - 1:  # Se ainda há mensagens a serem exibidas
                        active_message += 1  # Avança para a próxima mensagem
                        counter = 0  # Reseta o contador de exibição
                        done = False  # Reseta o status de conclusão da mensagem atual
                        
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Se o jogador clicar com o mouse, a posição do clique é capturada
                mousepos = pygame.mouse.get_pos()  # Pega as coordenadas do clique
                print(f'Coordenada: {mousepos}')  # Imprime as coordenadas na tela de console
        
        # Lógica para alternar a visibilidade da seta amarela de diálogo piscando
        current_time_seta = pygame.time.get_ticks()  # Obtém o tempo atual em milissegundos
        if current_time_seta - last_blink_time_seta >= blink_interval_seta:  # Verifica o intervalo
            is_pointer_visible = not is_pointer_visible  # Alterna a visibilidade da seta
            last_blink_time_seta = current_time_seta  # Atualiza o último momento de alteração

        # Limpar a tela e desenhar o cenário
        limpar_e_desenhar(tela_introducao)
        screen.blit(portrait_professor, (1220, 200))
        screen.blit(dialog_box, (0, 800))
        screen.blit(press_enter, key_position)  # Exibe a indicação de "Press ENTER"
        
        # Lógica de exibição de texto
        if active_message < len(finalizacao_jogo):
            active_message, counter, done = dialogo(screen, finalizacao_jogo, active_message, counter, 
                                                    x=85, y=905, speed=3, text_color=(0, 0, 0))  # Configura o diálogo com texto em preto  # Texto em preto
        
        # Lógica de exibição dos botões  
        if done and active_message == len(finalizacao_jogo) - 1:
            cena = "rua"  # Muda a cena para "rua"

        # Desenha a seta amarela piscando se estiver visível
        if is_pointer_visible:
            screen.blit(seta_azul, pointer_position)
                
        # Atualiza a tela e os Frames
        atualizar_tela()  # Atualiza a tela com as mudanças realizadas
    
    elif cena == "rua":
    # Cena atual sendo executada é "rua"

        if not musica_tocando:
            # Carrega e toca a música apenas uma vez
            pygame.mixer.music.load("assets/sounds/soundtrack.wav")
            pygame.mixer.music.set_volume(0.5)  # Ajusta o volume
            pygame.mixer.music.play(loops=-1)  # Toca a música em looping infinito
            musica_tocando = True  # Marca que a música está tocando
    
    # Verifica se o jogo está pausado e exibe o menu de pausa
        if pause:
            draw_pause(screen, menu_pause, pixelify_tiny, nome, personagem_escolhido)  # Exibe o menu de pausa


        for event in pygame.event.get():  # Loop de eventos para capturar interações do usuário
            if event.type == pygame.QUIT:  # Se o jogador fechar a janela
                loop = False  # Finaliza o loop principal
            if event.type == pygame.KEYDOWN:  # Evento de tecla pressionada
                if event.key == pygame.K_p:  # Se a tecla P for pressionada
                    # Alterna entre pausado e não pausado
                    if pause:
                        pause = False
                    else:
                        pause = True
                        
            if event.type == pygame.MOUSEBUTTONDOWN:  # Evento de clique do mouse
                mousepos = pygame.mouse.get_pos()  # Pega as coordenadas do clique                
                if pause and botao_continue.collidepoint(event.pos):
                    print("Continuar")  # Exibe mensagem no console
                    if pause:
                        pause = False
                    else:
                        pause = True
                        
                if pause and botao_sair.collidepoint(event.pos):
                    loop = False

                    
        # Verifica se o jogo não está pausado para atualizar os elementos
        if not pause:
            teclas = pygame.key.get_pressed()  # Captura as teclas pressionadas pelo jogador
            novo_x = player.x  # Guarda a posição atual do jogador para lidar com colisões
            novo_y = player.y 
            
            # Atualizar tela
            screen.fill([255, 255, 255])  # Preenche a tela com branco

            # Desenha o cenário da rua
            screen.blit(rua, (-4, -115))  # Desenha o cenário principal (rua)
            desenhar_img(cercaleft, 1, 585)  # Desenha objetos na rua (cerca esquerda)
            desenhar_img(cercaright, 1175, 585)  # Cerca direita
            desenhar_img(mesa_antonio, 410, 620)  # Uma mesa no cenário
            desenhar_img(antonio, 310, 590)  # Uma mesa no cenário
            
            # Faz o carro parar em uma posição específica e define sua animação para "parado"
            if carro0.carro_x <= 750:
                carro0.velocidade_carro = 0  # Para o carro
                carro0.direcao = "parado"  # Altera a direção para "parado"
                spr_atual_carro0 = carro0.animacoes["parado"][0]  # Seleciona o sprite de carro parado
            
            # Faz o jogador aparecer após o carro parar
            if referencia.npc_x <= 1570:
                player.desenhar_mainchar(screen)  # Desenha o jogador na tela  

            # Condições para movimentar o carro e o jogador
            if referencia.npc_x <= 1400 and referencia.npc_x >= 815:
                carro0.velocidade_carro = 10  # Define a velocidade do carro
                carro0.direcao = "esquerda"  # Altera a direção para "esquerda"
                player.mover(teclas)  # Move o jogador conforme as teclas pressionadas
                desenhar_bind = True
                if desenhar_bind:
                    screen.blit(keys, (1215, 900))  # Desenha instruções para as teclas na tela
                    screen.blit(press_p, (1215, 850))  # Desenha instruções para as teclas na tela

            # Para de desenhar as instruções após o NPC passar de certo ponto
            if referencia.npc_x < 815:
                desenhar_bind = False  # Reseta a variável
                player.mover(teclas)  # Move o jogador

            # Movimenta NPCs e carros quando alcançam uma área específica
            if referencia.npc_x <= 1520:
                for npc in npcs_rua:
                    npc.mover_npc()  # Atualiza a posição dos NPCs
                for npc in npcs_rua:
                    verificar_entrada_npc(npc, entrada_senac, screen)
                for automoveis in carros_rua:
                    automoveis.mover_carro()  # Atualiza a posição dos carros
                for automoveis in carros_rua:
                    desenhar_carro(automoveis)  # Desenha os carros na tela

            desenhar_carro(carro0)  # Desenha o carro principal na tela
            carro0.mover_carro()  # Atualiza a posição do carro principal
            
            referencia.mover_npc()  # Atualiza a posição do NPC referência
            #verificar_entrada_npc(referencia, entrada_senac, screen)
            
            # Verifica colisões com as hitboxes do cenário
            for hitbox in hitboxes_rua:
                if player.hitbox.colliderect(hitbox):  # Se houver colisão
                    player.x = novo_x  # Impede movimento na posição x
                    player.y = novo_y  # Impede movimento na posição y
        
            # Verifica se o jogador entrou na área de entrada do Senac
            if player.hitbox.colliderect(entrada_senac):
                cena = "terreo"  # Muda a cena para "terreo"
                player.x = entrando_senac_x  # Define nova posição x do jogador
                player.y = entrando_senac_y  # Define nova posição y do jogador
        
        # Aplica efeito de fade-in para transição de tela apenas se o jogo não estiver pausado
        if not pause:
            fade_alpha = aplicar_fade(screen, fade_in_surface, fade_alpha)

        # Atualiza a tela com os elementos desenhados e controla os frames por segundo
        atualizar_tela()

    elif cena == "terreo":
        if pause:
            draw_pause(screen, menu_pause, pixelify_tiny, nome, personagem_escolhido)  # Exibe o menu de pausa
            
        # Loop de eventos da cena "terreo"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False  # Encerra o jogo
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and done:
                    if active_message < len(recepcionista_msg1) - 1:  # Se ainda há mensagens a serem exibidas
                        active_message += 1  # Avança para a próxima mensagem
                        counter = 0  # Reseta o contador de exibição
                        done = False  # Reseta o status de conclusão da mensagem atual
                if event.key == pygame.K_RETURN and done:
                    if active_message < len(atendente_msg1) - 1:  # Se ainda há mensagens a serem exibidas
                        active_message += 1  # Avança para a próxima mensagem
                        counter = 0  # Reseta o contador de exibição
                        done = False  # Reseta o status de conclusão da mensagem atual
                        
                if event.key == pygame.K_p:  # Se a tecla P for pressionada
                    # Alterna entre pausado e não pausado
                    if pause:
                        pause = False
                    else:
                        pause = True
                        
            if event.type == pygame.MOUSEBUTTONDOWN:  # Evento de clique do mouse
                mousepos = pygame.mouse.get_pos()  # Pega as coordenadas do clique                
                if pause and botao_continue.collidepoint(event.pos):
                    print("Continuar")  # Exibe mensagem no console
                    if pause:
                        pause = False
                    else:
                        pause = True
                if pause and botao_sair.collidepoint(event.pos):
                    loop = False
                    
        if not pause:
            # Captura as teclas pressionadas
            teclas = pygame.key.get_pressed()
            
            # Armazena a posição atual do personagem
            novo_x = player.x
            novo_y = player.y
            
            # Mover o player com base nas teclas pressionadas
            player.mover(teclas)
            
                # Verificar colisões com as hitboxes do térreo
            for hitbox in hitboxes_terreo:
                if player.hitbox.colliderect(hitbox):
                    # Se houver colisão, retorna à posição anterior
                    player.x = novo_x
                    player.y = novo_y

            # Limpar e desenhar o cenário do térreo
            limpar_e_desenhar(terreo)

            if not recepcionista_dialog_concluido:
                screen.blit(tip1, (110, 460))
            
            # Desenha o balão de tutorial
            if not bloqueio_progresso1_on and recepcionista_dialog_concluido and not atendente_dialog_concluido:
                if visivel:
                    screen.blit(area_pontilhada, (725, 679))
            
            screen.blit(npc3.animacoes["cima"][0], (1675, 815))
            screen.blit(chair_top, (1710, 900))  # Desenha a imagem da cadeira no topo da tela
            
            # Blita o sprite específico diretamente na posição do NPC
            screen.blit(npc55.animacoes["baixo"][1], (150, 70))
            screen.blit(npc56.animacoes["baixo"][1], (230, 70))
            screen.blit(npc48.animacoes["baixo"][3], (545, 160))

            desenhar_img(parede_final1, 1702, 252)
            
            # Lógica para alternar a visibilidade da seta amarela de diálogo piscando
            current_time_seta = pygame.time.get_ticks()  # Obtém o tempo atual em milissegundos
            if current_time_seta - last_blink_time_seta >= blink_interval_seta:  # Verifica o intervalo
                is_pointer_visible = not is_pointer_visible  # Alterna a visibilidade da seta
                last_blink_time_seta = current_time_seta  # Atualiza o último momento de alteração
            
            # Lógica para alternar visiblidade do balão de tutorial
            tempo_atual = pygame.time.get_ticks()  # Obtém o tempo atual em milissegundos
            if tempo_atual - last_time >= intervalo:  # Verifica o intervalo
                visivel = not visivel  # Alterna a visibilidade
                last_time = tempo_atual  # Atualiza o último momento de alteração
    
            # Inicializar flags para áreas
            area_supervisao_ativa = False
            area_ti_ativa = False
            area_professores_ativa = False
            area_final2_ativa = False

            def ativar_area(area):
                """Ativa uma área e desativa as outras."""
                global area_supervisao_ativa, area_ti_ativa, area_professores_ativa, area_final2_ativa
                area_supervisao_ativa = area == "supervisao"
                area_ti_ativa = area == "ti"
                area_professores_ativa = area == "professores"
                area_final2_ativa = area == "final2"

            # Dentro do loop do jogo:
            if player.hitbox.colliderect(area_supervisao):
                ativar_area("supervisao")
            elif player.hitbox.colliderect(area_ti):
                ativar_area("ti")
            elif player.hitbox.colliderect(area_professores):
                ativar_area("professores")
            elif player.hitbox.colliderect(area_final2):
                ativar_area("final2")
            else:
                ativar_area(None)  # Nenhuma área ativa
                desenhar_img(parede_supervisao, 409, 470)
                desenhar_img(parede_ti, 1120, 260)
                desenhar_img(superior_professores, 998, 477)
                desenhar_img(parede_final2, 1765, 480)
            
            # Processar áreas ativas
            if area_supervisao_ativa:
                if player.y < 500:
                    player.desenhar_mainchar(screen)
                    desenhar_img(parede_supervisao, 409, 470)
                    desenhar_img(parede_ti, 1120, 260)
                    desenhar_img(superior_professores, 998, 477)
                    desenhar_img(parede_final2, 1765, 480)
                    if player.hitbox.colliderect(parede_top_supervisao1):
                        player.x, player.y = novo_x, novo_y
                else:
                    desenhar_img(parede_ti, 1120, 260)
                    desenhar_img(superior_professores, 998, 477)
                    desenhar_img(parede_final2, 1765, 480)
                    desenhar_img(parede_supervisao, 409, 470)
                    player.desenhar_mainchar(screen)
                    if player.hitbox.colliderect(parede_top_supervisao2):
                        player.x, player.y = novo_x, novo_y

            elif area_ti_ativa:
                if player.y < 300:
                    player.desenhar_mainchar(screen)
                    desenhar_img(parede_ti, 1120, 260)
                    desenhar_img(parede_supervisao, 409, 470)
                    desenhar_img(superior_professores, 998, 477)
                    desenhar_img(parede_final2, 1765, 480)
                    if player.hitbox.colliderect(parede_ti1):
                        player.x, player.y = novo_x, novo_y
                else:
                    desenhar_img(parede_ti, 1120, 260)
                    desenhar_img(parede_supervisao, 409, 470)
                    desenhar_img(superior_professores, 998, 477)
                    desenhar_img(parede_final2, 1765, 480)
                    player.desenhar_mainchar(screen)
                    if player.hitbox.colliderect(parede_ti2):
                        player.x, player.y = novo_x, novo_y

            elif area_professores_ativa:
                if player.y < 550:
                    player.desenhar_mainchar(screen)
                    desenhar_img(superior_professores, 998, 477)
                    desenhar_img(parede_supervisao, 409, 470)
                    desenhar_img(parede_ti, 1120, 260)
                    desenhar_img(parede_final2, 1765, 480)
                    if player.hitbox.colliderect(superior_professores1):
                        player.x, player.y = novo_x, novo_y
                else:
                    desenhar_img(superior_professores, 998, 477)
                    desenhar_img(parede_supervisao, 409, 470)
                    desenhar_img(parede_ti, 1120, 260)
                    desenhar_img(parede_final2, 1765, 480)
                    player.desenhar_mainchar(screen)
                    if player.hitbox.colliderect(superior_professores2):
                        player.x, player.y = novo_x, novo_y

            elif area_final2_ativa:
                if player.y < 540:
                    player.desenhar_mainchar(screen)
                    desenhar_img(parede_final2, 1765, 480)
                    desenhar_img(parede_supervisao, 409, 470)
                    desenhar_img(parede_ti, 1120, 260)
                    desenhar_img(superior_professores, 998, 477)
                    if player.hitbox.colliderect(parede_final2_1):
                        player.x, player.y = novo_x, novo_y
                else:
                    desenhar_img(parede_final2, 1765, 480)
                    desenhar_img(parede_supervisao, 409, 470)
                    desenhar_img(parede_ti, 1120, 260)
                    desenhar_img(superior_professores, 998, 477)
                    player.desenhar_mainchar(screen)
                    if player.hitbox.colliderect(parede_final2_2):
                        player.x, player.y = novo_x, novo_y

            # Caso nenhuma área esteja ativa
            else:
                player.desenhar_mainchar(screen)  # Sempre desenhar o jogador fora de áreas
                
            desenhar_img(parede_terreo, 375, 470)  
            desenhar_img(parede_terreo2, 973, 475)  
            
            #for hitbox in hitboxes_terreo:
                #pygame.draw.rect(screen, (255, 0, 0), hitbox, 2)        
            
            # Desenho de NPCs     
            seguranca_npc.desenhar_seguranca(screen)  # Desenha o segurança    
            
            screen.blit(atendente1, (850, 615))
            screen.blit(atendente2, (850, 705))
            screen.blit(atendente3, (850, 785))
            screen.blit(atendente4, (415, 600))


            if bloqueio_progresso1_on:
                if player.hitbox.colliderect(bloqueio_progresso1):
                    player.x, player.y = novo_x, novo_y

            if bloqueio_progresso2_on:
                if player.hitbox.colliderect(bloqueio_progresso2):
                    player.x, player.y = novo_x, novo_y
            
            # Interação com a recepcionista ao pressionar 'E'
            if player.hitbox.colliderect(recepcionista_dialogo):
                if teclas[pygame.K_RETURN]:  # Quando o jogador pressiona 'E'
                    if not dialogo_ativo:  # Se o diálogo não está ativo, inicia o diálogo
                        dialogo_ativo = True
                        active_message = 0  # Reinicia a mensagem ativa
                        counter = 0  # Reinicia o contador
                        done = False  # Define que o diálogo não terminou

                if dialogo_ativo:
                    player.velocidade = 0
                    screen.blit(dialog_box, (0, 800))  # Desenha a caixa de diálogo
                    screen.blit(press_enter, (35, 750))  # Desenha "pressione E para prosseguir"
                    if active_message < len(recepcionista_msg1):  # Verifica se há mensagens para serem exibidas
                        active_message, counter, done = dialogo(screen, recepcionista_msg1, active_message, counter, 
                                                                x=85, y=905, speed=3, text_color=(0, 0, 0))  # Configura o diálogo com texto em preto  # Configura o diálogo com texto em preto
                        
                        # Desenha a seta amarela piscando se estiver visível
                        if is_pointer_visible:
                            screen.blit(seta_azul, pointer_position)

                    # Se o diálogo terminou, desativa a caixa de diálogo
                    if done and active_message == len(recepcionista_msg1) - 1:
                        player.velocidade = 3.5
                        bloqueio_progresso1_on = False
                        recepcionista_dialog_concluido = True
                        active_message = 0  # (Opcional) Reseta o índice do texto
                        counter = 0  # Reseta o contador interno
                        done = False  # Reseta o status de conclusão
                        dialogo_ativo = False  # Finaliza o diálogo
                        
            # Interação com a atendente ao pressionar 'E'
            if player.hitbox.colliderect(atendente_dialogo):
                if teclas[pygame.K_RETURN]:  # Quando o jogador pressiona 'E'
                    if not dialogo_ativo:  # Se o diálogo não está ativo, inicia o diálogo
                        dialogo_ativo = True
                        active_message = 0  # Reinicia a mensagem ativa
                        counter = 0  # Reinicia o contador
                        done = False  # Define que o diálogo não terminou

                if dialogo_ativo:
                    player.velocidade = 0
                    screen.blit(dialog_box, (0, 800))  # Desenha a caixa de diálogo
                    screen.blit(press_enter, (35, 750))  # Desenha "pressione E para prosseguir"
                    if active_message < len(atendente_msg1):  # Verifica se há mensagens para serem exibidas
                        active_message, counter, done = dialogo(screen, atendente_msg1, active_message, counter, 
                                                                x=85, y=905, speed=3, text_color=(0, 0, 0))  # Configura o diálogo com texto em preto  # Configura o diálogo com texto em preto
                                                                
                        # Desenha a seta amarela piscando se estiver visível
                        if is_pointer_visible:
                            screen.blit(seta_azul, pointer_position)

                    # Se o diálogo terminou, desativa a caixa de diálogo
                    if done and active_message == len(atendente_msg1) - 1:
                        player.velocidade = 3.5
                        bloqueio_progresso2_on = False
                        atendente_dialog_concluido = True
                        active_message = 0  # (Opcional) Reseta o índice do texto
                        counter = 0  # Reseta o contador interno
                        done = False  # Reseta o status de conclusão
                        dialogo_ativo = False  # Finaliza o diálogo
            
                        
            # Verifica colisão com escada para o primeiro andar
            if player.hitbox.colliderect(subir_primeiro_andar_c4):
                cena = "primeiro_andar"  # Se colidir com a escada, cena muda para primeiro andar
                player.x = subir_primeiro_andar_x
                player.y = subir_primeiro_andar_y
            
            # Verifica colisão com a saída para a rua
            if player.hitbox.colliderect(saida_terreo):
                cena = "rua"  # Se colidir com a porta, muda para o cenário da rua
                player.x = saida_terreo_x
                player.y = saida_terreo_y

            # Verifica colisão com a saída para o corredor da biblioteca
            if player.hitbox.colliderect(corredor_entrada):
                cena = "corredor"  # Se colidir com a porta, muda para o cenário da rua
                player.x = corredor_entrada_x
                player.y = corredor_entrada_y
            
        # Atualiza a tela
        atualizar_tela()

    elif cena == "primeiro_andar":
        # Loop de eventos da cena "primeiro_andar"
        if pause:
            draw_pause(screen, menu_pause, pixelify_tiny, nome, personagem_escolhido)  # Exibe o menu de pausa

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Se o jogador clicar no botão de fechar a janela, o loop é encerrado
                loop = False
                sys.exit()  # Encerra o programa
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Se a tecla P for pressionada
                    # Alterna entre pausado e não pausado
                    if pause:
                        pause = False
                    else:
                        pause = True                        
                        
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Se o jogador clicar com o mouse, a posição do clique é capturada
                mousepos = pygame.mouse.get_pos()  # Pega as coordenadas do clique
                print(f'Coordenada: {mousepos}')  # Imprime as coordenadas na tela de console
                
                if pause and botao_continue.collidepoint(event.pos):
                    print("Continuar")  # Exibe mensagem no console
                    if pause:
                        pause = False
                    else:
                        pause = True
                if pause and botao_sair.collidepoint(event.pos):
                    loop = False


        if not pause:
            # Captura as teclas pressionadas fora do loop de eventos
            teclas = pygame.key.get_pressed()  # Retorna uma lista de teclas pressionadas atualmente
            
            novo_x = player.x  # Armazena a posição atual do personagem no eixo X
            novo_y = player.y  # Armazena a posição atual do personagem no eixo Y
            
            # Mover o player usando a classe MainCharacter
            player.mover(teclas)  # Atualiza a posição do personagem com base nas teclas pressionadas
            
            # Verificar colisões com as hitboxes definidas para o primeiro andar
            for hitbox in hitboxes_primeiro_andar:
                if player.hitbox.colliderect(hitbox):
                    # Se o personagem colidir com alguma hitbox, retorna à posição anterior
                    player.x = novo_x
                    player.y = novo_y
            
            tempo_atual = pygame.time.get_ticks()
            if tempo_atual - ultimo_tempo_piscar >= intervalo_piscar:
                azul_visivel = not azul_visivel
                ultimo_tempo_piscar = tempo_atual
       
            # Limpar a tela e desenhar o cenário do primeiro andar
            limpar_e_desenhar(primeiro_andar)  # Chama a função para limpar e desenhar o fundo do primeiro andar
            text = "Primeiro Andar"
            # Renderizar o texto (True é para ativar antialiasing)
            text_surface = pixelify_t.render(text, True, "white")
            screen.blit(text_surface, (20, 10))
            
            if dialogo_final_concluido and finalizacao:
                step = "Vá para o segundo andar."
                txt_surface = pixelify_t.render(step, True, "white")
                txt_x, txt_y = 1520, 10
                screen.blit(txt_surface, (txt_x, txt_y))
                if azul_visivel:
                    screen.blit(bola_azul, (txt_x - 25, txt_y + 15))
                                
            if not dialogo1_concluido:
                step = "Entre no laboratório de informática 107."
                txt_surface = pixelify_t.render(step, True, "white")
                txt_x, txt_y = 1300, 10
                screen.blit(txt_surface, (txt_x, txt_y))
                if azul_visivel:
                    screen.blit(bola_azul, (txt_x - 25, txt_y + 15))
                    screen.blit(seta_azul, (850, 165))
                  
            # Desenhar o player na tela
            player.desenhar_mainchar(screen)  # Desenha o sprite do personagem na tela
            
            if faxineira.npc_x > 52 and faxineira.npc_x < 1815:
                desenhar_npc(faxineira)
            
            faxineira.mover_npc()
        
            # Verificar se o personagem está colidindo com a hitbox que representa a escada para descer
            if player.hitbox.colliderect(descer_escada_1andar):
                # Se o personagem colidir com a área da escada, muda para a cena do térreo
                cena = "terreo"  # Altera para a cena do térreo
                player.x = descer_escada_1andar_x  # Define a nova posição X do personagem ao descer a escada
                player.y = descer_escada_1andar_y  # Define a nova posição Y do personagem ao descer a escada
                player.ultima_direcao = "baixo"  # Define a última direção como "baixo", pois o personagem desce para baixo

            # Verificar se o personagem está colidindo com a hitbox que representa a escada para descer
            if player.hitbox.colliderect(subir_segundo_andar):
                # Se o personagem colidir com a área da escada, muda para a cena do segimdp andar
                cena = "segundo_andar"  # Altera para a cena do térreo
                player.x = subir_segundo_andar_x  # Define a nova posição X do personagem ao descer a escada
                player.y = subir_segundo_andar_y  # Define a nova posição Y do personagem ao descer a escada
                player.ultima_direcao = "baixo"  # Define a última direção como "baixo", pois o personagem desce para baixo
            
            # Verificar se o personagem está colidindo com a hitbox que representa a entrada da sala de informática 1
            if player.hitbox.colliderect(entrada_sala_informatica):
                # Se o personagem colidir com a área da entrada, muda para a cena da sala de informática 1
                cena = "informatica"  # Altera para a cena da sala de informática 1
                player.x = entrada_sala_informatica_x  # Define a nova posição X do personagem na entrada da sala
                player.y = entrada_sala_informatica_y  # Define a nova posição Y do personagem na entrada da sala
                player.ultima_direcao = "baixo"  # Define a última direção como "baixo", pois o personagem entra para baixo
            
            # Verificar se o personagem está colidindo com a hitbox que representa a entrada da sala de informática 2
            if player.hitbox.colliderect(entrada_sala_informatica2):
                # Se o personagem colidir com a área da entrada, muda para a cena da sala de informática 2
                cena = "informatica2"  # Altera para a cena da sala de informática 2
                player.x = entrada_sala_informatica2_x  # Define a nova posição X do personagem na entrada da sala
                player.y = entrada_sala_informatica2_y  # Define a nova posição Y do personagem na entrada da sala
                player.ultima_direcao = "baixo"  # Define a última direção como "baixo", pois o personagem entra para baixo
            
            # Verificar se o personagem está colidindo com a hitbox que representa a entrada da sala de aprendizagem 1
            if player.hitbox.colliderect(entrada_sala_aprendizagem):
                # Se o personagem colidir com a área da entrada, muda para a cena da sala de aprendizagem 1
                cena = "aprendizagem"  # Altera para a cena da sala de aprendizagem 1
                player.x = entrada_sala_aprendizagem_x  # Define a nova posição X do personagem na entrada da sala
                player.y = entrada_sala_aprendizagem_y  # Define a nova posição Y do personagem na entrada da sala
                player.ultima_direcao = "baixo"  # Define a última direção como "baixo", pois o personagem entra para baixo
            
            # Verificar se o personagem está colidindo com a hitbox que representa a entrada da sala de aprendizagem 2
            if player.hitbox.colliderect(entrada_sala_aprendizagem2):
                # Se o personagem colidir com a área da entrada, muda para a cena da sala de aprendizagem 2
                cena = "aprendizagem2"  # Altera para a cena da sala de aprendizagem 2
                player.x = entrada_sala_aprendizagem2_x  # Define a nova posição X do personagem na entrada da sala
                player.y = entrada_sala_aprendizagem2_y  # Define a nova posição Y do personagem na entrada da sala
                player.ultima_direcao = "baixo"  # Define a última direção como "baixo", pois o personagem entra para baixo

        # Atualiza a tela e os Frames
        atualizar_tela()  # Atualiza a tela com as mudanças realizadas

    elif cena == "informatica":
        entrou_inf1 = True

        if pause:
            draw_pause(screen, menu_pause, pixelify_tiny, nome, personagem_escolhido)  # Exibe o menu de pausa


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pass
                elif event.key == pygame.K_p:
                    pause = not pause
                elif event.key == pygame.K_RETURN:
                    if dialogo_ativo:
                        if not puzzle1_concluido and active_message < len(dialogo1_professor) - 1:
                            active_message += 1
                            counter = 0
                            done = False
                        elif puzzle1_concluido and not puzzle2_concluido and active_message < len(dialogo2_professor) - 1:
                            active_message += 1
                            counter = 0
                            done = False
                        elif puzzle2_concluido and not puzzle3_concluido and active_message < len(dialogo3_professor) - 1:
                            active_message += 1
                            counter = 0
                            done = False
                        elif puzzle3_concluido and dialogo3_concluido and active_message < len(dialogo_final_professor) - 1:
                            active_message += 1
                            counter = 0
                            done = False

            elif event.type == pygame.MOUSEBUTTONDOWN and pause:
                if botao_continue.collidepoint(event.pos):
                    pause = not pause
                elif botao_sair.collidepoint(event.pos):
                    loop = False

        current_time_seta = pygame.time.get_ticks()
        if current_time_seta - last_blink_time_seta >= blink_interval_seta:
            is_pointer_visible = not is_pointer_visible
            last_blink_time_seta = current_time_seta

        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - ultimo_tempo_piscar >= intervalo_piscar:
            azul_visivel = not azul_visivel
            ultimo_tempo_piscar = tempo_atual

        if not pause:
            if puzzle1_ativo:
                if not fase1.acertou:
                    fase1.executar(screen, event)
                elif not fase2.acertou:
                    fase2.executar(screen, event)
                elif not fase3.acertou:
                    fase3.executar(screen, event)
                elif not fase4.acertou:
                    fase4.executar(screen, event)
                elif not fase5.acertou:
                    fase5.executar(screen, event)
                elif not fase6.acertou:
                    fase6.executar(screen, event)
                elif not fase7.acertou:
                    fase7.executar(screen, event)
                elif not fase8.acertou:
                    fase8.executar(screen, event)
                else:
                    puzzle1_ativo = False
                    puzzle1_concluido = True
                    
            elif puzzle2_ativo and puzzle2.rodando:
                puzzle2.executar(screen, event)
                # Caso o puzzle termine
                if not puzzle2.rodando:
                    puzzle2_ativo = False
                    puzzle2_concluido = True
                    
            elif puzzle3_ativo and puzzle3.rodando:
                puzzle3.executar(screen, event)
                if not puzzle3.rodando:
                    puzzle3_ativo = False
                    puzzle3_concluido = True
                        
            else:
                teclas = pygame.key.get_pressed()
                novo_x, novo_y = player.x, player.y

                player.mover(teclas)

                for hitbox in hitboxes_informatica1:
                    if player.hitbox.colliderect(hitbox):
                        player.x, player.y = novo_x, novo_y
                

                if not dialogo_final_concluido:
                    limpar_e_desenhar(sala_informatica1)
                    if player.hitbox.colliderect(hitbox_professor):
                        player.x, player.y = novo_x, novo_y
                else:
                    limpar_e_desenhar(sala_informatica_vazia)
                    sala_vazia_on = True
                
                # Texto a ser renderizado
                text = "Laboratório de Informática 107"
                # Renderizar o texto (True é para ativar antialiasing)
                text_surface = pixelify_t.render(text, True, "white")
                screen.blit(text_surface, (15, 10))
                player.desenhar_mainchar(screen)
                screen.blit(parede_sala_informatica, (321, 890))
                
                if not dialogo1_concluido:
                    step = "Fale com o professor utilizando a tecla ENTER."
                    txt_surface = pixelify_t.render(step, True, "white")
                    txt_x, txt_y = 1220, 10
                    screen.blit(txt_surface, (txt_x, txt_y))
                    if azul_visivel:
                        screen.blit(bola_azul, (txt_x - 25, txt_y + 15))
                
                if dialogo1_concluido and not puzzle1_concluido:
                    step = "Sente-se na cadeira utilizando a tecla ENTER."
                    txt_surface = pixelify_t.render(step, True, "white")
                    txt_x, txt_y = 1240, 10
                    screen.blit(txt_surface, (txt_x, txt_y))
                    if azul_visivel:
                        screen.blit(seta_azul, (800, 410))
                        screen.blit(bola_azul, (txt_x - 25, txt_y + 15))
                
                if dialogo1_concluido and puzzle1_concluido and not dialogo2_concluido:
                    step = "Fale com o professor novamente."
                    txt_surface = pixelify_t.render(step, True, "white")
                    txt_x, txt_y = 1410, 10
                    screen.blit(txt_surface, (txt_x, txt_y))
                    if azul_visivel:
                        screen.blit(bola_azul, (txt_x - 25, txt_y + 15))

                if dialogo2_concluido and not puzzle2_concluido:
                    step = "Realize a segunda atividade."
                    txt_surface = pixelify_t.render(step, True, "white")
                    txt_x, txt_y = 1490, 10
                    screen.blit(txt_surface, (txt_x, txt_y))
                    if azul_visivel:
                        screen.blit(seta_azul, (800, 410))
                        screen.blit(bola_azul, (txt_x - 25, txt_y + 15))

                if dialogo2_concluido and puzzle2_concluido and not dialogo3_concluido:
                    step = "Fale com o professor novamente."
                    txt_surface = pixelify_t.render(step, True, "white")
                    txt_x, txt_y = 1410, 10
                    screen.blit(txt_surface, (txt_x, txt_y))
                    if azul_visivel:
                        screen.blit(bola_azul, (txt_x - 25, txt_y + 15))
                
                if puzzle2_concluido and dialogo3_concluido and not puzzle3_concluido:
                    step = "Realize a terceira atividade."
                    txt_surface = pixelify_t.render(step, True, "white")
                    txt_x, txt_y = 1480, 10
                    screen.blit(txt_surface, (txt_x, txt_y))
                    if azul_visivel:
                        screen.blit(seta_azul, (800, 410))
                        screen.blit(bola_azul, (txt_x - 25, txt_y + 15))
                        
                if dialogo3_concluido and puzzle3_concluido and not dialogo_final_concluido:
                    step = "Fale com o professor novamente."
                    txt_surface = pixelify_t.render(step, True, "white")
                    txt_x, txt_y = 1410, 10
                    screen.blit(txt_surface, (txt_x, txt_y))
                    if azul_visivel:
                        screen.blit(bola_azul, (txt_x - 25, txt_y + 15))

                if dialogo_final_concluido and finalizacao:
                    step = "Vá para o segundo andar."
                    txt_surface = pixelify_t.render(step, True, "white")
                    txt_x, txt_y = 1520, 10
                    screen.blit(txt_surface, (txt_x, txt_y))
                    if azul_visivel:
                        screen.blit(bola_azul, (txt_x - 25, txt_y + 15))
                        
                if player.hitbox.colliderect(interacao_professor) and not sala_vazia_on:
                    if teclas[pygame.K_RETURN] and not dialogo_ativo:
                        dialogo_ativo = True
                        active_message = 0
                        counter = 0
                        done = False

                    if dialogo_ativo:
                        screen.blit(tela_introducao, (0, 0))
                        screen.blit(dialog_box, (0, 800))
                        screen.blit(press_enter, (35, 750))
                        screen.blit(portrait_professor, (1500, 250))

                        if not puzzle1_concluido and active_message < len(dialogo1_professor):
                            active_message, counter, done = dialogo(screen, dialogo1_professor, 
                                                                    active_message, counter, x=65, y=905, speed=3, text_color=(0, 0, 0))

                            if is_pointer_visible:
                                screen.blit(seta_azul, pointer_position)

                            if done and active_message == len(dialogo1_professor) - 1:
                                dialogo1_concluido = True
                                dialogo_ativo = False
                                active_message = 0
                                counter = 0
                                done = False
                        
                        elif dialogo1_concluido and puzzle1_concluido and not puzzle2_concluido and active_message < len(dialogo2_professor):
                            active_message, counter, done = dialogo(screen, dialogo2_professor, active_message, 
                                                                    counter, x=65, y=905, speed=3, text_color=(0, 0, 0))

                            if is_pointer_visible:
                                screen.blit(seta_azul, pointer_position)

                            if done and active_message == len(dialogo2_professor) - 1:
                                dialogo2_concluido = True
                                dialogo_ativo = False
                                active_message = 0
                                counter = 0
                                done = False

                        elif dialogo2_concluido and puzzle2_concluido and not puzzle3_concluido and active_message < len(dialogo3_professor):
                            active_message, counter, done = dialogo(screen, dialogo3_professor, active_message, 
                                                                    counter, x=65, y=905, speed=3, text_color=(0, 0, 0))

                            if is_pointer_visible:
                                screen.blit(seta_azul, pointer_position)

                            if done and active_message == len(dialogo3_professor) - 1:
                                dialogo3_concluido = True
                                dialogo_ativo = False
                                active_message = 0
                                counter = 0
                                done = False

                        elif puzzle3_concluido and dialogo3_concluido and active_message < len(dialogo_final_professor):
                            active_message, counter, done = dialogo(screen, dialogo_final_professor, active_message, 
                                                                    counter, x=65, y=905, speed=3, text_color=(0, 0, 0))

                            if is_pointer_visible:
                                screen.blit(seta_azul, pointer_position)

                            if done and active_message == len(dialogo_final_professor) - 1:
                                dialogo_final_concluido = True
                                finalizacao = True
                                dialogo_ativo = False
                                active_message = 0
                                counter = 0
                                done = False

                if player.hitbox.colliderect(hitbox_pc):
                    if teclas[pygame.K_RETURN]:
                        if not puzzle1_ativo and dialogo1_concluido:
                            puzzle1_ativo = True
                        if not puzzle2_ativo and dialogo2_concluido:
                            puzzle2_ativo = True
                        if not puzzle3_ativo and dialogo3_concluido:
                            puzzle3_ativo = True

                if player.hitbox.colliderect(sair_da_sala_inf1):
                    cena = "primeiro_andar"
                    player.x = sair_da_sala_inf1_x
                    player.y = sair_da_sala_inf1_y
                    ultima_direcao = "baixo"

        atualizar_tela()

    elif cena == "informatica2":
        # Loop de eventos da cena "informatica2"
        if pause:
            draw_pause(screen, menu_pause, pixelify_tiny, nome, personagem_escolhido)  # Exibe o menu de pausa

            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Se o jogador clicar no botão de fechar a janela, o loop é encerrado
                loop = False
                sys.exit()  # Encerra o programa
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_p:  # Se a tecla P for pressionada
                    # Alterna entre pausado e não pausado
                    if pause:
                        pause = False
                    else:
                        pause = True
                        
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Se o jogador clicar com o mouse, a posição do clique é capturada
                mousepos = pygame.mouse.get_pos()  # Pega as coordenadas do clique
                print(f'Coordenada: {mousepos}')  # Imprime as coordenadas na tela de console
                
                if pause and botao_continue.collidepoint(event.pos):
                    print("Continuar")  # Exibe mensagem no console
                    if pause:
                        pause = False
                    else:
                        pause = True
                if pause and botao_sair.collidepoint(event.pos):
                    loop = False
                    
        if not pause:
            # Captura as teclas pressionadas fora do loop de eventos
            teclas = pygame.key.get_pressed()  # Retorna uma lista de teclas pressionadas atualmente
            
            novo_x = player.x  # Armazena a posição atual do personagem no eixo X
            novo_y = player.y  # Armazena a posição atual do personagem no eixo Y
            
            # Mover o player usando a classe MainCharacter
            player.mover(teclas)  # Atualiza a posição do personagem com base nas teclas pressionadas
            
            # Verificar colisões com as hitboxes definidas
            for hitbox in hitboxes_informatica2:
                if player.hitbox.colliderect(hitbox):
                    # Se o personagem colidir com alguma hitbox, retorna à posição anterior
                    player.x = novo_x
                    player.y = novo_y
                
                
            tempo_atual = pygame.time.get_ticks()
            if tempo_atual - ultimo_tempo_piscar >= intervalo_piscar:
                azul_visivel = not azul_visivel
                ultimo_tempo_piscar = tempo_atual
                    
            # Limpar a tela e desenhar o cenário
            limpar_e_desenhar(sala_informatica2)  # Chama a função para limpar e desenhar o fundo da sala de informática 2
            text = "Laboratório de Informática 105"
            # Renderizar o texto (True é para ativar antialiasing)
            text_surface = pixelify_t.render(text, True, "white")
            screen.blit(text_surface, (20, 10)) 
            player.desenhar_mainchar(screen)  # Desenha o sprite do personagem na tela
            screen.blit(parede_sala_informatica2, (338, 930))  # Desenha a mesa na sala de informática 1
            
            if not dialogo1_concluido:
                step = "Entre no laboratório de informática 107."
                txt_surface = pixelify_t.render(step, True, "white")
                txt_x, txt_y = 1300, 10
                screen.blit(txt_surface, (txt_x, txt_y))
                if azul_visivel:
                    screen.blit(bola_azul, (txt_x - 25, txt_y + 15))
            
            #for hitbox in hitboxes_informatica2:
                #pygame.draw.rect(screen, (255, 0, 0), hitbox, 2)
            
            # Verificar se o personagem está colidindo com a hitbox que representa a saída da sala
            if player.hitbox.colliderect(sair_da_sala_inf2):
                # Se o personagem colidir com a área de saída, muda para a próxima cena
                cena = "primeiro_andar"  # Altera para a cena do primeiro andar
                player.x = sair_da_sala_inf2_x  # Define a nova posição X do personagem na saída
                player.y = sair_da_sala_inf2_y  # Define a nova posição Y do personagem na saída
                ultima_direcao = "baixo"  # Define a última direção como "baixo", pois o personagem sai para baixo

        # Atualiza a tela e os Frames
        atualizar_tela()  # Atualiza a tela com as mudanças realizadas

    elif cena == "aprendizagem":
        # Loop de eventos da cena "aprendizagem"
        if pause:
            draw_pause(screen, menu_pause, pixelify_tiny, nome, personagem_escolhido)  # Exibe o menu de pausa

            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Se o jogador clicar no botão de fechar a janela, o loop é encerrado
                loop = False
                sys.exit()  # Encerra o programa
            if event.type == pygame.KEYDOWN:       
                if event.key == pygame.K_p:  # Se a tecla P for pressionada
                    # Alterna entre pausado e não pausado
                    if pause:
                        pause = False
                    else:
                        pause = True
                        
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Se o jogador clicar com o mouse, a posição do clique é capturada
                mousepos = pygame.mouse.get_pos()  # Pega as coordenadas do clique
                print(f'Coordenada: {mousepos}')  # Imprime as coordenadas na tela de console
                
                if pause and botao_continue.collidepoint(event.pos):
                    print("Continuar")  # Exibe mensagem no console
                    if pause:
                        pause = False
                    else:
                        pause = True
                if pause and botao_sair.collidepoint(event.pos):
                    loop = False
        
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - ultimo_tempo_piscar >= intervalo_piscar:
            azul_visivel = not azul_visivel
            ultimo_tempo_piscar=tempo_atual
        
        if not pause:
            # Captura as teclas pressionadas fora do loop de eventos
            teclas = pygame.key.get_pressed()  # Retorna uma lista de teclas pressionadas atualmente
            
            novo_x = player.x  # Armazena a posição atual do personagem no eixo X
            novo_y = player.y  # Armazena a posição atual do personagem no eixo Y
            
            # Mover o player usando a classe MainCharacter
            player.mover(teclas)  # Atualiza a posição do personagem com base nas teclas pressionadas
            
            # Verificar colisões com as hitboxes definidas
            for hitbox in hitboxes_apredizagem1:
                if player.hitbox.colliderect(hitbox):
                    # Se o personagem colidir com alguma hitbox, retorna à posição anterior
                    player.x = novo_x
                    player.y = novo_y
                    
            # Limpar a tela e desenhar o cenário
            limpar_e_desenhar(aprendizagem1)  # Chama a função para limpar e desenhar o fundo da sala de aprendizagem 1
            text = "Sala de aprendizagem 111"
            # Renderizar o texto (True é para ativar antialiasing)
            text_surface = pixelify_t.render(text, True, "white")
            screen.blit(text_surface, (20, 10))
            
            if not dialogo1_concluido:
                step = "Entre no laboratório de informática 107."
                txt_surface = pixelify_t.render(step, True, "white")
                txt_x, txt_y = 1300, 10
                screen.blit(txt_surface, (txt_x, txt_y))
                if azul_visivel:
                    screen.blit(bola_azul, (txt_x - 25, txt_y + 15))
            
            # Desenhar professor e personagem na tela
            screen.blit(npc78, (867, 179))
            player.desenhar_mainchar(screen)  # Desenha o sprite do personagem na tela
            
            # Chamada no loop
            for npc in npcs_ap1_f1:
                desenhar_npc(npc)
            for cadeira, posicao in cadeiras_f1:
                screen.blit(cadeira, posicao)
            
            for npc in npcs_ap1_f2:
                desenhar_npc(npc)
            for cadeira, posicao in cadeiras_f2:
                screen.blit(cadeira, posicao)
                
            for npc in npcs_ap1_f3:
                desenhar_npc(npc)
            for cadeira, posicao in cadeiras_f3:
                screen.blit(cadeira, posicao)

            for npc in npcs_ap1_f4:
                desenhar_npc(npc)
            for cadeira, posicao in cadeiras_f4:
                screen.blit(cadeira, posicao)

            # Verificar se o personagem está colidindo com a hitbox que representa a saída da sala de aprendizagem 1
            if player.hitbox.colliderect(sair_da_sala_ap1):
                # Se o personagem colidir com a área de saída, muda para a próxima cena
                cena = "primeiro_andar"  # Altera para a cena do primeiro andar
                player.x = sair_da_sala_ap1_x  # Define a nova posição X do personagem na saída
                player.y = sair_da_sala_ap1_y  # Define a nova posição Y do personagem na saída
                ultima_direcao = "baixo"  # Define a última direção como "baixo", pois o personagem sai para baixo

        # Atualiza a tela e os Frames
        atualizar_tela()  # Atualiza a tela com as mudanças realizadas
    
    elif cena == "aprendizagem2":
        # Loop de eventos da cena "aprendizagem2"
        if pause:
            draw_pause(screen, menu_pause, pixelify_tiny, nome, personagem_escolhido)  # Exibe o menu de pausa

            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Se o jogador clicar no botão de fechar a janela, o loop é encerrado
                loop = False
                sys.exit()  # Encerra o programa
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_p:  # Se a tecla P for pressionada
                    # Alterna entre pausado e não pausado
                    if pause:
                        pause = False
                    else:
                        pause = True
                        
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Se o jogador clicar com o mouse, a posição do clique é capturada
                mousepos = pygame.mouse.get_pos()  # Pega as coordenadas do clique
                print(f'Coordenada: {mousepos}')  # Imprime as coordenadas na tela de console
                
                if pause and botao_continue.collidepoint(event.pos):
                    print("Continuar")  # Exibe mensagem no console
                    if pause:
                        pause = False
                    else:
                        pause = True
                if pause and botao_sair.collidepoint(event.pos):
                    loop = False
                    
        if not pause:
            # Captura as teclas pressionadas fora do loop de eventos
            teclas = pygame.key.get_pressed()  # Retorna uma lista de teclas pressionadas atualmente
            
            novo_x = player.x  # Armazena a posição atual do personagem no eixo X
            novo_y = player.y  # Armazena a posição atual do personagem no eixo Y
            
            # Mover o player usando a classe MainCharacter
            player.mover(teclas)  # Atualiza a posição do personagem com base nas teclas pressionadas
            
            # Verificar colisões com as hitboxes definidas
            for hitbox in hitboxes_apredizagem1:
                if player.hitbox.colliderect(hitbox):
                    # Se o personagem colidir com alguma hitbox, retorna à posição anterior
                    player.x = novo_x
                    player.y = novo_y
                    
            # Limpar a tela e desenhar o cenário
            limpar_e_desenhar(aprendizagem2)  # Chama a função para limpar e desenhar o fundo da sala de aprendizagem 2
            desenhar_npc(npc20)  # Professora
            
            # Renderizar o texto (True é para ativar antialiasing)
            text = "Sala de aprendizagem 109"
            text_surface = pixelify_t.render(text, True, "white")
            screen.blit(text_surface, (20, 10))
            
            tempo_atual = pygame.time.get_ticks()
            if tempo_atual - ultimo_tempo_piscar >= intervalo_piscar:
                azul_visivel = not azul_visivel
                ultimo_tempo_piscar=tempo_atual
                
            if not dialogo1_concluido:
                step = "Entre no laboratório de informática 107."
                txt_surface = pixelify_t.render(step, True, "white")
                txt_x, txt_y = 1300, 10
                screen.blit(txt_surface, (txt_x, txt_y))
                if azul_visivel:
                    screen.blit(bola_azul, (txt_x - 25, txt_y + 15))
            
            # Desenhar o player na tela
            player.desenhar_mainchar(screen)  # Desenha o sprite do personagem na tela
            
           # Chamada no loop
            for npc in npcs_ap2_f1:
                desenhar_npc(npc)
            for cadeira, posicao in cadeiras_f1:
                screen.blit(cadeira, posicao)
            
            for npc in npcs_ap2_f2:
                desenhar_npc(npc)
            for cadeira, posicao in cadeiras_f2:
                screen.blit(cadeira, posicao)
                
            for npc in npcs_ap2_f3:
                desenhar_npc(npc)
            for cadeira, posicao in cadeiras_f3:
                screen.blit(cadeira, posicao)

            for npc in npcs_ap2_f4:
                desenhar_npc(npc)
            for cadeira, posicao in cadeiras_f4:
                screen.blit(cadeira, posicao)

            # Verificar se o personagem está colidindo com a hitbox que representa a saída da sala de aprendizagem 2
            if player.hitbox.colliderect(sair_da_sala_ap2):
                # Se o personagem colidir com a área de saída, muda para a próxima cena
                cena = "primeiro_andar"  # Altera para a cena do primeiro andar
                player.x = sair_da_sala_ap2_x  # Define a nova posição X do personagem na saída
                player.y = sair_da_sala_ap2_y  # Define a nova posição Y do personagem na saída
                ultima_direcao = "baixo"  # Define a última direção como "baixo", pois o personagem sai para baixo

        # Atualiza a tela e os Frames
        atualizar_tela()  # Atualiza a tela com as mudanças realizadas
    
    elif cena == "segundo_andar":
        # Loop de eventos da cena "aprendizagem2"
        if pause:
            draw_pause(screen, menu_pause, pixelify_tiny, nome, personagem_escolhido)  # Exibe o menu de pausa

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Se o jogador clicar no botão de fechar a janela, o loop é encerrado
                loop = False
                sys.exit()  # Encerra o programa
            if event.type == pygame.KEYDOWN:       
                if event.key == pygame.K_p:  # Se a tecla P for pressionada
                    # Alterna entre pausado e não pausado
                    if pause:
                        pause = False
                    else:
                        pause = True
                        
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Se o jogador clicar com o mouse, a posição do clique é capturada
                mousepos = pygame.mouse.get_pos()  # Pega as coordenadas do clique
                print(f'Coordenada: {mousepos}')  # Imprime as coordenadas na tela de console
                
                if pause and botao_continue.collidepoint(event.pos):
                    print("Continuar")  # Exibe mensagem no console
                    if pause:
                        pause = False
                    else:
                        pause = True
                if pause and botao_sair.collidepoint(event.pos):
                    loop = False
                    
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - ultimo_tempo_piscar >= intervalo_piscar:
            azul_visivel = not azul_visivel
            ultimo_tempo_piscar = tempo_atual
                        
        if not pause:
            # Captura as teclas pressionadas fora do loop de eventos
            teclas = pygame.key.get_pressed()  # Retorna uma lista de teclas pressionadas atualmente
            
            novo_x = player.x  # Armazena a posição atual do personagem no eixo X
            novo_y = player.y  # Armazena a posição atual do personagem no eixo Y
            
            # Mover o player usando a classe MainCharacter
            player.mover(teclas)  # Atualiza a posição do personagem com base nas teclas pressionadas
            
            # Verificar colisões com as hitboxes definidas
            for hitbox in hitboxes_segundo_andar:
                if player.hitbox.colliderect(hitbox):
                    # Se o personagem colidir com alguma hitbox, retorna à posição anterior
                    player.x = novo_x
                    player.y = novo_y
                    
            # Limpar a tela e desenhar o cenário
            limpar_e_desenhar(segundo_andar)  # Chama a função para limpar e desenhar o fundo do segundo andar
            # Renderizar o texto (True é para ativar antialiasing)
            text = "Segundo Andar"
            text_surface = pixelify_t.render(text, True, "white")
            screen.blit(text_surface, (20, 10))
            
            tempo_atual = pygame.time.get_ticks()
            if tempo_atual - ultimo_tempo_piscar >= intervalo_piscar:
                azul_visivel = not azul_visivel
                ultimo_tempo_piscar=tempo_atual
                
            if not dialogo1_concluido:
                step = "Entre no laboratório de informática 107."
                txt_surface = pixelify_t.render(step, True, "white")
                txt_x, txt_y = 1300, 10
                screen.blit(txt_surface, (txt_x, txt_y))
                if azul_visivel:
                    screen.blit(bola_azul, (txt_x - 25, txt_y + 15))
            
            if dialogo_final_concluido and finalizacao:
                step = "Entre no auditório."
                txt_surface = pixelify_t.render(step, True, "white")
                txt_x, txt_y = 1620, 10
                screen.blit(txt_surface, (txt_x, txt_y))
                if azul_visivel:
                    screen.blit(bola_azul, (txt_x - 25, txt_y + 15))
                            
            if not entrou_auditorio and dialogo_final_concluido:
                if azul_visivel:
                    screen.blit(seta_azul, (560, 225))
            
            # Desenhar o player na tela
            player.desenhar_mainchar(screen)  # Desenha o sprite do personagem na tela
            
            # Verificar se o personagem está colidindo com a hitbox que representa a descida para o primeiro andar
            if player.hitbox.colliderect(descer_escada_2andar):
                # Se o personagem colidir com a área da entrada, muda para a cena do primeiro andar
                cena = "primeiro_andar"  # Altera para a cena do primeiro andar
                player.x = descer_escada_2andar_x  # Define a nova posição X do personagem na entrada da sala
                player.y = descer_escada_2andar_y  # Define a nova posição Y do personagem na entrada da sala

            # Verificar se o personagem está colidindo com a hitbox que representa a entrada para o auditorio
            if dialogo_final_concluido and player.hitbox.colliderect(entrada_auditorio):
                # Se o personagem colidir com a área da entrada, muda para a cena do auditorio
                cena = "auditorio"  # Altera para a cena do auditorio
                player.x = entrada_auditorio_x  # Define a nova posição X do personagem na entrada da sala
                player.y = entrada_auditorio_y  # Define a nova posição Y do personagem na entrada da sala

            # Verificar se o personagem está colidindo com a hitbox que representa a entrada para a sala vazia1
            if player.hitbox.colliderect(entrada_sala_vazia1):
                # Se o personagem colidir com a área da entrada, muda para a cena da sala vazia1
                cena = "sala_vazia1"  # Altera para a cena da sala vazia1
                player.x = entrada_sala_vazia1_x  # Define a nova posição X do personagem na entrada da sala
                player.y = entrada_sala_vazia1_y  # Define a nova posição Y do personagem na entrada da sala

            # Verificar se o personagem está colidindo com a hitbox que representa a entrada para a sala vazia2
            if player.hitbox.colliderect(entrada_sala_vazia2):
                # Se o personagem colidir com a área da entrada, muda para a cena da sala vazia2
                cena = "sala_vazia2"  # Altera para a cena da sala vazia2
                player.x = entrada_sala_vazia2_x  # Define a nova posição X do personagem na entrada da sala
                player.y = entrada_sala_vazia2_y  # Define a nova posição Y do personagem na entrada da sala
            
        # Atualiza a tela e os Frames
        atualizar_tela()  # Atualiza a tela com as mudanças realizadas   

    elif cena == "creditos":
        # Loop de eventos da cena "introducao"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Se o jogador clicar no botão de fechar a janela, o loop é encerrado
                loop = False
                sys.exit()  # Encerra o programa
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Se o jogador clicar com o mouse, a posição do clique é capturada
                mousepos = pygame.mouse.get_pos()  # Pega as coordenadas do clique
                print(f'Coordenada: {mousepos}')  # Imprime as coordenadas na tela de console
        
        # Lógica para alternar visiblidade do balão de tutorial
        tempo_atual = pygame.time.get_ticks()  # Obtém o tempo atual em milissegundos
        if tempo_atual - last_time >= intervalo:  # Verifica o intervalo
            visivel = not visivel  # Alterna a visibilidade
            last_time = tempo_atual  # Atualiza o último momento de alteração
        
        # Limpar a tela e desenhar o cenário
        screen.fill(PRETO)
        
        # Desenhar o texto na tela
        for i, linha in enumerate(creditos_render):
            screen.blit(linha, (50, posicao_y + i * 50))

        # Atualizar a posição do texto
        posicao_y -= velocidade

        '''# Reiniciar os créditos quando eles saírem da tela
        if posicao_y + len(creditos_render) * 50 < 0:
            posicao_y = ALTURA'''
        
        # Atualiza a tela e os Frames
        atualizar_tela()  # Atualiza a tela com as mudanças realizadas

    elif cena == "corredor":
        # Loop de eventos da cena "aprendizagem"
        if pause:
            draw_pause(screen, menu_pause, pixelify_tiny, nome, personagem_escolhido)  # Exibe o menu de pausa

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Se o jogador clicar no botão de fechar a janela, o loop é encerrado
                loop = False
                sys.exit()  # Encerra o programa
                    
                if event.key == pygame.K_p:  # Se a tecla P for pressionada
                    # Alterna entre pausado e não pausado
                    if pause:
                        pause = False
                    else:
                        pause = True
                        
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Se o jogador clicar com o mouse, a posição do clique é capturada
                mousepos = pygame.mouse.get_pos()  # Pega as coordenadas do clique
                print(f'Coordenada: {mousepos}')  # Imprime as coordenadas na tela de console
                
                if pause and botao_continue.collidepoint(event.pos):
                    print("Continuar")  # Exibe mensagem no console
                    if pause:
                        pause = False
                    else:
                        pause = True
                if pause and botao_sair.collidepoint(event.pos):
                    loop = False
        
        if not pause:
            # Captura as teclas pressionadas fora do loop de eventos
            teclas = pygame.key.get_pressed()  # Retorna uma lista de teclas pressionadas atualmente
            
            novo_x = player.x  # Armazena a posição atual do personagem no eixo X
            novo_y = player.y  # Armazena a posição atual do personagem no eixo Y
            
            # Mover o player usando a classe MainCharacter
            player.mover(teclas)  # Atualiza a posição do personagem com base nas teclas pressionadas
                
            # Verificar colisões com as hitboxes definidas
            for hitbox in hitboxes_corredor:
                if player.hitbox.colliderect(hitbox):
                    # Se o personagem colidir com alguma hitbox, retorna à posição anterior
                    player.x = novo_x
                    player.y = novo_y
            
            # Limpar a tela e desenhar o cenário
            limpar_e_desenhar(corredor_fundo)  # Chama a função para limpar e desenhar o fundo
                
            # Renderizar o texto (True é para ativar antialiasing)
            text = "Corredor para biblioteca"
            text_surface = pixelify_t.render(text, True, "white")
            screen.blit(text_surface, (20, 10))

            player.desenhar_mainchar(screen)  # Desenha o sprite do personagem na tela
                    
            # Verifica colisão com a saída para o terre
            if player.hitbox.colliderect(corredor_saida):
                cena = "terreo"  # Se colidir com a porta, muda para o cenário da rua
                print("Saindo para o térreo")
                player.x = corredor_saida_x
                player.y = corredor_saida_y

            # Verifica colisão com a saída para o terre
            if player.hitbox.colliderect(entrada_biblioteca):
                cena = "biblioteca"  # Se colidir com a porta, muda para o cenário da rua
                print("Saindo para o térreo")
                player.x = entrada_biblioteca_x
                player.y = entrada_biblioteca_y
                
        # Atualiza a tela e os Frames
        atualizar_tela()  # Atualiza a tela com as mudanças realizadas

    elif cena == "sala_vazia1":
        # Loop de eventos da cena "aprendizagem"
        if pause:
            draw_pause(screen, menu_pause, pixelify_tiny, nome, personagem_escolhido)  # Exibe o menu de pausa
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Se o jogador clicar no botão de fechar a janela, o loop é encerrado
                loop = False
                sys.exit()  # Encerra o programa
            if event.type == pygame.KEYDOWN:                   
                if event.key == pygame.K_p:  # Se a tecla P for pressionada
                    # Alterna entre pausado e não pausado
                    if pause:
                        pause = False
                    else:
                        pause = True
                        
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Se o jogador clicar com o mouse, a posição do clique é capturada
                mousepos = pygame.mouse.get_pos()  # Pega as coordenadas do clique
                print(f'Coordenada: {mousepos}')  # Imprime as coordenadas na tela de console
                
                if pause and botao_continue.collidepoint(event.pos):
                    print("Continuar")  # Exibe mensagem no console
                    if pause:
                        pause = False
                    else:
                        pause = True
                if pause and botao_sair.collidepoint(event.pos):
                    loop = False
        
        if not pause:
            # Captura as teclas pressionadas fora do loop de eventos
            teclas = pygame.key.get_pressed()  # Retorna uma lista de teclas pressionadas atualmente
            
            novo_x = player.x  # Armazena a posição atual do personagem no eixo X
            novo_y = player.y  # Armazena a posição atual do personagem no eixo Y
            
            # Mover o player usando a classe MainCharacter
            player.mover(teclas)  # Atualiza a posição do personagem com base nas teclas pressionadas
                
            # Verificar colisões com as hitboxes definidas
            for hitbox in hitboxes_sala_vazia1:
                if player.hitbox.colliderect(hitbox):
                    # Se o personagem colidir com alguma hitbox, retorna à posição anterior
                    player.x = novo_x
                    player.y = novo_y
            
            # Limpar a tela e desenhar o cenário
            limpar_e_desenhar(sala_vazia1)  # Chama a função para limpar e desenhar o fundo
                
            # Renderizar o texto (True é para ativar antialiasing)
            text = "Sala Vazia"
            text_surface = pixelify_t.render(text, True, "white")
            screen.blit(text_surface, (20, 10))

            player.desenhar_mainchar(screen)  # Desenha o sprite do personagem na tela

            # Verifica colisão com a saída para o terre
            if player.hitbox.colliderect(sair_da_sala_v1):
                cena = "segundo_andar"  # Se colidir com a porta, muda para o cenário da rua
                print("Saindo para o térreo")
                player.x = sair_da_sala_v1_x
                player.y = sair_da_sala_v1_y
            
        # Atualiza a tela e os Frames
        atualizar_tela()  # Atualiza a tela com as mudanças realizadas

    elif cena == "sala_vazia2":
        # Loop de eventos da cena "aprendizagem"
        if pause:
            draw_pause(screen, menu_pause, pixelify_tiny, nome, personagem_escolhido)  # Exibe o menu de pausa
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Se o jogador clicar no botão de fechar a janela, o loop é encerrado
                loop = False
                sys.exit()  # Encerra o programa
            if event.type == pygame.KEYDOWN:                
                if event.key == pygame.K_p:  # Se a tecla P for pressionada
                    # Alterna entre pausado e não pausado
                    if pause:
                        pause = False
                    else:
                        pause = True
                        
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Se o jogador clicar com o mouse, a posição do clique é capturada
                mousepos = pygame.mouse.get_pos()  # Pega as coordenadas do clique
                print(f'Coordenada: {mousepos}')  # Imprime as coordenadas na tela de console
                
                if pause and botao_continue.collidepoint(event.pos):
                    print("Continuar")  # Exibe mensagem no console
                    if pause:
                        pause = False
                    else:
                        pause = True
                if pause and botao_sair.collidepoint(event.pos):
                    loop = False
        
        if not pause:
            # Captura as teclas pressionadas fora do loop de eventos
            teclas = pygame.key.get_pressed()  # Retorna uma lista de teclas pressionadas atualmente
            
            novo_x = player.x  # Armazena a posição atual do personagem no eixo X
            novo_y = player.y  # Armazena a posição atual do personagem no eixo Y
            
            # Mover o player usando a classe MainCharacter
            player.mover(teclas)  # Atualiza a posição do personagem com base nas teclas pressionadas
                
            # Verificar colisões com as hitboxes definidas
            for hitbox in hitboxes_sala_vazia1:
                if player.hitbox.colliderect(hitbox):
                    # Se o personagem colidir com alguma hitbox, retorna à posição anterior
                    player.x = novo_x
                    player.y = novo_y
            
            # Limpar a tela e desenhar o cenário
            limpar_e_desenhar(sala_vazia1)  # Chama a função para limpar e desenhar o fundo
                
            # Renderizar o texto (True é para ativar antialiasing)
            text = "Sala Vazia"
            text_surface = pixelify_t.render(text, True, "white")
            screen.blit(text_surface, (20, 10))

            player.desenhar_mainchar(screen)  # Desenha o sprite do personagem na tela

            # Verifica colisão com a saída para o terre
            if player.hitbox.colliderect(sair_da_sala_v2):
                cena = "segundo_andar"  # Se colidir com a porta, muda para o cenário da rua
                print("Saindo para o térreo")
                player.x = sair_da_sala_v2_x
                player.y = sair_da_sala_v2_y
            
        # Atualiza a tela e os Frames
        atualizar_tela()  # Atualiza a tela com as mudanças realizadas

    elif cena == "auditorio":
        entrou_auditorio = True
        # Loop de eventos da cena "auditório"
        if pause:
            draw_pause(screen, menu_pause, pixelify_tiny, nome, personagem_escolhido)  # Exibe o menu de pausa

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Se o jogador clicar no botão de fechar a janela, o loop é encerrado
                loop = False
                sys.exit()  # Encerra o programa
            if event.type == pygame.KEYDOWN:           
                if event.key == pygame.K_RETURN and done:
                    if active_message < len(msg_finalizacao) - 1:  # Se ainda há mensagens a serem exibidas
                        active_message += 1  # Avança para a próxima mensagem
                        counter = 0  # Reseta o contador de exibição
                        done = False  # Reseta o status de conclusão da mensagem atual
                    
                if event.key == pygame.K_p:  # Se a tecla P for pressionada
                    # Alterna entre pausado e não pausado
                    if pause:
                        pause = False
                    else:
                        pause = True
                        
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Se o jogador clicar com o mouse, a posição do clique é capturada
                mousepos = pygame.mouse.get_pos()  # Pega as coordenadas do clique
                print(f'Coordenada: {mousepos}')  # Imprime as coordenadas na tela de console
                
                if pause and botao_continue.collidepoint(event.pos):
                    print("Continuar")  # Exibe mensagem no console
                    if pause:
                        pause = False
                    else:
                        pause = True
                if pause and botao_sair.collidepoint(event.pos):
                    loop = False
                    
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - ultimo_tempo_piscar >= intervalo_piscar:
            azul_visivel = not azul_visivel
            ultimo_tempo_piscar = tempo_atual
        
        if not pause:
            # Captura as teclas pressionadas fora do loop de eventos
            teclas = pygame.key.get_pressed()  # Retorna uma lista de teclas pressionadas atualmente
            
            novo_x = player.x  # Armazena a posição atual do personagem no eixo X
            novo_y = player.y  # Armazena a posição atual do personagem no eixo Y
            
            # Mover o player usando a classe MainCharacter
            player.mover(teclas)  # Atualiza a posição do personagem com base nas teclas pressionadas
                
            # Verificar colisões com as hitboxes definidas
            for hitbox in hitboxes_auditorio:
                if player.hitbox.colliderect(hitbox):
                    # Se o personagem colidir com alguma hitbox, retorna à posição anterior
                    player.x = novo_x
                    player.y = novo_y
            
            # Limpar a tela e desenhar o cenário
            limpar_e_desenhar(auditorio_fundo)  # Chama a função para limpar e desenhar o fundo
            player.desenhar_mainchar(screen)  # Desenha o sprite do personagem na tela
            screen.blit(bandeiras, (424, 750))
            
            screen.blit(npc25.animacoes["cima"][0], (940, 775))

        
                
            #pygame.draw.rect(screen, "red", dialogo_finalizacao, 2)
            
            # Renderizar o texto (True é para ativar antialiasing)
            text = "Auditório"
            text_surface = pixelify_t.render(text, True, "white")
            screen.blit(text_surface, (20, 10))
                
            # Interação com a recepcionista ao pressionar 'E'
            if player.hitbox.colliderect(dialogo_finalizacao):
                if teclas[pygame.K_RETURN]:  # Quando o jogador pressiona 'E'
                    if not dialogo_ativo:  # Se o diálogo não está ativo, inicia o diálogo
                        dialogo_ativo = True
                        active_message = 0  # Reinicia a mensagem ativa
                        counter = 0  # Reinicia o contador
                        done = False  # Define que o diálogo não terminou

                if dialogo_ativo:
                    player.velocidade = 0
                    screen.blit(dialog_box, (0, 800))  # Desenha a caixa de diálogo
                    screen.blit(press_enter, (35, 750))  # Desenha "pressione E para prosseguir"
                    if active_message < len(msg_finalizacao):  # Verifica se há mensagens para serem exibidas
                        active_message, counter, done = dialogo(screen, msg_finalizacao, active_message, counter, 
                                                                x=85, y=905, speed=3, text_color=(0, 0, 0))  # Configura o diálogo com texto em preto  # Configura o diálogo com texto em preto
                        
                        # Desenha a seta amarela piscando se estiver visível
                        if azul_visivel:
                            screen.blit(seta_azul, pointer_position)

                    # Se o diálogo terminou, desativa a caixa de diálogo
                    if done and active_message == len(msg_finalizacao) - 1:
                        player.velocidade = 3.5
                        active_message = 0  # (Opcional) Reseta o índice do texto
                        counter = 0  # Reseta o contador interno
                        done = False  # Reseta o status de conclusão
                        dialogo_ativo = False  # Finaliza o diálogo
                        cena = "diploma"
            
            if entrou_auditorio:
                step = "Fale com o professor."
                txt_surface = pixelify_t.render(step, True, "white")
                txt_x, txt_y = 1585, 10
                screen.blit(txt_surface, (txt_x, txt_y))
                if azul_visivel:
                    screen.blit(bola_azul, (txt_x - 25, txt_y + 15))
                    
            # Verifica colisão com a saída para o terre
            if player.hitbox.colliderect(corredor_saida):
                cena = "terreo"  # Se colidir com a porta, muda para o cenário da rua
                print("Saindo para o térreo")
                player.x = corredor_saida_x
                player.y = corredor_saida_y
            
        # Atualiza a tela e os Frames
        atualizar_tela()  # Atualiza a tela com as mudanças realizadas

    elif cena == "biblioteca":
        # Verifica se o jogo está pausado e exibe o menu de pausa
        if pause:
            draw_pause(screen, menu_pause, pixelify_tiny, nome, personagem_escolhido)  # Exibe o menu de pausa


        for event in pygame.event.get():  # Loop de eventos para capturar interações do usuário
            if event.type == pygame.QUIT:  # Se o jogador fechar a janela
                loop = False  # Finaliza o loop principal
            if event.type == pygame.KEYDOWN:  # Evento de tecla pressionada
                if event.key == pygame.K_p:  # Se a tecla P for pressionada
                    # Alterna entre pausado e não pausado
                    if pause:
                        pause = False
                    else:
                        pause = True
                        
            if event.type == pygame.MOUSEBUTTONDOWN:  # Evento de clique do mouse
                mousepos = pygame.mouse.get_pos()  # Pega as coordenadas do clique                
                if pause and botao_continue.collidepoint(event.pos):
                    print("Continuar")  # Exibe mensagem no console
                    if pause:
                        pause = False
                    else:
                        pause = True
                if pause and botao_sair.collidepoint(event.pos):
                    loop = False
                    
        # Verifica se o jogo não está pausado para atualizar os elementos
        if not pause:
            teclas = pygame.key.get_pressed()  # Captura as teclas pressionadas pelo jogador
            novo_x = player.x  # Guarda a posição atual do jogador para lidar com colisões
            novo_y = player.y 
            
            # Mover o player usando a classe MainCharacter
            player.mover(teclas)  # Atualiza a posição do personagem com base nas teclas pressionadas
                
            # Verificar colisões com as hitboxes definidas
            for hitbox in hitboxes_biblioteca:
                if player.hitbox.colliderect(hitbox):
                    # Se o personagem colidir com alguma hitbox, retorna à posição anterior
                    player.x = novo_x
                    player.y = novo_y
            
            # Limpar a tela e desenhar o cenário
            limpar_e_desenhar(biblioteca_fundo)  # Chama a função para limpar e desenhar o fundo
            
            if player.y <= 650:
                player.desenhar_mainchar(screen)  # Desenha o sprite do personagem na tela
                screen.blit(estante1, (465, 678))
            
            elif player.y > 650:
                screen.blit(estante1, (465, 678))
                player.desenhar_mainchar(screen)  # Desenha o sprite do personagem na tela

            screen.blit(estante2, (465, 780))
            screen.blit(parede_biblioteca, (262, 858))
                
            # Renderizar o texto (True é para ativar antialiasing)
            text = "Biblioteca"
            text_surface = pixelify_t.render(text, True, "white")
            screen.blit(text_surface, (20, 10))


            # Verifica colisão com a saída para o terre
            if player.hitbox.colliderect(saida_biblioteca):
                cena = "corredor"  # Se colidir com a porta, muda para o cenário da rua
                print("Saindo para o térreo")
                player.x = saida_biblioteca_x
                player.y = saida_biblioteca_y
            
            #coords_text = pixelify.render(f"X: {player.x}, Y: {player.y}", True, "white")
            #screen.blit(coords_text, (10, 50))  # Especifica a posição do texto na tela
            
            # Atualiza a tela e os Frames
            atualizar_tela()  # Atualiza a tela com as mudanças realizadas        
    
    elif cena == "diploma":
        for event in pygame.event.get():  # Loop de eventos para capturar interações do usuário
            if event.type == pygame.QUIT:  # Se o jogador fechar a janela
                loop = False  # Finaliza o loop principal
            if event.type == pygame.KEYDOWN:  # Evento de tecla pressionada
                if event.key == pygame.K_p:  # Se a tecla P for pressionada
                    # Alterna entre pausado e não pausado
                    if pause:
                        pause = False
                    else:
                        pause = True
        
        teclas = pygame.key.get_pressed()  # Captura as teclas pressionadas pelo jogador

        # Limpar a tela e desenhar o cenário
        limpar_e_desenhar(diploma_cena)  # Chama a função para limpar e desenhar o fundo
        
        nome_diploma = pixelify_t.render(nome, True, "black")
        
            # Verifica o comprimento do nome e define a posição da name_box de acordo
        if len(nome) <= 10:
            screen.blit(nome_diploma, (840, 475))  # Nome menor que 10
        elif len(nome) >= 10 and len(nome) <= 20:
            screen.blit(nome_diploma, (800, 475))  # Nome entre 10 e 20
        elif len(nome) >= 20 and len(nome) <= 30:
            screen.blit(nome_diploma, (735, 475)) # Nome entre 20 e 30
        else:  # Caso o nome tenha mais de 30 caracteres
            screen.blit(nome_diploma, (680, 475)) # Nome maior que 30 
        
        # Verifique se passou o tempo necessário para mostrar a mensagem
        if pygame.time.get_ticks() - time_started > delay_time:
            screen.blit(press_enter, (1480, 10))  # Exibe a mensagem
            on_screen = True  # Define que a mensagem está na tela
        
        if on_screen:
            if teclas[pygame.K_RETURN]:  # Quando o jogador pressiona 'Enter'
                cena = "creditos"

        if personagem_escolhido == "menino":
            screen.blit(portraitg_mainchar, (110, 180))
        if personagem_escolhido == "menina":
            screen.blit(portraitg_fmainchar, (110, 180))
        
        # Atualiza a tela e os Frames
        atualizar_tela()  # Atualiza a tela com as mudanças realizadas
      
pygame.quit()
sys.exit()