import turtle
import time
import random

delay = 0.1
body_segments = {}

# Configuración de la ventana
wn = turtle.Screen()
wn.title("Juego Snake")
wn.setup(width=600, height=600)
wn.bgcolor("blue")

# Configuración de la cabeza de la serpiente
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('red')
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Configuración de la comida
food = turtle.Turtle()
food.speed(0)
food.shape("dog")
food.color("green")
food.penup()
food.goto(0, 100)

# Movimiento de la serpiente
def mov():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

# Funciones para cambiar la dirección
def dirUp():
    if head.direction != "down":
        head.direction = "up"

def dirDown():
    if head.direction != "up":
        head.direction = "down"

def dirRight():
    if head.direction != "left":
        head.direction = "right"

def dirLeft():
    if head.direction != "right":
        head.direction = "left"

# Conexión de teclas
wn.listen()
wn.onkeypress(dirUp, "Up")
wn.onkeypress(dirDown, "Down")
wn.onkeypress(dirRight, "Right")
wn.onkeypress(dirLeft, "Left")

# Bucle principal del juego
while True:
    wn.update()

    # Comprobar si la cabeza de la serpiente toca la comida
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
         #cofiguracion de los segmet
         new_segments = turtle.Turtle() 
         new_segments.speed(0)
         new_segments.shape('square')
         new_segments.color('yellow')
         new_segments.penup()
         body_segments.append(new_segments)
         print(body_segments)
         
         totlseg = len(body_segments)
         print(totlseg)
 
        for i in range(totlseg - 1, 0, -1):
            x = body_segments[i - 1].xcor()
            y = body_segments[i - 1].ycor()
            body_segments [i]. goto(x, y)
            
          # Mover la cabeza de la serpiente
if totlseg > 0:
    x = head.xcor()
    y = head.ycor()
    body_segments[0].goto(x, y)
            



    mov()
    time.sleep(0.1)

turtle.done()
