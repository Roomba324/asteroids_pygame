# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from bullet import *

clock = pygame.time.Clock()
dt = 0

updateable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updateable, drawable)
Asteroid.containers = (asteroids, updateable, drawable)
AsteroidField.containers = (updateable)
Shot.containers = (shots, updateable, drawable)

ppx = SCREEN_WIDTH / 2
ppy = SCREEN_HEIGHT / 2
player1 = Player(ppx, ppy)
AsteroidFiedld1 = AsteroidField()

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
		for object in drawable:
			object.draw(screen)
		for asteroid in asteroids:
			if player1.collision(asteroid):
				print ("Game over!")
				return
		updateable.update(dt)
		pygame.display.flip()

	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()

