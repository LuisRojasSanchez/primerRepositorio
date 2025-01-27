import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (2, 2, 56)

# Posición y tamaño del jugador (Pacman)
player_size = 40
player_x, player_y = WIDTH // 2, HEIGHT // 2

# Velocidad del Jugador
player_speed = 5  # Ajustado para que el movimiento sea más visible

# Bucle principal del Juego
running = True
while running:
    screen.fill(BLUE)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimiento del Jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Limitar el movimiento del jugador a los bordes de la pantalla
    player_x = max(player_size // 2, min(WIDTH - player_size // 2, player_x))
    player_y = max(player_size // 2, min(HEIGHT - player_size // 2, player_y))

    # Dibujar al jugador (Pacman)
    pygame.draw.circle(screen, YELLOW, (player_x, player_y), player_size // 2)

    pygame.display.flip()

    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
