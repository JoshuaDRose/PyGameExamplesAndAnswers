# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# GitHub - PyGameExamplesAndAnswers - Clipping - Clipping with masks
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_clipping.md

import pygame

def clip_surface(surf, mask):
    clip_surf = mask.to_surface()
    clip_surf.set_colorkey(0)
    clip_surf.blit(surf, (0, 0), special_flags = pygame.BLEND_RGB_MULT)
    return clip_surf

pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

image = pygame.Surface((200, 200))
ts, w, h, c1, c2 = 20, *image.get_size(), (255, 128, 128), (255, 64, 64)
tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
for rect, color in tiles:
    pygame.draw.rect(image, color, rect)

mask_image = pygame.Surface((200, 200))
pygame.draw.polygon(mask_image, (255, 255, 255), [(100, 10), (10, 190), (190, 190)])
mask_image.set_colorkey(0)
mask = pygame.mask.from_surface(mask_image)

clipped_image = clip_surface(image, mask)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False          

    window.fill((127, 127, 127))
    window.blit(clipped_image, clipped_image.get_rect(center = window.get_rect().center))
    pygame.display.flip()

pygame.quit()
exit()