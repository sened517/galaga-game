import pgzrun
import random

WIDTH=400
HEIGHT=700

ship=Actor("ship")
ship.x=WIDTH//2
ship.y=HEIGHT-100
ship.dead=False


bullets=[]
enemies=[]
score=0
direction=1

# Initialize enemies

for x in range(8):
 for y in range(4):
     enemies.append(Actor("bug"))
     enemies[-1].x=100+40*x
     enemies[-1].y=0+20*y




#Draw the score
def drawScore():
    screen.draw.text(str(score),(50,50),color="blue")


def on_key_down(key):
   if ship.dead==False:
      if key==keys.SPACE:
         bullets.append(Actor("bullet"))
         bullets[-1].x=ship.x
         bullets[-1].y=ship.y-40



def draw():
    screen.fill("light green")
    drawScore()
    for bullet in bullets:
        bullet.draw()
    for enemie in enemies:
       enemie.draw()
    if ship.dead==True:
       ship.draw()


def update():
    global score,direction

    # Move the ship
    if ship.dead==False:
       if keyboard.left:
          ship.x-=2
       elif keyboard.right:
          ship.x+=2

    # update bullet postions and remove bullets off screen
    for bullet in bullets:
       if bullet.y<-20:
          bullets.remove(bullet)
       else:
          bullet.y-=10

    # move enemies and handle direction change
            

          
    moveDown=False




















pgzrun.go()