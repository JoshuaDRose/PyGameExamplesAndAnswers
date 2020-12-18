[![StackOverflow](https://stackexchange.com/users/flair/7322082.png)](https://stackoverflow.com/users/5577765/rabbid76?tab=profile) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [![reply.it](../../resource/logo/Repl_it_logo_80.png) reply.it](https://repl.it/repls/folder/PyGame%20Examples)

---

# Miscellaneous

## Version issues

Related Stack Overflow questions:

- [ImportError: No module named 'pygame'](https://stackoverflow.com/questions/18317521/importerror-no-module-named-pygame/64494572#64494572)

The current [PyGame](https://www.pygame.org/news) release, 1.9.6 doesn't support Python 3.9. I fyou don't want to wait for PyGame 2.0, you have to use Python 3.8. Alternatively, you can install a developer version by explicitly specifying the version (_2.0.0.dev20_ is the latest release at the time of writing):

```
pip install pygame==2.0.0.dev20
```

or try to install a pre-release version by enabling the `--pre` option:

```
pip install pygame --pre
```

### Windows

Related Stack Overflow questions:

- [Unable to install pygame on Python 3.8 via pip (Windows 10)](https://stackoverflow.com/questions/58489348/unable-to-install-pygame-on-python-3-8-via-pip-windows-10)
- [How to troubleshoot python import error - DLL access denied](https://stackoverflow.com/questions/49127425/how-to-troubleshoot-python-import-error-dll-access-denied)
- [When I try to install pygame using python 3.9 I get an error windows](https://stackoverflow.com/questions/64261106/when-i-try-to-install-pygame-using-python-3-9-i-get-an-error-windows)

### Mac

Related Stack Overflow questions:

- [Problems getting pygame to show anything but a blank screen on Macos Mojave](https://stackoverflow.com/questions/52718921/problems-getting-pygame-to-show-anything-but-a-blank-screen-on-macos-mojave)
- [pygame installation issue in mac os](https://stackoverflow.com/questions/22974339/pygame-installation-issue-in-mac-os)
- [Pygame 1.9.6 not loading in Python 3.8.1](https://stackoverflow.com/questions/59691131/pygame-1-9-6-not-loading-in-python-3-8-1)
- [Pygame not showing anything in the window](https://stackoverflow.com/questions/53182886/pygame-not-showing-anything-in-the-window)
- [Error when installing PyGame on Mac (Catalina) [duplicate]](https://stackoverflow.com/questions/60132717/error-when-installing-pygame-on-mac-catalina)

### Ubuntu

- [Pygame already installed; however, python terminal says “No module named 'pygame' ” (Ubuntu 20.04.1)](https://stackoverflow.com/questions/64016215/pygame-already-installed-however-python-terminal-says-no-module-named-pygame/64016373#64016373)

## File access

Related Stack Overflow questions:

- **[pygame.image.load('sprite/test_bg.jpg'): pygame.error: Couldn't open sprite/test_bg.jpg](https://stackoverflow.com/questions/58177145/pygame-image-loadsprite-test-bg-jpg-pygame-error-couldnt-open-sprite-test)**
- **[Is there any other way to load image in pygame?](https://stackoverflow.com/questions/64835525/is-there-any-other-way-to-load-image-in-pygame)**
- [Is there any other way to load image in pygame?](https://stackoverflow.com/questions/64835525/is-there-any-other-way-to-load-image-in-pygame/64835607#64835607)
- [Error - pygame.error: Couldn't open backround.png. Fix?](https://stackoverflow.com/questions/57836528/error-pygame-error-couldnt-open-backround-png-fix/57836574#57836574)
- [I've got an error when trying to create sound using pygame](https://stackoverflow.com/questions/55784793/ive-got-an-error-when-trying-to-create-sound-using-pygame/55784882#55784882)

The image file path has to be relative to the current working directory. The working directory is possibly different to the directory of the python file.

The name and path of the file can be get by [`__file__`](https://docs.python.org/3/reference/import.html#import-related-module-attributes). The current working directory can be get by [`os.getcwd()`](https://docs.python.org/3/library/os.html) and can be changed by [`os.chdir(path)`](https://docs.python.org/3/library/os.html).

One solution is to change the working directory:

```py
import os

sourceFileDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(sourceFileDir)
```

An alternative solution is to find the absolute path.
If the image is relative to the folder of the python file (or even in the same folder), then you can get the directory of the file and join ([`os.path.join()`](https://docs.python.org/3/library/os.path.html)) the image filename. e.g.:

```py
import pygame
import os

# get the directory of this file
sourceFileDir = os.path.dirname(os.path.abspath(__file__))

# [...]

# join the filepath and the filename
imgPath = os.path.join(sourceFileDir, 'test_bg.jpg')
# imgPath = os.path.join(sourceFileDir, '_pycache_/test_bg.jpg')

surface = pygame.image.load(imgPath)
```

## Errors

### Local and global variables

[Python Global Keyword](https://www.programiz.com/python-programming/global-keyword)

- [Python pygame - bouncing ball (UnboundLocalError: local variable 'move_y' referenced before assignment)](https://stackoverflow.com/questions/65153237/python-pygame-bouncing-ball-unboundlocalerror-local-variable-move-y-refere/65154942#65154942)

In Python, a variable declared outside of the function or in global scope is known as a global variable. This means that a global variable can be accessed inside or outside of the function.  
A variable declared inside the function's body or in the local scope is known as a local variable.  
Reading a local variable `x` before it is declared causes the error:

> UnboundLocalError: local variable `x` referenced before assignment

You have to use the global statement if you want to be interpret the variable as global variable.

## Math

- [How to draw a rectangle around two points](https://stackoverflow.com/questions/62008684/how-to-draw-a-rectangle-around-two-points/62008841#62008841)
- [I am wondering why it says the distance has to be less than 27? Why less than 27? Where is 27 coming from?](https://stackoverflow.com/questions/62523256/i-am-wondering-why-it-says-the-distance-has-to-be-less-than-27-why-less-than-27/62527566#62527566)  
- [Why is the math of my stacking game not working?](https://stackoverflow.com/questions/64598428/why-is-the-math-of-my-stacking-game-not-working/64598693#64598693)  

## Delete, remove Object

Tag: delete object, remove object, erase object, delete image, remove image, erase image

Related Stack Overflow questions:

- [how to make image/images disappear in pygame?](https://stackoverflow.com/questions/61480115/how-to-make-image-images-disappear-in-pygame/61480380#61480380)
- [How to delete one object from a Surface instance (pygame)?](https://stackoverflow.com/questions/62859831/how-to-delete-one-object-from-a-surface-instance-pygame/62860003)
- [How do I delete rect object from screen once player collides with it?](https://stackoverflow.com/questions/62957899/how-do-i-delete-rect-object-from-screen-once-player-collides-with-it/62958077#62958077)

## Grid

[Image loading using pygame](https://stackoverflow.com/questions/60617748/image-loading-using-pygame/60622756#60622756)

[Blitting images onto a tile that is part of a grid in pygame](https://stackoverflow.com/questions/59121989/blitting-images-onto-a-tile-that-is-part-of-a-grid-in-pygame/59124520#59124520)  
![scene](https://i.stack.imgur.com/9WgWJ.png)

[Pygame lags after drawing full window grid](https://stackoverflow.com/questions/61650325/pygame-lags-after-drawing-full-window-grid/61650969#61650969)

[Python pygame converting drawing to an image](https://stackoverflow.com/questions/61678353/python-pygame-converting-drawing-to-an-image/61678449#61678449)

[how can I edit a sudoku grid in pygame using mouse and keyboard detection?](https://stackoverflow.com/questions/62345206/how-can-i-edit-a-sudoku-grid-in-pygame-using-mouse-and-keyboard-detection/62345586#62345586)

[Colour chainging problem and non dupicates](https://stackoverflow.com/questions/63538350/colour-chainging-problem-and-non-dupicates/63538548#63538548)  
![scene](https://i.stack.imgur.com/81Tvv.gif)

[Get a sprites position so that the next sprite can be placed near it](https://stackoverflow.com/questions/63871620/get-a-sprites-position-so-that-the-next-sprite-can-be-placed-near-it/63873027#63873027)

[Python: How to make drawn elements snap to grid in pygame](https://stackoverflow.com/questions/63926261/python-how-to-make-drawn-elements-snap-to-grid-in-pygame/63926759#63926759)  
![scene](https://i.stack.imgur.com/VCmuV.gif)

[Pygame: tweening error in movement in tile based game](https://stackoverflow.com/questions/63478615/pygame-tweening-error-in-movement-in-tile-based-game/65338538#65338538)  
![Pygame: tweening error in movement in tile based game](https://i.stack.imgur.com/Gapfj.gif)

[Plotting pieces on a checkerboard using pygame](https://stackoverflow.com/questions/65309004/plotting-pieces-on-a-checkerboard-using-pygame/65309258#65309258)  

## Where is 27 coming from?

[I am wondering why it says the distance has to be less than 27? Why less than 27? Where is 27 coming from?](https://stackoverflow.com/questions/62523256/i-am-wondering-why-it-says-the-distance-has-to-be-less-than-27-why-less-than-27/62527566#62527566)

[Collision detection in pygame not working](https://stackoverflow.com/questions/64393985/collision-detection-in-pygame-not-working/64394459#64394459)

## Collection

[Pygame Basic calculator](https://stackoverflow.com/questions/63200489/pygame-basic-calculator)  
![scene](https://i.stack.imgur.com/tbIt8.gif)

[How to draw with mouse and save as 1s and 0s](https://stackoverflow.com/questions/58847079/how-to-draw-with-mouse-and-save-as-1s-and-0s/58850614#58850614)  
![scene](https://i.stack.imgur.com/hMHD8.gif)

[Is there anyway to do this recursively in pygame?](https://stackoverflow.com/questions/59455641/is-there-anyway-to-do-this-recursively-in-pygame/59456232#59456232)  
![scene](https://i.stack.imgur.com/fyYSY.png)

[Trying to code the Recaman Sequence, but issue with the parameters I pass for drawing an arc](https://stackoverflow.com/questions/54384422/trying-to-code-the-recaman-sequence-but-issue-with-the-parameters-i-pass-for-dr/54386695#54386695)  

[Pygame low frame rate on simple game](https://stackoverflow.com/questions/55073598/pygame-low-frame-rate-on-simple-game/55076222#55076222)  
![scene](https://i.stack.imgur.com/hseTx.gif)

[Trying to delete two objects when placed next to eachother in pygame](https://stackoverflow.com/questions/56101697/trying-to-delete-two-objects-when-placed-next-to-eachother-in-pygame/56102178#56102178)

[Need help creating buttons in pygame](https://stackoverflow.com/questions/57672389/need-help-creating-buttons-in-pygame/57678017#57678017)  
![scene](https://i.stack.imgur.com/BfXkE.gif)

[Python : What is the better way to make multiple loops in pygame?](https://stackoverflow.com/questions/57908287/python-what-is-the-better-way-to-make-multiple-loops-in-pygame)  

[How can I create a window where my program draws a dot ( which is point.png here ) wherever I click on the screen?](https://stackoverflow.com/questions/59002061/how-can-i-create-a-window-where-my-program-draws-a-dot-which-is-point-png-here/59002137#59002137)  
![scene](https://i.stack.imgur.com/XthPF.gif)

[Python3: Count images number and compared the similarity](https://stackoverflow.com/questions/59183941/python3-count-images-number-and-compared-the-similarity/59184495#59184495)  
![scene](https://i.stack.imgur.com/WEdJR.gif)

[How to code a rectangles that start from right in circular motion in pygame](https://stackoverflow.com/questions/59180556/how-to-code-a-rectangles-that-start-from-right-in-circular-motion-in-pygame/59217711#59217711)  
![scene](https://i.stack.imgur.com/Jskrw.png)

[How do I make my monster move randomly in my game](https://stackoverflow.com/questions/59327552/how-do-i-make-my-monster-move-randomly-in-my-game/59329312#59329312)  
![scene](https://i.stack.imgur.com/J7bIM.gif)

[Pygame problem: how to execute conditional on collision?](https://stackoverflow.com/questions/59522285/pygame-problem-how-to-execute-conditional-on-collision/59522405#59522405)  
![scene](https://i.stack.imgur.com/iTIE0.gif)

[How do i correctly update the position and velocity of 100 class objects individually drawing with pygame?](https://stackoverflow.com/questions/59868994/how-do-i-correctly-update-the-position-and-velocity-of-100-class-objects-individ/59869091#59869091)  
![scene](https://i.stack.imgur.com/dgCq1.gif)

[Colour Changing Bouncing Ball](https://stackoverflow.com/questions/60312365/colour-changing-bouncing-ball/60315375#60315375)
![scene](https://i.stack.imgur.com/Bz0cu.gif)

[Is it possible to implement gradual movement of an object to given coordinates in Pygame?](https://stackoverflow.com/questions/60356812/is-it-possible-to-implement-gradual-movement-of-an-object-to-given-coordinates-i/60356995#60356995)  
![scne](https://i.stack.imgur.com/rScfu.gif)

[Using a matrix as a sprite and testing if two sprites overlap](https://stackoverflow.com/questions/60387917/using-a-matrix-as-a-sprite-and-testing-if-two-sprites-overlap/60391694#60391694)  
![scene](https://i.stack.imgur.com/brlQk.gif)

[Is it possible to update a pygame drawing attribute when a event occurs?](https://stackoverflow.com/questions/61551790/is-it-possible-to-update-a-pygame-drawing-attribute-when-a-event-occurs/61555479#61555479)
![scene](https://i.stack.imgur.com/rchSC.gif)

[How can I blit an image on the screen where i click after pressing a button](https://stackoverflow.com/questions/61556099/how-can-i-blit-an-image-on-the-screen-where-i-click-after-pressing-a-button/61556461#61556461)

[How to find the button on the entered position by user and change it's color in pygame?](https://stackoverflow.com/questions/61767256/how-to-find-the-button-on-the-entered-position-by-user-and-change-its-color-in/61767309#61767309)  
![scene](https://i.stack.imgur.com/sqIcy.gif)
![scene](https://i.stack.imgur.com/KMpLP.gif)

[Why it doesn't spin in a circle? And how to fix it?](https://stackoverflow.com/questions/62883103/why-it-doesnt-spin-in-a-circle-and-how-to-fix-it/62883770#62883770)  
![scene](https://i.stack.imgur.com/UD6Wt.gif)

[pygame.mouse.get_pressed() not responding](https://stackoverflow.com/questions/63197182/pygame-mouse-get-pressed-not-responding/63197269#63197269)  
![scene](https://i.stack.imgur.com/zL9WO.gif)

[Pygame Enemys Wont Move Down - Tower Defense Game](https://stackoverflow.com/questions/63734280/pygame-enemys-wont-move-down-tower-defense-game)

[How to shade all the cells that will be useless when you click on them?](https://stackoverflow.com/questions/64625472/how-to-shade-all-the-cells-that-will-be-useless-when-you-click-on-them)  
![scene](https://i.stack.imgur.com/qwMND.png)

[How can I make my recursive function go back to continue recursing other cells](https://stackoverflow.com/questions/64721771/how-can-i-make-my-recursive-function-go-back-to-continue-recursing-other-cells/64722209#64722209)  
![scene](https://i.stack.imgur.com/L32ZZ.png)

[Pygame Tic Tak Toe Logic? How Would I Do It](https://stackoverflow.com/questions/64825967/pygame-tic-tak-toe-logic-how-would-i-do-it/64934964#64934964)  
![Pygame Tic Tak Toe Logic? How Would I Do It](https://i.stack.imgur.com/p7mfM.gif)

[How do I add a rubber band for mouse dragging in PyGame?](https://stackoverflow.com/questions/64880962/how-do-i-add-a-rubber-band-for-mouse-dragging-in-pygame/64881500#64881500)  
![How do I add a rubber band for mouse dragging in PyGame?](https://i.stack.imgur.com/f3aOb.gif)

