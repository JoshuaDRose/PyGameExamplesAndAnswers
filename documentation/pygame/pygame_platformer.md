
[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

---

# Jump 'n' Run and Platformer

Related Stack Overflow questions:

- [Issue with Collision Detection in Pygame for simple 2D Platformer](https://stackoverflow.com/questions/66127646/issue-with-collision-detection-in-pygame-for-simple-2d-platformer/66127881#66127881)

## Scrolling - Center to player

Related Stack Overflow questions:

- [Add scrolling to a platformer in pygame](https://stackoverflow.com/questions/14354171/add-scrolling-to-a-platformer-in-pygame)  

Unfortunately, Pygame doesn't have a built-in solution to this problem. Pygame use [`pygame.sprite.Sprite`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite) objects organized in [`pygame.sprite.Group`s](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group). The attribute `.rect` of the _Sprites_ is used for drawing the objects as well as for the collision test between objects. There is no built-in feature that can convert object coordinates to screen coordinates before drawing.  
As a suggestion for the pygame developers: It would be nice to have an optional argument for the camera _offset_ in the method [`pygame.sprite.Group.draw`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group.draw).

There a different approaches:

- Instead of moving the player, you can move any object in the scene in the opposite direction. This is the worst of all approaches. I strongly recommend not doing this.
  Every time you add a new object you need to make sure that it moves as the player moves. Dealing with object animation or floating point accuracy can turn out to be a nightmare.

- Create a virtual screen size of the world and draw the entire screen on the virtual screen. At the end of each frame, a subsection of the map is displayed on the screen.
  
  ```py
  virtual_screen = pygame.Surface((map_width, map_height))
  ```

  There are 2 possibilities. You can [`blit`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit) an area of the virtual screen directly on the screen by specifying the _area_ argument:

  ```py
  camera_area = pygame.Rect(camera_x, camera_y, camera_width, camera_height)
  screen.blit(virtual_screen, (0, 0), camera_area)
  ```

  The other possibility is to define a subsurface that is linked directly to the source surface using the[`subsurface`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.subsurface) method

  ```py
  camera_area = pygame.Rect(camera_x, camera_y, camera_width, camera_height)
  camera_subsurf = source_surf.subsurface(camera_area)
  ```

  ```py
  screen.blit(camera_subsurf, (0, 0))
  ```

  The disadvantage of this approach is that it can have a very large memory footprint. If the virtual screen is huge, the game will lag. This solution is only suitable if the size of the game area is not much larger than the screen. As a rule of thumb, if the play area is more than twice the size of the screen, you shouldn't go this way (I'm talking about twice the size of the area, not twice the length of its width and height).

- For large play areas, the only approach that can be used is to add an offset to the objects before drawing

  ```py
  offset_x = -camera_x
  offset_y = -camera_y
  for object in objects:
      screen.blit(object.image, (object.rect.x + offset_x, object.rect.y + offset_y))
  ```

  Unfortunately [`pygame.sprite.Group.draw`](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group) can not be used directly in this case. This approach is detailed in a highly rated answer.
