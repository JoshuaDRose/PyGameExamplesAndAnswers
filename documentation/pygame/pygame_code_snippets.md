[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

"Once I get on a puzzle, I can't get off."
Richard P. Feynman

---

# Code snippets

## Minimal application loop

```py
import pygame

pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 100)
text = font.render("Text", True, (255, 255, 0))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    window_center = window.get_rect().center

    window.fill(0)
    pygame.draw.circle(window, (255, 0, 0), window_center, 100)
    window.blit(text, text.get_rect(center = window_center))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()
```

## Background

Checkered  background _Surface_:

```py
background = pygame.Surface(window.get_size())
ts, w, h, c1, c2 = 50, *background.get_size(), (128, 128, 128), (64, 64, 64)
tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
[pygame.draw.rect(background, color, rect) for rect, color in tiles]
```
