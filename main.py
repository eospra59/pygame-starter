import pygame # import library
import random
pygame.init()

# Create the window
win = pygame.display.set_mode((800, 600))
#img = pygame.image.load("assets/hero/sliced/Untitled.png").convert()
font = pygame.font.SysFont("arial", 72)
font2 = pygame.font.SysFont("arial", 50)
font3 = pygame.font.SysFont("arial", 28)
img2 = pygame.image.load('forest-assets/silver_coin.gif').convert()
img3 = pygame.image.load('forest-assets/copper_coin.gif').convert()
img4 = pygame.image.load('forest-assets/sample3b.png').convert()
spritesheet = pygame.image.load('gfx/character.png').convert()
hearts = pygame.image.load('gfx/objects.png')
text = pygame.image.load('gfx/font.png')
doors = pygame.image.load('gfx/Overworld.png')
# Create the first image
smol_img = pygame.Surface([16, 30]).convert()
smol_img.blit(spritesheet, (0, 0), (0, 0, 16, 30))
heart_img = pygame.Surface([60, 10]).convert()
heart_img.blit(hearts, (0, 0), (0, 50, 60, 10))
door_img = pygame.Surface([62, 50]).convert()
door_img.blit(doors, (0, 0), (65, 495, 62, 80))
text_img = pygame.Surface([240, 70]).convert()
text_img.blit(text, (0, 0), (0, 50, 240, 70))
# Create the text object
text = font.render("Welcome to Raymere", True, (130, 143, 133))
text2 = font2.render("Your adventure shall begin.", True, (130, 143, 133))
text3 = font3.render("Begin Game", True, (84, 92, 86))
#x = 0
#y = 0
#a = 0
#b = 0
#c = 0
run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

# Game code starts here ---------------------
  #win.fill((0, 0, 0))
  win.blit(img4, (0, 0))
  win.blit(img4, (200, 0))
  win.blit(img4, (400, 0))
  win.blit(img4, (600, 0))
  win.blit(img4, (0, 200))
  win.blit(img4, (200, 200))
  win.blit(img4, (400, 200))
  win.blit(img4, (600, 200))
  win.blit(img4, (0, 400))
  win.blit(img4, (200, 400))
  win.blit(img4, (400, 400))
  win.blit(img4, (600, 400))
  win.blit(img2, (380, 520))
  win.blit(img3, (410, 520))
  win.blit(smol_img, (360, 570))
  win.blit(heart_img, (380, 500))
  win.blit(door_img, (380, 550))
  win.blit(text_img, (280, 250))
  win.blit(text, (50, 100))
  win.blit(text2, (100, 180))
  win.blit(text3, (325, 265))
  #x = random.randint(0, 1000)
  #y = random.randint(0, 1000)
  #a = random.randint(0, 255)
  #b = random.randint(0, 255)
  #c = random.randint(0, 255)
  #win.blit(img, (x, y))
  # Draw a rectangle
  #pygame.draw.rect(win, (a, b, c), (x, y, 10, 10))
  #pygame.draw.rect(win, (b, c, a), (y, x, 10, 10))
  #Update the display
  pygame.display.update()

print("Ending game")
pygame.quit()
