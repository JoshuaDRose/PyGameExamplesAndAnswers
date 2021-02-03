# pygame.math.Vector3 object
# https://www.pygame.org/docs/ref/math.html
#
# How do I render faces properly in 3d?
# https://stackoverflow.com/questions/60308506/how-do-i-render-faces-properly-in-3d
#
# GitHub - PyGameExamplesAndAnswers - Draw 3D
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_3D.md

import pygame, math

def rotate2d(pos, rad): 
    s,c  = math.sin(rad), math.cos(rad)
    return pos[0]*c - pos[1]*s, pos[1]*c + pos[0]*s

class Camera:
    def __init__(self, viewport_rect, pos, rot):
        self.viewport_rect = viewport_rect
        self.pos = list(pos)
        self.rot = list(rot)

    def events(self, move_rel):
        self.rot[0] += event.rel[1] * 2 / self.viewport_rect.width
        self.rot[1] += event.rel[0] * 2 / self.viewport_rect.height

    def update(self, dt, move_vec):
        s = dt*10
        x, y = math.sin(self.rot[1]), math.cos(self.rot[1])
        self.pos[0] += s * (x * move_vec[1] + y * move_vec[0])
        self.pos[1] += s * move_vec[2]
        self.pos[2] += s * (y * move_vec[1] - x * move_vec[0])

    def viewcoordinate(self, vertex):
        x = vertex[0] - self.pos[0]
        y = vertex[1] - self.pos[1]
        z = vertex[2] - self.pos[2]
        x, z = rotate2d((x, z), camera.rot[1])
        y, z = rotate2d((y, z), camera.rot[0])
        return x, y, z

    def project(self, vertex):
        z = 0.001 if vertex[2] == 0 else vertex[2]
        f = 200 / z
        return self.viewport_rect.centerx + round(vertex[0]*f), self.viewport_rect.centery + round(vertex[1]*f)


class Cube:
    verticies = (-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)
    faces = (0,1,2,3),(4,5,6,7),(0,1,5,4),(2,3,7,6),(0,3,7,4),(1,2,6,5)
    def __init__(self,pos=(0,0,0)):
        x,y,z = pos
        self.verts = [(x+X/2,y+Y/2,z+Z/2) for X,Y,Z in self.verticies]


pygame.init()
cx, cy = 200, 200
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

camera = Camera(screen.get_rect(), (0, 0, -5), (0, 0))

pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

cubes = [Cube((-2+i*2,0,0)) for i in range(3)]

run = True
while run:
    dt = clock.tick()/1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: 
            run = False
        if event.type == pygame.MOUSEMOTION:
            camera.events(event.rel)

    key = pygame.key.get_pressed()
    camera.update(dt, (
        key[pygame.K_d] - key[pygame.K_a],
        key[pygame.K_w] - key[pygame.K_s],
        key[pygame.K_q] - key[pygame.K_e]))

    screen.fill((255,255,255))
    for obj in cubes:
        vert_list = [camera.viewcoordinate(v) for v in obj.verts] 
        screen_coords = [camera.project(v) for v in vert_list]
        face_list = []
        face_color = []
        depth = []
        for face in obj.faces:
            on_screen = any(i for i in face if vert_list[i][2]>0 and camera.viewport_rect.collidepoint(screen_coords[i]))     
            if on_screen:
                face_list += [[screen_coords[i] for i in face]]
                face_color += (128,128,128)
                depth += [sum(sum(vert_list[j][i] for j in face)**2 for i in range(3))]
        
        order = sorted(range(len(face_list)),key=lambda i: depth[i], reverse=0)
        for i in order:
            try:
                pygame.draw.polygon(screen, face_color[i], face_list[i])
            except: 
                pass
    pygame.display.flip()
    
pygame.quit()
exit()