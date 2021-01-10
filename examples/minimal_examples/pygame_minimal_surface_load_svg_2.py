# pynanosvg 
# 
# pip install svglib
#
#    - https://pypi.org/project/svglib/
#
# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# SVG rendering in a PyGame application
# https://stackoverflow.com/questions/120584/svg-rendering-in-a-pygame-application
#
# GitHub - PyGameExamplesAndAnswers - Surface and image - Load Pillow image
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_surface_and_image.md

import os
import pygame
import cairo
from svglib.svglib import svg2rlg
import io

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))

def load_svg(filename):
    drawing = svg2rlg(filename)
    str = drawing.asString("png")
    byte_io = io.BytesIO(str)
    return pygame.image.load(byte_io)

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

pygame_surface = load_svg('clipart/Ice-001.svg')
size = pygame_surface.get_size()
scale = min(window.get_width() / size[0], window.get_width() / size[1]) * 0.8
pygame_surface = pygame.transform.scale(pygame_surface, (round(size[0] * scale), round(size[1] * scale)))

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((127, 127, 127))
    window.blit(pygame_surface, pygame_surface.get_rect(center = window.get_rect().center))
    pygame.display.flip()

pygame.quit()
exit()