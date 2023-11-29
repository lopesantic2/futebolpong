import pygame

# Inicialização do Pygame
pygame.init()

# Configuração da janela do jogo
window = pygame.display.set_mode([1280, 720])
title = pygame.display.set_caption('Futeball Pong')

# Carregamento de imagens
win = pygame.image.load('assets/win.png')

# Variáveis de pontuação
score1 = 0
score1_img = pygame.image.load('assets/score/0.png')
score2 = 0
score2_img = pygame.image.load('assets/score/0.png')

# Carregamento de imagens para o campo, jogadores e bola
field = pygame.image.load('assets/field.png')
player1 = pygame.image.load('assets/player1.png')
player1_y = 310
player1_moveUp = False
player1_moveDown = False

player2 = pygame.image.load('assets/player2.png')
player2_y = 310

ball = pygame.image.load('assets/ball.png')
ball_x = 617
ball_y = 337
ball_dir = -3
ball_dir_y = 1
ball_speed = 3  # Velocidade inicial da bola

# Função para mover o jogador 1
def move_player():
    global player1_y

    # Move o jogador 1 para cima
    if player1_moveUp:
        player1_y -= 5

    # Move o jogador 1 para baixo
    if player1_moveDown:
        player1_y += 5

    # Garante que o jogador 1 não ultrapasse os limites da tela
    if player1_y <= 0:
        player1_y = 0
    elif player1_y >= 575:
        player1_y = 575

# Função para mover o jogador 2
def move_player2():
    global player2_y
    player2_y = ball_y

# Função para mover a bola
def move_ball():
    global ball_x, ball_y, ball_dir, ball_dir_y, score1, score2, score2_img, score1_img, ball_speed

    # Move a bola de acordo com a velocidade
    ball_x += ball_dir * ball_speed
    ball_y += ball_dir_y * ball_speed

    # Lógica de colisão com o jogador 1
    if ball_x < 120:
        if player1_y < ball_y + 23 and player1_y + 146 > ball_y:
            ball_dir *= -1

    # Lógica de colisão com o jogador 2
    if ball_x > 1100:
        if player2_y < ball_y + 23 and player2_y + 146 > ball_y:
            ball_dir *= -1

    # Lógica de rebatida na parte superior e inferior da tela
    if ball_y > 685 or ball_y <= 0:
        ball_dir_y *= -1

    # Lógica de pontuação e reinício da bola
    if ball_x < -50:
        ball_x = 617
        ball_y = 337
        ball_dir_y *= -1
        ball_dir *= -1
        score2 += 1
        score2_img = pygame.image.load("assets/score/" + str(score2) + ".png")
        ball_speed += 1  # Aumenta a velocidade da bola após a vitória
    elif ball_x > 1320:
        ball_x = 617
        ball_y = 337
        ball_dir_y *= -1
        ball_dir *= -1
        score1 += 1
        score1_img = pygame.image.load("assets/score/" + str(score1) + ".png")
        ball_speed += 1  # Aumenta a velocidade da bola após a vitória

# Função para desenhar os elementos na tela
def draw():
    if score1 < 9 and score2 < 9:
        window.blit(field, (0, 0))
        window.blit(player1, (50, player1_y))
        window.blit(player2, (1150, player2_y))
        window.blit(ball, (ball_x, ball_y))
        window.blit(score1_img, (500, 50))
        window.blit(score2_img, (710, 50))
        move_ball()
        move_player()
        move_player2()
    else:
        window.blit(win, (300, 330))

# Loop principal do jogo
loop = True
while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False
        if events.type == pygame.KEYDOWN:
            # Verifica se as teclas W e S foram pressionadas para mover o jogador 1
            if events.key == pygame.K_w:
                player1_moveUp = True
            if events.key == pygame.K_s:
                player1_moveDown = True
        if events.type == pygame.KEYUP:
            # Verifica se as teclas W e S foram soltas para parar o movimento do jogador 1
            if events.key == pygame.K_w:
                player1_moveUp = False
            if events.key == pygame.K_s:
                player1_moveDown = False

    # Chama a função de desenho
    draw()

    # Atualiza a janela do jogo
    pygame.display.update()
