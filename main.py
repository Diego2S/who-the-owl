import pgzrun
import random 

# game screen

WIDTH = 800
HEIGHT = 600

# background

bg = Actor("background_800x600") # type: ignore


# who

who = Actor("who2") 
who.x = 400
who.y = 550

candy = Actor("candy2")
candy.x = random.randint(20,780)
candy.y = 0


ant = Actor("ant2")
ant.x = random.randint(20,780)
ant.y = 0

bomb = Actor("bomb2")
bomb.x = random.randint(20,780)
bomb.y = 0

def draw():
    bg.draw()
    who.draw()
    candy.draw()
    bomb.draw()
    ant.draw()

def update():
    # mover owl
    if keyboard.left:
        who.x -= 5
    if keyboard.right:
        who.x += 5

    if who.x < 60:
        who.x = 60
    if who.x > 740:
        who.x = 740

pgzrun.go()