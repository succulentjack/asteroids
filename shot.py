import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, SHOT_RADIUS)

	def draw(self, screen):
		pygame.draw.circle(screen, pygame.color.Color('white'), self.position, SHOT_RADIUS, width = 1)

	def update(self, dt):
		self.position += self.velocity * dt
