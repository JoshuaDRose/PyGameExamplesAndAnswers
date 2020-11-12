[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

"Once I get on a puzzle, I can't get off."  
Richard P. Feynman

---

# Scale and zoom

## Scale surface

Related Stack Overflow questions:

- [How can i reshape an array from (280, 280, 3) to (28, 28, 3)](https://stackoverflow.com/questions/62391656/how-can-i-reshape-an-array-from-280-280-3-to-28-28-3/62392403#62392403)
- [What does the parameter DestSurface in Pygame.transform.scale mean and how do I use it?](https://stackoverflow.com/questions/60045882/what-does-the-parameter-destsurface-in-pygame-transform-scale-mean-and-how-do-i/60045993#60045993)
- [How do i properly rescale an image on PyGame without it being badly cropped?](https://stackoverflow.com/questions/55319967/how-do-i-properly-rescale-an-image-on-pygame-without-it-being-badly-cropped/55321552#55321552)
- [Set the width and height of a pygame surface](https://stackoverflow.com/questions/62467003/set-the-width-and-height-of-a-pygame-surface/62467567#62467567)
- [Resize Image Content but Keep Image Dimensions](https://stackoverflow.com/questions/63648196/resize-image-content-but-keep-image-dimensions/63648597#63648597)

[`pygame.transform.scale()`](https://www.pygame.org/docs/ref/surface.html) does not scale the input Surface itself. It creates a new surface and does a scaled "blit" to the new surface. The new surface is returned by the return value:

`pygame.transform.scale()` does:

1. Creates a new surface (`newSurface`) with size `(width, height)`.
2. Scale and copy `Surface` to `newSurface`.
3. Return `newSurface`.

The destination surface is a [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html) where the scaled surface is copied to. That is quicker, because the memory for the Surface has not to be allocated.

It `DestSurface` is set, then `pygame.transform.scale()` does:

1. Scale and copy `Surface` to the `DestSurface`.
2. Return `DestSurface`.

For that reason, the size of `DestSurface` has to be `(width, height)`, the format of `DestSurface` has the same as the format of `Surface`.

A possible use case is if you have to continuously scale something to a fixed size in the main application loop (e.g. if the surface is dynamically generated). In the following `surf` is assumed to be a surface object:

```py
while True:
    # [...]

    scaledSurf = pygame.transform.scale(surf, (100, 100)) 
    window.blit(scaledSurf, (x, y)
```

The code can be improved by using the `DestSurface` parameter:

```py
scaledSurf = pygame.Surface((100, 100))

while True:
    # [...]

    pygame.transform.scale(surf, (100, 100), scaledSurf) 
    window.blit(scaledSurf, (x, y)
```

That is probably a rare case. In general you should try to scale the surfaces at the initialization, rather than continuously in the application loop and to use the scaled surfaces in the loop. 

Do not try to use the parameter compulsively and do not "construct" a use case for the `DestSurface` parameter. Do it the other way around. Write your application and make it run. Then investigate whether the `DestSurface` parameter can be an improvement for your specific use case.


## Zoom surface

Related Stack Overflow questions:

- [pygame.transform.scale does not work on the “game” surface](https://stackoverflow.com/questions/56407891/pygame-transform-scale-does-not-work-on-the-game-surface/56408482#56408482)
- [Manipulating rect image size in pygame](https://stackoverflow.com/questions/59919826/manipulating-rect-image-size-in-pygame/59919909#59919909)  
  ![Manipulating rect image size in pygame](https://i.stack.imgur.com/soWSp.gif)

Define a zoom factor and calculate the size of the of the zoom area. e.g. If the zoom factor is 2, the area that needs to be zoomed on the window is half the width and height of the window:

```py
zoom = 2

wnd_w, wnd_h = window.get_size()
zoom_size = (round(wnd_w/zoom), round(wnd_h/zoom))
```

Define the rectangular zoom area. The center point of the area is the position where to zoom to. (e.g the cursor position):

```py
zoom_area = pygame.Rect(0, 0, *zoom_size)
zoom_area.center = (pos_x, pos_y)
```

Create a new [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.get_clip) with the size of the zoom area and copy the region of the window to the surface, by using [`,blit`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit), where the `area` parameter is set to the zoom region:

```py
zoom_surf = pygame.Surface(zoom_area.size)
zoom_surf.blit(screen, (0, 0), zoom_area)
```

Scale `zoom_surf` by either [`pygame.transform.scale()`](https://www.pygame.org/docs/ref/transform.html#pygame.transform.scale) or [`pygame.transform.smoothscale()`](https://www.pygame.org/docs/ref/transform.html#pygame.transform.smoothscale):

```py
zoom_surf = pygame.transform.scale(zoom_surf, (wnd_w, wnd_h))
```

Now `zoom_surf` has the same size as the window. `.blit` the surface to the window:

```py
window.blit(zoom_surf, (0, 0))
``` 