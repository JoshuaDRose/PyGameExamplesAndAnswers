[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

---

# Display, display position, resize, coordinate system and scroll

## Video driver

Related Stack Overflow questions:

- [pygame: doesn't open window / 'pygame.error: No available video device'](https://stackoverflow.com/questions/64379965/pygame-doesnt-open-window-pygame-error-no-available-video-device)

## Display update

Related Stack Overflow questions:

- [Why is nothing drawn in PyGame at all?](https://stackoverflow.com/questions/65113967/why-is-nothing-drawn-in-pygame-at-all/65114059#65114059)  
- [Why is screen not background surface does not blit onto screen?](https://stackoverflow.com/questions/64566867/why-is-screen-not-background-surface-does-not-blit-onto-screen/65508952#65508952)  
- [Why is the PyGame animation is flickering](https://stackoverflow.com/questions/62120723/why-is-the-pygame-animation-is-flickering/62120776#62120776)  
- [How do I draw a line without updating the whole screen in pygame?](https://stackoverflow.com/questions/64620388/how-do-i-draw-a-line-without-updating-the-whole-screen-in-pygame/64620675?noredirect=1#comment114264702_64620675)  
- [How can I make the ball move instead of stretch in pygame?](https://stackoverflow.com/questions/65494890/how-can-i-make-the-ball-move-instead-of-stretch-in-pygame/65494925#65494925)  
- [pygame - surface from part of another surface](https://stackoverflow.com/questions/71538869/pygame-surface-from-part-of-another-surface/71538929#71538929)  

You need to update the display.

You are actually drawing on a [`Surface`](https://www.pygame.org/docs/ref/display.html#pygame.display.update) object. If you draw on the _Surface_ associated to the PyGame display, this is not immediately visible in the display. The changes become visible, when the display is updated with either [`pygame.display.update()`](https://www.pygame.org/docs/ref/display.html#pygame.display.update) or [`pygame.display.flip()`](https://www.pygame.org/docs/ref/display.html#pygame.display.flip).

See [`pygame.display.flip()`](https://www.pygame.org/docs/ref/display.html#pygame.display.flip):

> This will update the contents of the entire display.

## Size

Related Stack Overflow questions:

- [How do I get the size (width x height) of my pygame window](https://stackoverflow.com/questions/36653519/how-do-i-get-the-size-width-x-height-of-my-pygame-window)  

You can get the [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html) object associated with the display with [`pygame.display.get_surface()`](https://www.pygame.org/docs/ref/display.html#pygame.display.get_surface):

```py
window_surface = pygame.display.get_surface()
```

Each _Surface_ object can be asked for its with and height with [`get_width()`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.get_width) respectively [`get_height()`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.get_height):

```py
window_width = pygame.display.get_surface().get_width()
window_height = pygame.display.get_surface().get_height()
```

[`get_size()`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.get_size) returns a tuple with the width and height of the window:

```py
window_width, window_height = pygame.display.get_surface().get_size()
```

[`get_rect()`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.get_rect) returns a rectangle the size of the window, always starting at (0, 0):

This can be used to get the center of the display:

```py
window_center = pygame.display.get_surface().get_rect().center
```

It can even be used to limit the movement of an object to the window area:

```py
object_rect = pygame.Rect(x, y, w, h)
```

```py
object_rect.clamp_ip(pygame.display.get_surface().get_rect())
```

:scroll: **[minimal example - Move object with keys limit it to the window borders](../../examples/minimal_examples/pygame_minimal_move_object_limit_window.py)**

[How do I get the size (width x height) of my pygame window](https://i.stack.imgur.com/xMMCz.gif)

## Resize and resize event

Related Stack Overflow questions:

- [python pygame the background image changes with the screen size](https://stackoverflow.com/questions/59694909/python-pygame-the-background-image-changes-with-the-screen-size/59694983#59694983)
- [How to transform current pygame surface to a larger one?](https://stackoverflow.com/questions/60481977/how-to-transform-current-pygame-surface-to-a-larger-one/60483134#60483134)
- [Resize proportionally to the screen](https://stackoverflow.com/questions/55382238/resize-proportionally-to-the-screen/55387255#55387255)
- [How to put limits on resizing a window in pygame](https://stackoverflow.com/questions/18285208/how-to-put-limits-on-resizing-a-window-in-pygame)
- [python pygame use VIDEORESIZE to update the new window but the item in window not update its new position](https://stackoverflow.com/questions/60051525/python-pygame-use-videoresize-to-update-the-new-window-but-the-item-in-window-no/60051721#60051721)
- [How do I make my pygame window minimze and maximize?](https://stackoverflow.com/questions/61867449/how-do-i-make-my-pygame-window-minimze-and-maximize/61867690#61867690)
- [How to make my pygame game window resizeable?](https://stackoverflow.com/questions/62899967/how-to-make-my-pygame-game-window-resizeable/62900107#62900107)
- [Get screen orientation with Python](https://stackoverflow.com/questions/64272110/get-screen-orientation-with-python/64273980#64273980)
- [Update during resize in Pygame](https://stackoverflow.com/questions/64543449/update-during-resize-in-pygame)

When the display option `RESIZABLE` (see [`pygame.display.set_mode()`](https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode)) is set, then the `VIDEORESIZE` event (see [`pygame.event`](https://www.pygame.org/docs/ref/event.html)) occurs when the window is resized. The new size of the window can be get form the even attributes:

```py
width, height = event.w, event.h
```

Create a new Surface associated to the window and scale the background to the new size:

```py
p.init()
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

run = True
while run:
    for event in p.event.get():
        if event.type == pygame.QUIT:
            run == False
        elif event.type == pygame.VIDEORESIZE:
            width, height = event.w, event.h
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
```

:scroll: **[Minimal example - Resize](../../examples/minimal_examples/pygame_minimal_display_resize.py)**

### SDL Resize issues on Windows

Related Stack Overflow questions:

- [Update during resize in Pygame](https://stackoverflow.com/questions/64543449/update-during-resize-in-pygame/64550793#64550793)

## Fullscreen

Related Stack Overflow questions:

- [The fullscreen mode in pygame is entirely black](https://stackoverflow.com/questions/59127002/the-fullscreen-mode-in-pygame-is-entirely-black/59127089#59127089)
- [Switching to Pygame Fullscreen Mode working only one time](https://stackoverflow.com/questions/62412357/switching-to-pygame-fullscreen-mode-working-only-one-time/62413119#62413119)
- [Pygame switching from fullscreen to normal does not work](https://stackoverflow.com/questions/66387983/pygame-switching-from-fullscreen-to-normal-does-not-work/66388005#66388005)  

[`pygame.display.set_mode`](https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode) creates a [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html) object, which is associated to the window. When `pygame.display.set_mode()` is called a again, then the object which was associated to the surface before gets invalide.

You've to [`copy()`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.copy) the "old" surface:

```py
is_fullscreen = not is_fullscreen

old_surface = display_surf.copy()

setmode = FULLSCREEN if is_fullscreen else RESIZABLE
display_surf = pygame.display.set_mode(size, setmode)
display_surf.blit(old_surface, (0,0))
```

### Toggle fullscreen and maximize window

- [pygame.display.toggle_fulscreen() not working](https://stackoverflow.com/questions/64495710/pygame-display-toggle-fulscreen-not-working/64495762#64495762)
- [pygame fullscreen on second monitor](https://stackoverflow.com/questions/64495381/pygame-fullscreen-on-second-monitor)
- [How to make a pygame window fullscreen without hiding the taskbar](https://stackoverflow.com/questions/68831902/how-to-make-a-pygame-window-fullscreen-without-hiding-the-taskbar)  

See the documentation of [`pygame.display.toggle_fullscreen()`](https://www.pygame.org/docs/ref/display.html#pygame.display.toggle_fullscreen):

> Switches the display window between windowed and fullscreen modes. **This function only works under the UNIX X11 video driver.**

A workaround is presented on the Pygame Wiki [`toggle_fullscreen`](https://www.pygame.org/wiki/toggle_fullscreen?parent=CookBook) 

## Set position

Related Stack Overflow questions:

- [How to move a no frame pygame windows when user click on it?](https://stackoverflow.com/questions/57674156/how-to-move-a-no-frame-pygame-windows-when-user-click-on-it/57681853#57681853)

  :scroll: **[Minimal example - Display zoom](../../examples/minimal_examples/pygame_minimal_display_move_no_frame_window_1.py)**

- [Pygame Display Position](https://stackoverflow.com/questions/4135928/pygame-display-position)  
- [Make a pygame resizable window that can be snapped to the screen](https://stackoverflow.com/questions/62034222/make-a-pygame-resizable-window-that-can-be-snapped-to-the-screen/62035592#62035592)
- [PyGame os.environ SDL_VIDEO_WINDOW_POS does not work](https://stackoverflow.com/questions/68324163/pygame-os-environ-sdl-video-window-pos-does-not-work/68325597#68325597)  

[PyGame](https://www.pygame.org/news) is based on [Simple DirectMedia Layer (SDL)](https://www.libsdl.org/download-2.0.php). Hence you can set SDL environment variables.

See [pygame wiki - `SettingWindowPosition`](https://www.pygame.org/wiki/SettingWindowPosition):

>You can set the position of the window by using SDL environment variables before you initialise pygame. Environment variables can be set with the os.environ dict in python.
>
>```py
>x = 100
>y = 0
>import os
>os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
>
>import pygame
>pygame.init()
>screen = pygame.display.set_mode((100,100))
>```

## Scale and zoom window

Related Stack Overflow questions:

- [Scale Everything On Pygame Display Surface](https://stackoverflow.com/questions/64341589/scale-everything-on-pygame-display-surface/64341784#64341784)
- [How do I make my screen zoom in and out in pygame?](https://stackoverflow.com/questions/64079174/how-do-i-make-my-screen-zoom-in-and-out-in-pygame/64079239#64079239)
- [Zooming in and out of a PyGame window with all objects still in place](https://stackoverflow.com/questions/64936805/zooming-in-and-out-of-a-pygame-window-with-all-objects-still-in-place/64937795#64937795)  
  ![Zooming in and out of a PyGame window with all objects still in place](https://i.stack.imgur.com/qYHGr.gif)

  :scroll: **[Minimal example - Display zoom](../../examples/minimal_examples/pygame_minimal_display_zoom.py)**

  **[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-colliderect](https://replit.com/@Rabbid76/PyGame-colliderect#main.py)**

> I'm wondering if there's a way I can globally scale everything up in my game without either having to scale each sprite up individually [...]"

No there is no way. You have to scale each coordinate, each size and each surface individually. PyGame is made for images (Surfaces) and shapes in pixel units. Anyway up scaling an image will result in either a fuzzy, blurred or jagged (Minecraft) appearance.

> Is there a way I could make a seperate surface and just put that on top of the base window surface, and just scale that?

Yes  of course.

Create a _Surface_ to draw on (`win`). Use [`pygame.transform.scale()`](https://www.pygame.org/docs/ref/transform.html#pygame.transform.scale) or [`pygame.transform.smoothscale()`](https://www.pygame.org/docs/ref/transform.html#pygame.transform.smoothscale) to scale it to the size of the window and [`blit`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit) it to the actual display _Surface_ (`display_win`):

```py
display_win = pygame.display.set_mode((WINDOW_WIDTH*2, WINDOW_HEIGHT*2))
win = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))

while running:
    # [...]

    # draw to "win"

    # [...]

    scaled_win = pygame.transform.smoothscale(win, display_win.get_size())
    # or scaled_win = pygame.transform.scale(win, display_win.get_size())
    display_win.blit(scaled_win, (0, 0))
    pygame.display.flip()
```

:scroll: [Minimal example - Scale up display window](../../examples/minimal_examples/pygame_minimal_dispaly_up_scale.py)

**[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-ZoomInAndOut](https://replit.com/@Rabbid76/PyGame-ZoomInAndOut#main.py)**

## Coordinate system and transformations

Related Stack Overflow questions:

- [Rotate pygame screen](https://stackoverflow.com/questions/69394255/rotate-pygame-screen/69394709#69394709)  
  ![Rotate pygame screen](https://i.stack.imgur.com/d4WcW.png)

:scroll: **[Minimal example - Rotate screen](../../examples/minimal_examples/pygame_minimal_display_rotate_screen.py)**

- [Assosiate rects to specific window in pygame](https://stackoverflow.com/questions/70447129/assosiate-rects-to-specific-window-in-pygame/70448761#70448761)  
- [How do I change the Pygame coordinate system so that the center of the window is (0,0)?](https://stackoverflow.com/questions/61514113/how-do-i-change-the-pygame-coordinate-system-so-that-the-center-of-the-window-is/61516769#61516769)
- [pushMatrix, popMatrix, translate, and rotate in pygame?](https://stackoverflow.com/questions/63078272/pushmatrix-popmatrix-translate-and-rotate-in-pygame/63078556#63078556)  
- [Polygons on created surfaces](https://stackoverflow.com/questions/56639370/polygons-on-created-surfaces/65456150#65456150)  
- [pygame define different position order make the different result](https://stackoverflow.com/questions/59810922/pygame-define-different-position-order-make-the-different-result/59810986#59810986)

:scroll: **[Minimal example - Center the origin of the coordinate system](../../examples/minimal_examples/pygame_minimal_display_center_origin.py)**

Be aware that the y-axis needs to be reversed (`-y` respectively `y1-y2`) because the y-axis is generally pointing up but in the PyGame coordinate system the y-axis is pointing down.

## Window caption and icon

Related Stack Overflow questions:

- [How to Change the Name of a Pygame window?](https://stackoverflow.com/questions/40566585/how-to-change-the-name-of-a-pygame-window/65641908#65641908)  
- [Icons are not displayed, displayed only after closing for half a second](https://stackoverflow.com/questions/65079658/icons-are-not-displayed-displayed-only-after-closing-for-half-a-second/65079700#65079700)  
- [Why can't I change the python window icon?](https://stackoverflow.com/questions/65809541/why-cant-i-change-the-python-window-icon)  
- [pygame.display.set_icon(pygame.image obj) doesn't work in python 3.9.1](https://stackoverflow.com/questions/65454856/pygame-display-set-iconpygame-image-obj-doesnt-work-in-python-3-9-1/65454866#65454866)
- [how to set a picture as an app icon in pygame in ubuntu](https://stackoverflow.com/questions/63717695/how-to-set-a-picture-as-an-app-icon-in-pygame-in-ubuntu/63717754#63717754)
- [pygame collision detection causes my computer to hang](https://stackoverflow.com/questions/60323509/pygame-collision-detection-causes-my-computer-to-hang/60327662#60327662)

## Scroll background

Related Stack Overflow questions:

- [Making the background move sideways in pygame](https://stackoverflow.com/questions/55050166/making-the-background-move-sideways-in-pygame/55068602#55068602)

  :scroll: **[Minimal example - Scroll background vertical](../../examples/minimal_examples/pygame_minimal_display_scroll_background_1.py)**

- [How to scroll the background surface in PyGame?](https://stackoverflow.com/questions/55319181/how-to-scroll-the-background-surface-in-pygame/55321731#55321731)  
  ![How to scroll the background surface in PyGame?](https://i.stack.imgur.com/QosjL.gif)

  :scroll: **[Minimal example - Scroll background vertical](../../examples/minimal_examples/pygame_minimal_display_scroll_background_2.py)**

- [How to move the background image with keys in pygame?](https://stackoverflow.com/questions/61039508/how-to-move-the-background-image-with-keys-in-pygame/61039821#61039821)
- [Pygame : Two layered scrolling background, can you help me?](https://stackoverflow.com/questions/55454487/pygame-two-layered-scrolling-background-can-you-help-me/55460386#55460386)

- [How to move the player across a one background image?](https://stackoverflow.com/questions/67736156/how-to-move-the-player-across-a-one-background-image/67741682#67741682)  
  ![How to move the player across a one background image?](https://i.stack.imgur.com/Mb09D.gif)

  :scroll: **[Minimal example - Scroll background with player](../../examples/minimal_examples/pygame_minimal_display_scroll_background_3.py)**

- [How to continuously move an image smoothly in Pygame?](https://stackoverflow.com/questions/67944873/how-to-continuously-move-an-image-smoothly-in-pygame/67946424#67946424)  
  ![How to continuously move an image smoothly in Pygame?](https://i.stack.imgur.com/7Rexy.gif)

- [How to move the player across a one background image?](https://stackoverflow.com/questions/67736156/how-to-move-the-player-across-a-one-background-image?noredirect=1#comment119731761_67736156)  
  ![How to move the player across a one background image?](https://i.stack.imgur.com/Mb09D.gif)

If you want to have a continuously repeating background, then you've to draw the background twice:

```lang.none
        +==================+
   +----||---------+------||------+
   |    ||         |      ||      |
   |    ||    1    |   2  ||      |
   |    ||         |      ||      |
   +----||---------+------||------+
        +==================+
```

You've to know the size of the screen. The size of the height background image should match the height of the screen. The width of the background can be different, but should be at least the with of the window (else the background has to be drawn more than 2 times).

```py
bg_w, gb_h = size
bg =  pygame.transform.smoothscale(pygame.image.load('background.image'), (bg_w, bg_h))
```

The background can be imagined as a endless row of tiles.
If you want to draw the background at an certain position `pos_x`, then you have to calculate the position of the tile relative to the screen by the modulo (`%`) operator. The position of the 2nd tile is shifted by the width of the background (`bg_w`):

```py
x_rel = pos_x % bg_w
x_part2 = x_rel - bg_w if x_rel > 0 else x_rel + bg_w
```

Finally the background has to be _blit_ twice, to fill the entire screen:

```py
screen.blit(bg, (x_rel, 0))
screen.blit(bg, (x_part2, 0))
```

## Message box

Related Stack Overflow questions:

- [Is there a way to make the message box show up in front of a PyGame Window?](https://stackoverflow.com/questions/60990283/is-there-a-way-to-make-the-message-box-show-up-in-front-of-a-pygame-window/60993478#60993478)

## Multiple Windows

Related Stack Overflow questions:

- [Pygame with Multiple Windows](https://stackoverflow.com/questions/29811814/pygame-with-multiple-windowsv)
