import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mover Objeto con Teclas")

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Posición inicial del objeto
x, y = width // 2, height // 2
speed = 5

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Capturar las teclas presionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Limitar el objeto dentro de la pantalla
    x = max(0, min(x, width - 50))
    y = max(0, min(y, height - 50))

    # Dibujar el fondo y el objeto
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (x, y, 50, 50))

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.Clock().tick(60)

# Salir de Pygame
pygame.quit()
sys.exit()