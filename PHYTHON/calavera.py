import turtle

# Configuración de pantalla y tortuga
screen = turtle.Screen()
screen.bgcolor("lightblue")

t = turtle.Turtle()
t.shape("turtle")
t.speed(5)
t.width(2)

# Función para dibujar el cráneo
def draw_skull():
    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.color("black", "white")
    t.begin_fill()
    t.circle(100)  # Círculo para el cráneo
    t.end_fill()

# Función para dibujar un ojo
def draw_eye(x, y):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.color("black", "black")
    t.begin_fill()
    t.circle(30)  # Tamaño del ojo
    t.end_fill()

# Función para dibujar la nariz
def draw_nose():
    t.penup()
    t.goto(0, -20)
    t.setheading(0)
    t.pendown()
    t.color("black", "black")
    t.begin_fill()
    t.circle(10, steps=3)  # Triángulo para la nariz
    t.end_fill()

# Función para dibujar la boca con "marcas" de dientes
def draw_mouth():
    t.penup()
    t.goto(-40, -70)
    t.pendown()
    t.width(2)
    t.color("black")
    t.setheading(-15)
    t.circle(80, 30)  # Línea curva para la boca
    # Dibujar líneas para los "dientes"
    t.penup()
    t.goto(-35, -70)
    t.setheading(-15)
    for _ in range(5):
        t.forward(15)
        t.pendown()
        t.forward(10)
        t.penup()

# Función para dibujar una flor sencilla
def draw_flower():
    t.penup()
    t.goto(40, -70)  # Coloca la flor en el lado derecho de la boca
    t.setheading(0)
    t.pendown()
    t.color("darkred", "pink")
    
    # Dibuja los pétalos
    for _ in range(6):
        t.begin_fill()
        t.circle(20, 60)
        t.left(120)
        t.circle(20, 60)
        t.left(120)
        t.end_fill()
        t.right(60)
    
    # Dibuja el centro de la flor
    t.penup()
    t.goto(40, -65)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.circle(5)
    t.end_fill()

# Dibuja el cráneo y los detalles
draw_skull()
draw_eye(-35, 30)  # Ojo izquierdo
draw_eye(35, 30)   # Ojo derecho
draw_nose()
draw_mouth()
draw_flower()

# Finaliza y oculta la tortuga
t.hideturtle()
turtle.done()
