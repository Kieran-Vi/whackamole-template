import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        mole = [0, 0]
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked_x, clicked_y = event.pos
                    if clicked_x // 32 == mole[0] and clicked_y // 32 == mole[1]:
                        mole[0] = random.randint(0, 19)
                        mole[1] = random.randint(0, 15)

            screen.fill("light green")
            for i in range(1, 16):
                pygame.draw.line(screen, "black", (0, i*32), (640, i*32))
            for i in range(1, 20):
                pygame.draw.line(screen, "black", (i*32, 0), (i*32, 512))

            screen.blit(mole_image, mole_image.get_rect(topleft=(mole[0] * 32 + 2, mole[1] * 32 + 2)))
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
