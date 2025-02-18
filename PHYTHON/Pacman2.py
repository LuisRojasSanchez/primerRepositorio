import pygame
import sys
import random

# Inicializa pygame
pygame.init()

# Obtener las dimensiones de la pantalla
screen_info = pygame.display.Info()
WIDTH, HEIGHT = screen_info.current_w - 100, screen_info.current_h - 100  # Menos 100px para que no sea pantalla completa
CELL_SIZE = 28  # Ajusta el tamaño de las celdas
ROWS = 25  # Número de filas
COLS = 28  # Número de columnas

# Configuración de la pantalla
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Pacman")

# Colores
WHITE = (22, 22, 72)
BLACK = (0, 0, 0)

# Direcciones
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Cargar imágenes de Pacman
pacman_frames = [pygame.image.load(r"PHYTHON/images/pacman_frame_{}.png".format(i)) for i in range(1, 7)]

# Redimensionar imágenes
pacman_frames = [pygame.transform.scale(img, (CELL_SIZE, CELL_SIZE)) for img in pacman_frames]

# Cargar la imagen del fantasma
ghost_img = pygame.image.load(r"PHYTHON/images/ghots.png")
ghost_img = pygame.transform.scale(ghost_img, (CELL_SIZE, CELL_SIZE))

# Cargar la imagen de la superpastilla
power_pellet_img = pygame.image.load(r"PHYTHON/images/power_pellet.png")
power_pellet_img = pygame.transform.scale(power_pellet_img, (CELL_SIZE, CELL_SIZE))

# Definición del mapa (0 = camino, 1 = pared, 2 = punto comestible)
map_layout = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
    [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
    [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1],
    [1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
    [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = None
        self.animation_index = 0
        self.image = pacman_frames[0]
        self.score = 0

    def draw(self):
        screen.blit(self.image, (self.x * CELL_SIZE, self.y * CELL_SIZE))

    def move(self, direction):
        self.direction = direction

    def update(self):
        if self.direction:
            new_x = self.x + self.direction[0]
            new_y = self.y + self.direction[1]
            if 0 <= new_x < COLS and 0 <= new_y < ROWS:
                if map_layout[new_y][new_x] != 1:
                    self.x = new_x
                    self.y = new_y

            self.animation_index = (self.animation_index + 1) % len(pacman_frames)
            self.image = pacman_frames[self.animation_index]

    def check_collision(self, ghost):
        return self.x == ghost.x and self.y == ghost.y


class Ghost:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def draw(self):
        screen.blit(ghost_img, (self.x * CELL_SIZE, self.y * CELL_SIZE))

    def update(self):
        new_x = self.x + self.direction[0]
        new_y = self.y + self.direction[1]
        if 0 <= new_x < COLS and 0 <= new_y < ROWS and map_layout[new_y][new_x] != 1:
            self.x = new_x
            self.y = new_y
        else:
            self.direction = random.choice([UP, DOWN, LEFT, RIGHT])


# Inicializar jugador y fantasmas
player = Player(1, 1)
ghosts = [Ghost(6, 6), Ghost(8, 8)]

# Reloj para controlar FPS
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(BLACK)

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move(UP)
            elif event.key == pygame.K_DOWN:
                player.move(DOWN)
            elif event.key == pygame.K_LEFT:
                player.move(LEFT)
            elif event.key == pygame.K_RIGHT:
                player.move(RIGHT)

    # Dibujar el mapa
    for row in range(ROWS):
        for col in range(COLS):
            if map_layout[row][col] == 1:
                pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif map_layout[row][col] == 2:
                pygame.draw.circle(screen, (255, 255, 0), (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 6)
            elif map_layout[row][col] == 3:
                screen.blit(power_pellet_img, (col * CELL_SIZE, row * CELL_SIZE))

    # Actualizar y dibujar personajes
    player.update()
    player.draw()
    for ghost in ghosts:
        ghost.update()
        ghost.draw()
        if player.check_collision(ghost):
            running = False  # Terminar juego si colisiona

    pygame.display.flip()
    clock.tick(30)  # Limitar FPS a 30

pygame.quit()
sys.exit()
