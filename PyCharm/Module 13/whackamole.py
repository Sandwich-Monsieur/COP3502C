#https://youtu.be/Izx6ByqgEAA

import pygame
import random

cell = 32
width = 20
height = 16
window_width = cell * width
window_height = cell * height

def draw_grid(screen):
    for x in range(0, window_width, cell):
        pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, window_height))
    for y in range(0, window_height, cell):
        pygame.draw.line(screen, (0, 0, 0), (0, y), (window_width, y))

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        screen = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Whack-a-Mole")
        clock = pygame.time.Clock()

        mole_image = pygame.image.load("mole.png")
        mole_col = 0
        mole_row = 0

        running = True
        while running:
            screen.fill("light green")
            draw_grid(screen)

            mole_x = mole_col * cell
            mole_y = mole_row * cell
            mole_rect = mole_image.get_rect(topleft=(mole_x, mole_y))
            screen.blit(mole_image, mole_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if mole_rect.collidepoint(event.pos):
                        mole_col = random.randrange(0, width)
                        mole_row = random.randrange(0, height)
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()