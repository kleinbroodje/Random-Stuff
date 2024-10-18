import pygame
import os


pygame.init()

screen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h ))
pygame.display.set_caption("Zintuigen PO")

WIDTH = 2648
HEIGHT = 1488
SCALE = 0.65
nums = {}
data = []
runs = 0

audio = pygame.mixer.Sound(os.path.join("assets", "audio.mp3"))

for i in range(1, 10):
    for j in range(3):
        if i == 9 and j == 2:
            continue
        nums[f"{i}.{j}"] = pygame.transform.scale(pygame.image.load(os.path.join("assets", f"ishihara-{i}.{j}.png")), (WIDTH * SCALE, HEIGHT * SCALE)).convert()
