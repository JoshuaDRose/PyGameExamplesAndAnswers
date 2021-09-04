[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

---

# Camera and Video

## Camera

Related Stack Overflow questions:

- [python pygame.camera.init() NO vidcapture](https://stackoverflow.com/questions/16266244/python-pygame-camera-init-no-vidcapture)
- [How to open camera with pygame in Windows?](https://stackoverflow.com/questions/29673348/how-to-open-camera-with-pygame-in-windows/29673710#29673710)

:scroll: **[Minimal example - Camera capture](../../examples/minimal_examples/pygame_minimal_video_camera.py)**

The [`pygame.camera`](https://www.pygame.org/docs/ref/camera.html) is only supported on linux:

> Pygame currently supports only Linux and v4l2 cameras.

An alternative solution is to use the [OpenCV `VideoCapture`](https://docs.opencv.org/master/d8/dfe/classcv_1_1VideoCapture.html). Install OpenCV for Python (_cv2_) (see [opencv-python](https://pypi.org/project/opencv-python/)).

Opens a camera for video capturing:

```py
capture = cv2.VideoCapture(0)
```

Grabs a camera frame:

```py
success, camera_image = capture.read()
```

Convert the camera frame to a [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html) object with [`pygame.image.frombuffer`](https://www.pygame.org/docs/ref/image.html#pygame.image.frombuffer):

```py
camera_surf = pygame.image.frombuffer(camera_image.tobytes(), camera_image.shape[1::-1], "BGR")
```

## Video

Related Stack Overflow questions:

- [How to play video in Pygame currently?](https://stackoverflow.com/questions/62870381/how-to-play-video-in-pygame-currently)