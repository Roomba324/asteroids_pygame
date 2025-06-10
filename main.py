# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

clock = pygame.time.Clock()
dt = 0


ppx = SCREEN_WIDTH / 2
ppy = SCREEN_HEIGHT / 2
player1 = Player(ppx, ppy)

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


	while True:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return
		screen.fill("black")
		dt = clock.tick(60)
		dt /= 1000
		player1.draw(screen)
		pygame.display.flip()
		

	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()

