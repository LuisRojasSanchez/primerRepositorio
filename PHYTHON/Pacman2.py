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
6
# Configuración de la pantalla en modo ventana maximizable
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

# Cargar imágenes para la animación de Pacman
pacman_frames = [
    pygame.image.load(f"PHYTHON\images\pacman_frame_{i}.png") for i in range(1, 7)  # Carga de 6 frames
]

# Redimensionar las imágenes de Pacman
for i in range(len(pacman_frames)):
    pacman_frames[i] = pygame.transform.scale(pacman_frames[i], (CELL_SIZE, CELL_SIZE))

# Cargar la imagen del fantasma
ghost_img = pygame.image.load("PHYTHON\images\ghots.png")  # Corregido el nombre de la imagen
ghost_img = pygame.transform.scale(ghost_img, (CELL_SIZE, CELL_SIZE))

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


# Asegúrate de que las dimensiones del mapa sean correctas
assert len(map_layout) == ROWS, f"Se esperaban {ROWS} filas, pero se encontró {len(map_layout)}."
assert all(len(row) == COLS for row in map_layout), "Algunas filas del mapa no tienen la cantidad correcta de columnas."

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = None
        self.animation_index = 0
        self.image = pacman_frames[0]
        self.score = 0  # Agregar un atributo para el puntaje
        self.power_mode = False  # Indica si está en modo superpastilla
        self.power_mode_duration = 0  # Duración del modo superpastilla

    def draw(self):
        screen.blit(self.image, (self.x * CELL_SIZE, self.y * CELL_SIZE))

    def move(self, direction):
        self.direction = direction

    def update(self):
        if self.direction:
            new_x = self.x + self.direction[0]
            new_y = self.y + self.direction[1]
            if 0 <= new_x < COLS and 0 <= new_y < ROWS:
                if map_layout[new_y][new_x] != 1:  # Verificar que no sea una pared
                    # Comprobar si recoge un punto o una superpastilla
                    if map_layout[new_y][new_x] == 2:  # Punto comestible
                        self.score += 1
                        map_layout[new_y][new_x] = 0  # Eliminar el punto del mapa
                    elif map_layout[new_y][new_x] == 3:  # Superpastilla
                        self.score += 5
                        map_layout[new_y][new_x] = 0  # Eliminar la superpastilla del mapa
                        self.activate_power_mode()  # Activar el modo de superpastilla

                    self.x = new_x
                    self.y = new_y

            # Cambiar la imagen de Pacman para crear la animación
            self.animation_index = (self.animation_index + 1) % len(pacman_frames)
            self.image = pacman_frames[self.animation_index]

            # Rotar Pacman según la dirección
            if self.direction == LEFT:
                self.image = pygame.transform.rotate(pacman_frames[self.animation_index], 180)
            elif self.direction == UP:
                self.image = pygame.transform.rotate(pacman_frames[self.animation_index], 90)
            elif self.direction == DOWN:
                self.image = pygame.transform.rotate(pacman_frames[self.animation_index], -90)
            else:  # RIGHT
                self.image = pacman_frames[self.animation_index]

        else:  # Si no hay movimiento, mantener la última imagen
            self.image = pacman_frames[self.animation_index]

    def activate_power_mode(self):
        self.power_mode = True
        self.power_mode_duration = 5  # Duración en segundos


# Clase de los fantasmas
class Ghost:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def draw(self):
        screen.blit(ghost_img, (self.x * CELL_SIZE, self.y * CELL_SIZE))

    def get_possible_directions(self):
        possible_directions = []
        for direction in [UP, DOWN, LEFT, RIGHT]:
            new_x = self.x + direction[0]
            new_y = self.y + direction[1]
            if 0 <= new_x < COLS and 0 <= new_y < ROWS:
                if map_layout[new_y][new_x] != 1:  # No es una pared
                    possible_directions.append(direction)
        return possible_directions

    def update(self):
        possible_directions = self.get_possible_directions()

        if possible_directions:
            # Elegir una nueva dirección aleatoria de las posibles
            self.direction = random.choice(possible_directions)

            new_x = self.x + self.direction[0]
            new_y = self.y + self.direction[1]
            self.x = new_x
            self.y = new_y


# Inicialización de jugador y fantasmas
player = Player(15, 17)  # Asegúrate de que esta línea esté después de la definición de la clase Player
ghosts = [Ghost(6, 6), Ghost(8, 8)]


# Cargar fuente
font = pygame.font.Font(None, 74)  # Puedes ajustar el tamaño de la fuente

# Reloj para controlar los FPS
clock = pygame.time.Clock()

# Estado del juego
game_over = False

# Inicializar el estado del juego
game_over = False

# Bucle principal del juego
running = True
while running:
    screen.fill(BLACK)

# Cargar la imagen de la superpastilla
power_pellet_img = pygame.image.load("PHYTHON\images\power_pellet.png")  # Asegúrate de que la imagen esté en esta ruta
power_pellet_img = pygame.transform.scale(power_pellet_img, (CELL_SIZE, CELL_SIZE))


# Dibujar el mapa
for row in range(ROWS):
    for col in range(COLS):
        if map_layout[row][col] == 1:  # Pared
            pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        elif map_layout[row][col] == 2:  # Punto comestible
            pygame.draw.circle(screen, (255, 255, 0), (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 6)
        elif map_layout[row][col] == 3:  # Superpastilla
            screen.blit(power_pellet_img, (col * CELL_SIZE, row * CELL_SIZE))  # Dibuja la superpastilla



    # Eventos de teclado
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if not game_over:  # Solo permitir movimiento si el juego no ha terminado
                if event.key == pygame.K_UP:
                    player.move(UP)
                elif event.key == pygame.K_DOWN:
                    player.move(DOWN)
                elif event.key == pygame.K_LEFT:
                    player.move(LEFT)
                elif event.key == pygame.K_RIGHT:
                    player.move(RIGHT)

    # Actualizar y dibujar al jugador y los fantasmas
    player.update()
    player.draw()

    for ghost in ghosts:
        ghost.update()
        ghost.draw()
        if player.check_collision(ghost):  # Comprobar colisiones con los fantasmas
            game_over = True  # Cambiar el estado del juego a "Game Over"

    # Comprobar si se recogieron todos los puntos
    if player.score == player.total_points:
        game_over_text = font.render("¡Ganaste!", True, (255, 255, 255))
        screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
        pygame.display.flip()
        pygame.time.wait(2000)  # Esperar 2 segundos antes de cerrar
        running = False  # Terminar el juego

    # Mostrar mensaje de Game Over si el juego ha terminado
    if game_over:
        game_over_text = font.render("¡Game Over!", True, (255, 0, 0))  # Rojo para Game Over
        screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 50))
        pygame.display.flip()
        pygame.time.wait(2000)  # Esperar 2 segundos antes de cerrar
        running = False  # Terminar el juego

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
sys.exit()

