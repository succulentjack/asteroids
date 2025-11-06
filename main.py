import sys
import pygame
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	gameclock = pygame.time.Clock()
	dt = 0
	x = constants.SCREEN_WIDTH / 2
	y = constants.SCREEN_HEIGHT / 2
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Asteroid.containers = (asteroids, updatable, drawable)
	Player.containers = (updatable, drawable)
	Shot.containers = (shots, updatable, drawable)
	AsteroidField.containers = (updatable)
	player = Player(x, y)
	asteroid_field = AsteroidField()
	print("Starting Asteroids!")
	print(f"Screen width: {constants.SCREEN_WIDTH}")
	print(f"Screen height: {constants.SCREEN_HEIGHT}")
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
		for asteroid in asteroids:
			if asteroid.check_collision(player):
				print("Game Over!")
				sys.exit()
			for shot in shots:
				if asteroid.check_collision(shot):
					asteroid.split()
					shot.kill()
		pygame.display.flip()
		dt = gameclock.tick(60) / 1000

if __name__ == "__main__":
    main()
