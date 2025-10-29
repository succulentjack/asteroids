import pygame
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
	pygame.init()
	gameclock = pygame.time.Clock()
	dt = 0
	x = constants.SCREEN_WIDTH / 2
	y = constants.SCREEN_HEIGHT / 2
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	Asteroid.containers = (asteroids, updatable, drawable)
	Player.containers = (updatable, drawable)
	AsteroidField.containers = (updatable)
	player = Player(x, y)
	asteroid_field = AsteroidField()
	print("Starting Asteroids!")
	screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0, 0, 0))
		for entity in updatable:
			entity.update(dt)
		for entity in drawable:
			entity.draw(screen)
		pygame.display.flip()
		dt = gameclock.tick(60) / 1000

if __name__ == "__main__":
    main()
