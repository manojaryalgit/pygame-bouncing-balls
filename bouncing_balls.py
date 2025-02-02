import pygame
import random
import math
from pygame.math import Vector3

pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Sphere settings
SPHERE_RADIUS = min(WIDTH, HEIGHT) * 0.3
CENTER = Vector3(WIDTH // 2, HEIGHT // 2, 0)

class Ball:
    def __init__(self):
        self.pos = Vector3(random.uniform(-SPHERE_RADIUS, SPHERE_RADIUS),
                           random.uniform(-SPHERE_RADIUS, SPHERE_RADIUS),
                           random.uniform(-SPHERE_RADIUS, SPHERE_RADIUS))
        self.vel = Vector3(random.uniform(-2, 2), random.uniform(-2, 2), random.uniform(-2, 2))
        self.trail = []
        self.trail_length = 15
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
    
    def update(self):
        self.pos += self.vel
        if self.pos.length() > SPHERE_RADIUS:
            normal = self.pos.normalize()
            self.vel = self.vel.reflect(normal)
            self.pos = normal * (SPHERE_RADIUS - 1)
        
        self.trail.append(self.pos.copy())
        if len(self.trail) > self.trail_length:
            self.trail.pop(0)
    
    def display(self):
        for i in range(len(self.trail)):
            alpha = int((i / self.trail_length) * 255)
            pygame.draw.circle(screen, self.color, (int(self.trail[i].x + CENTER.x), int(self.trail[i].y + CENTER.y)), 3)
        pygame.draw.circle(screen, self.color, (int(self.pos.x + CENTER.x), int(self.pos.y + CENTER.y)), 5)

balls = [Ball() for _ in range(100)]

running = True
while running:
    screen.fill((10, 10, 10))
    
    for ball in balls:
        ball.update()
        ball.display()
    
    pygame.display.flip()
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
