# How to open camera with pygame in Windows?
# https://stackoverflow.com/questions/29673348/how-to-open-camera-with-pygame-in-windows/29673710#29673710
# 
# python pygame.camera.init() NO vidcapture
# https://stackoverflow.com/questions/21356439/how-to-load-and-play-a-video-in-pygame
# 
# GitHub - PyGameExamplesAndAnswers - Camera and Video
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_camera_and_video.md

import pygame
import cv2

capture = cv2.VideoCapture(0)
success, camera_image = capture.read()

window = pygame.display.set_mode(camera_image.shape[1::-1])
clock = pygame.time.Clock()

run = success
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    camera_surf = pygame.image.frombuffer(
        camera_image.tobytes(), camera_image.shape[1::-1], "BGR")
    window.blit(camera_surf, (0, 0))
    pygame.display.flip()

    success, camera_image = capture.read()
    if not success:
        run = False

pygame.quit()
exit()