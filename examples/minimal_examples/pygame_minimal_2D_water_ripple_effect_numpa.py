# pygame.math module
# https://www.pygame.org/docs/ref/math.html
#
# Water ripple effect Python and Pygame, from coding train video
# https://stackoverflow.com/questions/60336688/wter-ripple-effect-python-and-pygame-from-coding-train-video/60337269#60337269
#
# from coding train video
# https://www.youtube.com/watch?v=BZUdGqeOD0w
#
# GitHub - PyGameExamplesAndAnswers - Draw 2D - Effects
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_2D.md

import numpy
import pygame   
pygame.init()

window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

size = window.get_size()
dampening = 0.999

current = numpy.zeros(size, numpy.float32)
previous = numpy.zeros(size, numpy.float32)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False    
        
    if any(pygame.mouse.get_pressed()):
        mouse_pos = pygame.mouse.get_pos()
        previous[mouse_pos] = 1000

    current[1:size[0]-1, 1:size[1]-1] = (
        (previous[0:size[0]-2, 0:size[1]-2] + 
         previous[2:size[0], 0:size[1]-2] + 
         previous[0:size[0]-2, 2:size[1]] + 
         previous[2:size[0], 2:size[1]]) / 2 - 
        current[1:size[0]-1, 1:size[1]-1]) * dampening
    array = numpy.transpose(255 - numpy.around(numpy.clip(current, 0, 255)))
    array = numpy.repeat(array.reshape(*size, 1).astype('uint8'), 3, axis = 2)
    image = pygame.image.frombuffer(array.flatten(), size, 'RGB')

    previous, current = current, previous

    window.blit(image, (0, 0))
    pygame.display.flip()

pygame.quit()
exit()