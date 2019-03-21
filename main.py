import pygame

pygame.init()

RED = pygame.Color("#FF0000")
WHITE = pygame.Color("#FFFFFF")
CYAN = pygame.Color("#00FFFF")
SILVER = pygame.Color("#C0C0C0")
BLUE = pygame.Color("#0000FF")
GRAY = pygame.Color("#808080")
DARKBLUE = pygame.Color("#0000A0")
BLACK = pygame.Color("#000000")
LIGHTBLUE = pygame.Color("#ADD8E6")
ORANGE = pygame.Color("#FFA500")
PURPLE = pygame.Color("#800080")
BROWN = pygame.Color("#A52A2A")
YELLOW = pygame.Color("#FFFF00")
MAROON = pygame.Color("#800000")
LIME = pygame.Color("#00FF00")
GREEN = pygame.Color("#008000")
MAGENTA = pygame.Color("#FF00FF")
OLIVE = pygame.Color("#808000")


size = (400, 500)
screen = pygame.display.set_mode(size)#, pygame.FULLSCREEN)

pygame.display.set_caption("Rotate Text")

done = False
clock = pygame.time.Clock()

text_rotate_degrees = 0

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                   done = True

    screen.fill(BLACK)

    font = pygame.font.SysFont('Calibri', 25, True, False)

    text = font.render("text", True, WHITE)
    screen.blit(text, [0, 0])

    text = font.render("more text", True, WHITE)
    screen.blit(text, [0, 100])

    pygame.display.flip()

    clock.tick(60)

pygame.quit()