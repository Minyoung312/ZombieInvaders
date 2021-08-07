import pygame
import random
import math

pygame.init()
screen_dimensions = 1000, 629
display = pygame.display.set_mode((screen_dimensions))

Background =  pygame.image.load("composition-with-tombstones-hill.jpg")


# Title and Game Logo
Zombie_icon = "icons8-zombie-100.png"
pygame.display.set_caption("Zombie Invaders!!")
icon = pygame.image.load(Zombie_icon)
pygame.display.set_icon(icon)

# Cop
cop_image = "icons8-fat-cop-48.png"
character_image = pygame.image.load(cop_image)
playerX = 0
playerY = 350
playerY_movements = 0
playerX_movements = 0

#Zombie

zombie_image = []
zombieY = []
zombieX = []
zombieY_movements = []
zombieX_movements = []
zombie_number = 10

for i in range(zombie_number):
   zombie_image.insert(0,pygame.image.load("icons8-zombie-48.png"))
   zombieY.insert(0,random.randint(0, 615))
   zombieX.insert(0,random.randint(952, 952))
   zombieY_movements.insert(0,1)
   zombieX_movements.insert(0,-150)



# Axe

axe_image = pygame.image.load("icons8-small-axe-48.png")
axeX = 0
axeY = 350
axeX_movements = 4

axe_state = "Ready"

axe_state = "Out"

# Score
players_score = 0
font = pygame.font.Font("freesansbold.ttf", 24)

fontX = 5
fontY = 5

# game over
game_over_font = pygame.font.Font("freesansbold.ttf", 64)


def score(x,y):
   score = font.render("Your Score:" + str(players_score), True, (255, 0, 0))
   display.blit(score, (x, y))

def game_over(x,y):
   over = game_over_font.render("Game Over", True, (255, 0, 0))
   display.blit(over, (x, y))

def player(x,y):
   display.blit(character_image, (x,y))

def zombie(x,y,i):
   display.blit(zombie_image[i], (x,y))

def throw_axe(x,y):
   global axe_state
   axe_state = "Axe thrown"
   display.blit(axe_image, (x,y))

def Hit(zombieX, zombieY, axeX, axeY):
   distance = math.sqrt((math.pow(zombieX - axeX, 2))+ (math.pow(zombieY-axeY, 2)))
   if distance<27:
       return True
   else:
       return False



# Main loop
action = True

while action:
   display.fill((0, 128, 0))
   display.blit(Background, (0,0))

   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           action = False
       if event.type == pygame.KEYDOWN:

           if event.key == pygame.K_UP:
               playerY_movements = -0.7

           if event.key == pygame.K_DOWN:
               playerY_movements = 0.7
           if event.key == pygame.K_LEFT:
               playerX_movements = -0.7
           if event.key == pygame.K_RIGHT:
               playerX_movements = 0.7
           if event.key == pygame.K_SPACE:
               if axe_state == "Ready":
                   axeY = playerY
                   throw_axe(playerX, playerY)
               if axe_state == "Out":
                   throw_axe(0,0)






       if event.type == pygame.KEYUP:
           if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
               playerY_movements = 0
               playerX_movements = 0






   # Cop Movements
   playerY += playerY_movements
   if playerY <= 0:
       playerY = 0
   elif playerY >= 629:
       playerY = 581
   playerX += playerX_movements
   if playerX <= 0:
       playerX = 0
   elif playerX >= 1000:
       playerX = 952 #900-48

   # Zombie Movements
   for i in range(zombie_number):
       if zombieX[i] < 10:
           
               game_over(300,300)
               axe_state = "Out"
               break






       zombieY[i] += zombieY_movements[i]
       if zombieY[i] <= 0:
           zombieY_movements[i] = 0.6
           zombieX[i] += zombieX_movements[i]
       elif zombieY[i] >= 629:
           zombieY_movements[i] = -0.6  
           zombieX[i] += zombieX_movements[i]


       # When Zombies are hit

       zombie_hit = Hit(zombieX[i], zombieY[i], axeX, axeY)
       if zombie_hit:
           axeX = 0
           axe_state = "Ready"
           players_score = players_score + 1

           zombieY[i] = random.randint(0, 615)
           zombieX[i] = random.randint(952, 952)
       zombie(zombieX[i], zombieY[i], i)



   if axeX == 1000:
       axeX = 0
       axe_state = "Ready"

   if axe_state == "Axe thrown":
       throw_axe(axeX, axeY)
       axeX += axeX_movements



   player(playerX,playerY)
   score(fontX, fontY)
   pygame.display.update()
   game_over(500,314.5)
