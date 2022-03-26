# GitHub - PyGameExamplesAndAnswers - PyGame and OpenGL immediate mode (Legacy OpenGL) - Wavefront .obj file
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame_opengl/immediate_mode/pygame_opengl_immediate_mode.md#mouse-position-and-unproject
#
# PyOpenGL how do I import an obj file?
# https://stackoverflow.com/questions/59923419/pyopengl-how-do-i-import-an-obj-file/59926122#59926122

import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../resource'))
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame_opengl_begin_end_objloader import *

pygame.init()
display = (640, 480)

pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
clock = pygame.time.Clock()

glMatrixMode(GL_PROJECTION)
gluPerspective(90, (display[0]/display[1]), 0.1, 10)

glMatrixMode(GL_MODELVIEW)
glTranslatef(0.0, 0, -5)

model = OBJ('model/wavefront/bunny.obj')
angle = 0

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glPushMatrix()
    scale = 30
    glTranslate(0, -3, 0)
    glRotate(angle, 0, 1, 0)
    glTranslate(0.5, 0, 0)
    glScale(scale, scale, scale)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    model.render()
    glPopMatrix()
    angle += 1
    
    pygame.display.flip()

pygame.quit()
quit()