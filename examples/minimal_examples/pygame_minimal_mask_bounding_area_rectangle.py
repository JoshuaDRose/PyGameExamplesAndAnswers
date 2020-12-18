# pygame.mask module
# https://www.pygame.org/docs/ref/mask.html
#
# pygame.Surface object
# https://www.pygame.org/docs/ref/surface.html
#
# How to get the correct dimensions for a pygame rectangle created from an image
# https://stackoverflow.com/questions/65361582/how-to-get-the-correct-dimensions-for-a-pygame-rectangle-created-from-an-image/65361896#65361896
#
# GitHub - Sprite, Group and Sprite mask - Mask bounding area rectangle
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_sprite_and_sprite_mask.md

import pygame

def getMaskRect(surf, top = 0, left = 0):
    surf_mask = pygame.mask.from_surface(surf)
    rect_list = surf_mask.get_bounding_rects()
    surf_mask_rect = rect_list[0].unionall(rect_list)
    surf_mask_rect.x +=  top 
    surf_mask_rect.y +=  left
    return surf_mask_rect

pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

my_image = pygame.Surface((200, 200), pygame.SRCALPHA)
pygame.draw.circle(my_image, (255, 0, 255), (60, 60), 40)
pygame.draw.circle(my_image, (0, 255, 255), (100, 150), 40)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pos = window.get_rect().center
    my_image_rect = my_image.get_rect(center = pos)
    my_image_mask_rect = getMaskRect(my_image, *my_image_rect.topleft)

    window.fill(0)
    window.blit(my_image, my_image_rect)
    pygame.draw.rect(window, (255, 255, 0), my_image_rect, 1)
    pygame.draw.rect(window, (255, 128, 0), my_image_mask_rect, 1)
    pygame.display.flip()

pygame.quit()
exit()