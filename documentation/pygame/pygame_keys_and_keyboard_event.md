[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

"You should name a variable using the same care with which you name a first-born child."  
Robert C. Martin, Clean Code: A Handbook of Agile Software Craftsmanship

---

# Keys and keyboard events

Related Stack Overflow questions:

- [How to get keyboard input in pygame?](https://stackoverflow.com/questions/16044229/how-to-get-keyboard-input-in-pygame/64494842#64494842)  
- [How can I make a sprite move when key is held down](https://stackoverflow.com/questions/9961563/how-can-i-make-a-sprite-move-when-key-is-held-down)  

## Key state

**What does `pygame.key.get_pressed()` do?**

Related Stack Overflow questions:

- [How to hold a 'key down' in Pygame?](https://stackoverflow.com/questions/63816977/how-to-hold-a-key-down-in-pygame/63817093#63817093)
- [How to get if a key is pressed pygame](https://stackoverflow.com/questions/59830738/how-to-get-if-a-key-is-pressed-pygame/59831073#59831073)
- [“Tuple object not callable” when inspecting the result of pygame.key.get_pressed()](https://stackoverflow.com/questions/62666910/tuple-object-not-callable-when-inspecting-the-result-of-pygame-key-get-pressed/62669811#62669811)
- [Why use (bitwise) & when handling keyboard events involving multiple keys?](https://stackoverflow.com/questions/65219618/why-use-bitwise-when-handling-keyboard-events-involving-multiple-keys/65219714#65219714)
- [Confused by pygame key.get_pressed() method](https://stackoverflow.com/questions/59457872/confused-by-pygame-key-get-pressed-method/65367962#65367962)
- [Pygame's pygame.event.get()'s key value is a ridiculous number as of today, why?](https://stackoverflow.com/questions/66665341/pygames-pygame-event-gets-key-value-is-a-ridiculous-number-as-of-today-why/66667449#66667449)

[`pygame.key.get_pressed()`](https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed) returns a sequence with the state of each key. If a key is held down, the state for the key is `True`, otherwise `False`. Use [`pygame.key.get_pressed()`](https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed) to evaluate the current state of a button and get continuous movement

## Key repeat

Related Stack Overflow questions:

- [Detect single key press using key.get_pressed()](https://stackoverflow.com/questions/65266365/detect-single-key-press-using-key-get-pressed/65267063#65267063)  
- [Why is pygame.KEYUP event triggering when the key has not been released?](https://stackoverflow.com/questions/53525617/why-is-pygame-keyup-event-triggering-when-the-key-has-not-been-released/65658666#65658666)  

## Keyboard event

**What is `pygame.KEYDOWN`, `pygame.KEYUP`?**

Related Stack Overflow questions:

- **[Getting Pygame keyboard input and check if it's a number](https://stackoverflow.com/questions/64124050/getting-pygame-keyboard-input-and-check-if-its-a-number/64124342#64124342)**
- [Python Pygame press two direction key and another key to shoot there's no bullet](https://stackoverflow.com/questions/59004524/python-pygame-press-two-direction-key-and-another-key-to-shoot-theres-no-bullet/59005776#59005776)
- [Problem when using keyboard commands in pygame](https://stackoverflow.com/questions/58299480/problem-when-using-keyboard-commands-in-pygame/58307655#58307655)
- [How to get a variable keyboard input in pygame?](https://stackoverflow.com/questions/63449626/how-to-get-a-variable-keyboard-input-in-pygame/63449886#63449886)
- [Pygame keys convention](https://stackoverflow.com/questions/64651122/pygame-keys-convention/64651187#64651187)  
- [python why wont this accept upper case or symbols](https://stackoverflow.com/questions/16422264/python-why-wont-this-accept-upper-case-or-symbols/65335937#65335937)

The keyboard events `KEYDOWN` and `KEYUP` (see [pygame.event](https://www.pygame.org/docs/ref/event.html) module) create a [`pygame.event.Event`](https://www.pygame.org/docs/ref/event.html#pygame.event.Event) object with additional attributes. The key that was pressed can be obtained from the `key` attribute (e.g. `K_RETURN `, `K_a`) and the `mod` attribute contains a bitset with additional modifiers (e.g. `KMOD_LSHIFT`). The `unicode` attribute provides the Unicode representation of the keyboard input.

The keyboard events (see [pygame.event](https://www.pygame.org/docs/ref/event.html) module) occur only once when the state of a key changes. The `KEYDOWN` event occurs once every time a key is pressed. `KEYUP` occurs once every time a key is released. Use the keyboard events for a single action or a step-by-step movement.

[`pygame.key.get_pressed()`](https://www.pygame.org/docs/ref/key.html) returns a list with the state of all keyboard buttons. This is not intended to get the key of a keyboard event. The key that was pressed can be obtained from the `key` attribute of the [`pygame.event.Event`](https://www.pygame.org/docs/ref/event.html#pygame.event.Event) object:

```py
if event.type == pg.KEYDOWN:
    if event.key == pg.K_a:
        # [...]
```

`unicode` contains a single character string that is the fully translated character:

```py
if event.type == pg.KEYDOWN:
    if event.unicode == 'a':
        # [...]
```

See also [`pygame.event`](https://www.pygame.org/docs/ref/event.html) module and [pygame.key](https://www.pygame.org/docs/ref/key.html).

If you press **UP** + **LEFT** + **SPACE** then the **SPACE** key doesn't appear to be pressed immediately. You've to release the **UP** or **LEFT** key to get the `pygame.KEYDOWN` event for **SPACE**.  

This is a known bug in pygame and doesn't seem to be solved yet: [Incorrect handling of pressed keys #235](https://github.com/pygame/pygame/issues/235).

Sadly even [`pygame.key.get_pressed()`](https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed) doesn't state the **SPACE** key in this case, so I can't even think a workaround.

While `pygame.K_f` is a key enumerator constant (see [`pygame.key`](https://www.pygame.org/docs/ref/key.html)) the content of `event.type` is event enumerator constant (see [`pygame.event`](https://www.pygame.org/docs/ref/event.html)).  
If you want to determine if a certain key is pressed, the you've to verify if the event type is `pygame.KEYDOWN` (or `pygame.KEYUP` for button release) and if the `.key` attribute of the event is equal the key enumerator. e.g.:

```py
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        self.quit()

    # [...]

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_f:
            # [...]
```

## Detecting key states and events

### Difference between key state key event

Related Stack Overflow questions:

- **[How to get keyboard input in pygame?](https://stackoverflow.com/questions/16044229/how-to-get-keyboard-input-in-pygame/64494842#64494842)**  
  [How can I make a sprite move when key is held down](https://stackoverflow.com/questions/9961563/how-can-i-make-a-sprite-move-when-key-is-held-down)  
  ![How can I make a sprite move when key is held down](https://i.stack.imgur.com/S24dj.gif)

  :scroll: **[minimal example - Move object with keys](../../examples/minimal_examples/pygame_minimal_move_object.py)**

  **[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-ContinuousMovement](https://replit.com/@Rabbid76/PyGame-ContinuousMovement#main.py)**

- [What all things happens inside pygame when I press a key? When to use pygame.event==KEYDOWN](https://stackoverflow.com/questions/63050139/what-all-things-happens-inside-pygame-when-i-press-a-key-when-to-use-pygame-eve/63056690#63056690)
- [PyGame press two buttons at the same time](https://stackoverflow.com/questions/59181962/pygame-press-two-buttons-at-the-same-time/59182228#59182228)
- [Pygame Keys Activating in Multiple Frames](https://stackoverflow.com/questions/64540381/pygame-keys-activating-in-multiple-frames/64540554#64540554)
- [How to make the snake continue in that direction until another arrow key is pressed](https://stackoverflow.com/questions/64902377/how-to-make-the-snake-continue-in-that-direction-until-another-arrow-key-is-pres/64902458#64902458)

[`pygame.key.get_pressed()`](https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed) returns a list with the state of each key. If a key is held down, the state for the key is `True`, otherwise `False`. Use [`pygame.key.get_pressed()`](https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed) to evaluate the current state of a button and get continuous movement:

```py
while True:

    keys = pygame.key.get_pressed()
    x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * speed
    y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * speed
```

The keyboard events (see [pygame.event](https://www.pygame.org/docs/ref/event.html) module) occur only once when the state of a key changes. The `KEYDOWN` event occurs once every time a key is pressed. `KEYUP` occurs once every time a key is released. Use the keyboard events for a single action or a step-by-step movement

```py
while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= speed
            if event.key == pygame.K_RIGHT:
                x += speed
            if event.key == pygame.K_UP:
                y -= speed
            if event.key == pygame.K_DOWN:
                y += speed
```

### When is the key state used and when the keyboard event

When does it make sense to use keyboard events (`pygame.KEYDOWN`, `pygame.KEYUP` see [`pygame.event`](https://www.pygame.org/docs/ref/event.html)), and when is it better to get the state of the keys ([`pygame.key.get_pressed()`](https://www.pygame.org/docs/ref/key.html))?

Related Stack Overflow questions:

- [Python only running while loop once](https://stackoverflow.com/questions/59706667/python-only-running-while-loop-once/59706711#59706711)
- [I want my character to do something as long as I'm holding a button, then go back to normal once I let go of the button](https://stackoverflow.com/questions/60741355/i-want-my-character-to-do-something-as-long-as-im-holding-a-button-then-go-bac/60742556#60742556)
- [how to control snake with only two keys i.e left and right](https://stackoverflow.com/questions/61862293/how-to-control-snake-with-only-two-keys-i-e-left-and-right/61863664#61863664)
- [how to drop a bomb in character position in a pygame game](https://stackoverflow.com/questions/62066092/how-to-drop-a-bomb-in-character-position-in-a-pygame-game/62067605#62067605)
- [how to make rectangle “sprint”](https://stackoverflow.com/questions/64209885/how-to-make-rectangle-sprint/64209944#64209944)
- [How to put a variable into pygame key detector?](https://stackoverflow.com/questions/64717181/how-to-put-a-variable-into-pygame-key-detector)
- [How do I get the size (width x height) of my pygame window](https://stackoverflow.com/questions/36653519/how-do-i-get-the-size-width-x-height-of-my-pygame-window) 

Use the keyboard events (`KEYDOWN`,` ​​KEYUP`) for actions like jumping or spawning a bullet.

:scroll: **[minimal example - Move object with keys](../../examples/minimal_examples/pygame_minimal_move_object.py)**

**[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-ContinuousMovement](https://replit.com/@Rabbid76/PyGame-ContinuousMovement#main.py)**

![How can I make a sprite move when key is held down](https://i.stack.imgur.com/S24dj.gif)

:scroll: **[minimal example - Move object with keys limit it to the window borders](../../examples/minimal_examples/pygame_minimal_move_object_limit_window.py)**

[How do I get the size (width x height) of my pygame window](https://i.stack.imgur.com/xMMCz.gif)

:scroll: **[minimal example - Move object fast when key is hit twice](../../examples/minimal_examples/pygame_minimal_move_object_fast_on_key_twice.py)**

:scroll: **[minimal example - Move object fast when key is in opposite direction is hit](../../examples/minimal_examples/pygame_minimal_move_object_slow_on_opposite_key.py)**

### Shoot bullet

Related Stack Overflow questions:

- [How can i shoot a bullet with space bar?](https://stackoverflow.com/questions/59687250/how-can-i-shoot-a-bullet-with-space-bar/59689297#59689297)  
  ![How can i shoot a bullet with space bar?](https://i.stack.imgur.com/2sp5D.gif)

  :scroll: **[minimal example - Sustained fire](../../examples/minimal_examples/pygame_minimal_shoot_bullet_sustained_fire.py)**

  **[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-ShootBulletSustainedFire](https://replit.com/@Rabbid76/PyGame-ShootBulletSustainedFire#main.py)**

- [How do I stop more than 1 bullet firing at once?](https://stackoverflow.com/questions/60122492/how-do-i-stop-more-than-1-bullet-firing-at-once/60125448#60125448)  
  ![How do I stop more than 1 bullet firing at once?](https://i.stack.imgur.com/W6lzh.gif)

  :scroll: **[minimal example - Shoot bullet](../../examples/minimal_examples/pygame_minimal_shoot_bullet.py)**

  **[![](https://i.stack.imgur.com/5jD0C.png) repl.it/@Rabbid76/PyGame-ShootBullet](https://replit.com/@Rabbid76/PyGame-ShootBullet#main.py)**

- [Pygame: problems with shooting in Space Invaders](https://stackoverflow.com/questions/65759929/pygame-problems-with-shooting-in-space-invaders/65759972#65759972)  
  ![Pygame: problems with shooting in Space Invaders](https://i.stack.imgur.com/bSRed.gif)

- [Pygame How to check for second press of a key](https://stackoverflow.com/questions/65832446/pygame-how-to-check-for-second-press-of-a-key/65832768#65832768)  
  ![Pygame How to check for second press of a key](https://i.stack.imgur.com/vl3gn.gif)

The general approach to firing bullets is to store the positions of the bullets in a list (`bullet_list`). When a bullet is fired, add the bullet's starting position (`[start_x, start_y]`) to the list. The starting position is the position of the object (player or enemy) that fires the bullet. Use a `for`-loop to iterate through all the bullets in the list. Move position of each individual bullet in the loop. Remove a bullet from the list that leaves the screen (`bullet_list.remove(bullet_pos)`). For this reason, a copy of the list (`bullet_list[:]`) must be run through (see [How to remove items from a list while iterating?](https://stackoverflow.com/questions/1207406/how-to-remove-items-from-a-list-while-iterating)). Use another ` for`-loop to `blit` the remaining bullets on the screen:

```py
bullet_list = []

while run == True:
    # [...]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_list.append([start_x, start_y])

    for bullet_pos in bullet_list[:]:
        bullet_pos[0] += move_bullet_x
        bullet_pos[1] += move_bullet_y
        if not screen.get_rect().colliderect(bullet_image.get_rect(center = bullet_pos))
            bullet_list.remove(bullet_pos)

    # [...]

    for bullet_pos in bullet_list[:]
        screen.blit(bullet_image, bullet_image.get_rect(center = bullet_pos))

    # [...]
```

## Key representation

Related Stack Overflow questions:

- [pygame get key pressed as a string](https://stackoverflow.com/questions/59935639/pygame-get-key-pressed-as-a-string/59935886#59935886)  

A user friendly name of a key can be get by `pygame.key.name()`:

```py
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:

        print(pygame.key.name(event.key))
```
