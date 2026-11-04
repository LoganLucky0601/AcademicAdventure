import pygame

sala_vazia2 = pygame.image.load("assets/img/scenes/salas_vazias/sala_vazia.jpg")

#HITBOXES
hitboxes_sala_vazia2 = [
    #Paredes
    pygame.Rect(456, 205, 1010, 1), #parede top 
    pygame.Rect(456, 820, 1010, 1), #parede bottom 
    pygame.Rect(456, 191, 1, 623), #parede left 
    pygame.Rect(1465, 191, 1, 623), #parede left 
    
    #Plantas
    pygame.Rect(1425, 730, 30, 44), #planta right 
    
    # Fileira de mesas (da esquerda para direita)
    pygame.Rect(500, 370, 60, 500), #fileira de mesa 1
    pygame.Rect(700, 370, 60, 500), #fileira de mesa 2
    pygame.Rect(905, 370, 60, 500), #fileira de mesa 3
    pygame.Rect(1104, 370, 60, 500), #fileira de mesa 4
    pygame.Rect(1315, 370, 60, 500), #fileira de mesa 5
    
    # Armários
    pygame.Rect(478, 190, 74, 43), #armário 1
    pygame.Rect(755, 190, 74, 43), #armário 2
]

# Variáveis interativas
sair_da_sala_v2 = pygame.Rect(1355, 228, 45, 1)
sair_da_sala_v2_x = 775
sair_da_sala_v2_y = 340