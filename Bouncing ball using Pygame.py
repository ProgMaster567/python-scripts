import pygame

# Initialize pygame
pygame.init()

# Screen settings
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball Game")

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Ball properties
ball_radius = 20
ball_x, ball_y = width // 2, height // 3
ball_speed_x, ball_speed_y = 3, 3

# Paddle properties
paddle_width, paddle_height = 100, 10
paddle_x = (width - paddle_width) // 2
paddle_y = height - 50
paddle_speed = 7

# Game loop
running = True
while running:
    pygame.time.delay(10)  # Control game speed

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement (Arrow Keys)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < width - paddle_width:
        paddle_x += paddle_speed

    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with walls
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= width:
        ball_speed_x = -ball_speed_x
    if ball_y - ball_radius <= 0:
        ball_speed_y = -ball_speed_y

    # Ball collision with paddle
    if (paddle_y - ball_radius <= ball_y <= paddle_y and
            paddle_x <= ball_x <= paddle_x + paddle_width):
        ball_speed_y = -ball_speed_y

    # Ball falls below paddle (Game Over)
    if ball_y > height:
        print("Game Over!")
        running = False

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    pygame.draw.rect(screen, BLUE, (paddle_x, paddle_y, paddle_width, paddle_height))

    # Update screen
    pygame.display.update()

pygame.quit()
