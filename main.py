import pygame # import library
import random
pygame.init()

# Create the window
win = pygame.display.set_mode((800, 600))
img = pygame.image.load("assets/hero/sliced/Untitled.png").convert()
x = 0
y = 0
a = 0
b = 0
c = 0
run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

# Game code starts here ---------------------
  #win.fill((0, 0, 0))
  x = random.randint(0, 1000)
  y = random.randint(0, 1000)
  a = random.randint(0, 255)
  b = random.randint(0, 255)
  c = random.randint(0, 255)
  win.blit(img, (x, y))
  # Draw a rectangle
  #pygame.draw.rect(win, (a, b, c), (x, y, 10, 10))
  #pygame.draw.rect(win, (b, c, a), (y, x, 10, 10))
  #Update the display
  pygame.display.update()

print("Ending game")
pygame.quit()
