# pygame.math module
# https://www.pygame.org/docs/ref/math.html
#
# [Trying to code the Recaman Sequence, but issue with the parameters I pass for drawing an arc
# https://stackoverflow.com/questions/54384422/trying-to-code-the-recaman-sequence-but-issue-with-the-parameters-i-pass-for-dr/54386695#54386695  
#
# GitHub - PyGameExamplesAndAnswers - Recaman's sequence
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_2D.md

import pygame 
import math

pygame.init()
window = pygame.display.set_mode((800, 600))

index, limit = 0, 40
sequence = [0]
for i in range(limit):
    index += -i if index-i > 0 and index-i not in sequence else i
    sequence.append(index)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    zx = window.get_width() / limit
    zy = window.get_height() / 2 / limit
    
    window.fill((255, 255, 255))

    curX, curY = 0, 500
    for n in range(0, len(sequence)-1):
        
        d = 1 if n % 2 == 0 else -1
        s = 1 if sequence[n+1] > sequence[n] else -1
        
        curX = curX + n * zx * s
        xi = curX + (n * zx) * -s
        yi = 500
        xf = curX
        yf = curY - (n * zy) * d
        
        p1 = (xi, yi)
        p2 = (xf, yf)

        dx = xf - xi
        dy = yf - yi

        diameter   = abs(dx)
        px         = xi if dx > 0 else xi + dx
        py         = window.get_height() // 2 - diameter // 2

        start_ang = 0 if dy < 0 else math.pi
        end_ang   = start_ang + math.pi
        pygame.draw.arc(window, (0, 0, 0), (px, py, diameter, diameter), start_ang, end_ang, 1)

    pygame.display.flip()
