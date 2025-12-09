import pgzrun
import random 

# game screen

WIDTH = 800
HEIGHT = 600
WHITE = 255,255,255
# 
def R():
    return random.randint(20, 780)

# background

bg = Actor("background_800x600") # type: ignore



# who

who = Actor("who2") 
who.x = 400
who.y = 550

candy = Actor("candy2")
candy.x = R()
candy.y = 0


ant = Actor("ant2")
ant.x = R()
ant.y = 0

bomb = Actor("bomb2")
bomb.x = R()
bomb.y = 0

# Variaves do jogo

score = 0
lives = 3
game_over = False
dead =False


def draw():
    bg.draw()

    if game_over:
        screen.draw.text("Game Over",(230,200),color=(WHITE),fontname="publicpixel",fontsize=30)

    who.draw()
    candy.draw()
    bomb.draw()
    ant.draw()
    screen.draw.text("Score: "+ str(score),(15,10),color=(WHITE),fontname="publicpixel",fontsize=15)
    screen.draw.text("Lives: "+ str(lives),(650,10),color=(WHITE),fontname="publicpixel",fontsize=15)

def update():
    global score,lives ,game_over, dead
    
    
    # mover owl
    if keyboard.left:
        who.x -= 5
    if keyboard.right:
        who.x += 5

    if who.x < 60:
        who.x = 60
    if who.x > 740:
        who.x = 740

    #candy
    candy.y += 4 + score / 4
    
    if candy.y > 600:
        candy.x = R()
        candy.y = 0

    if candy.colliderect(who):
        sounds.colliderect.play()
        candy.x = R()
        candy.y = 0

        score +=1

    # ant
    ant.y += 4 + score /4
    
    if ant.y > 600:
        ant.x = R()
        ant.y = 0

    if ant.colliderect(who):
        sounds.lose.play()
        ant.x = R()
        ant.y = 0
        score -=1
    #BomB

    bomb.y += 4 + score /4
    
    if bomb.y > 600:
        bomb.x = R()
        bomb.y = 0

    if bomb.colliderect(who):
        sounds.explosao.play()
        bomb.x = R()
        bomb.y = 0
        score -=5
        lives -= 1

    if lives == 0:
        game_over = True
        candy.y = 0
        ant.y = 0
        bomb.y = 0
        if dead == False:
            sounds.gameover.play()
        dead =True



pgzrun.go()