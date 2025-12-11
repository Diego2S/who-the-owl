import pgzrun
import random 

# game screen
WIDTH = 800
HEIGHT = 600
WHITE = 255,255,255

# estados do jogo
game_state = "menu"   # menu -> playing -> gameover
music_on = True

def get_random_x():
    return random.randint(20, 780)

# background
bg = Actor("background_800x600")
bg_menu = Actor("menu_background_800x600")

# who
who = Actor("who2") 
who.x = 400
who.y = 550

candy = Actor("candy2")
candy.x = get_random_x()
candy.y = 0

ant = Actor("ant2")
ant.x = get_random_x()
ant.y = 0

bomb = Actor("bomb2")
bomb.x = get_random_x()
bomb.y = 0

# Variáveis
score = 0
lives = 3
dead = False

# -------------------------
# MOVER COM MOUSE
# -------------------------
def on_mouse_move(pos):
    if game_state == "playing":
        who.x = pos[0]

# -------------------------
# CLIQUES DO MOUSE
# -------------------------
def on_mouse_down(pos):
    global game_state, music_on

    # ------ MENU ------
    if game_state == "menu":

        x, y = pos

        # BOTÃO 1: PLAY NORMAL
        if 50 < x < 350 and 90 < y < 140:
            music_on = True
            music.play("background.wav")
            reset_game()
            game_state = "playing"
            return

        # BOTÃO 2: PLAY SEM MÚSICA
        if 50 < x < 550 and 150 < y < 200:
            music_on = False
            music.stop()
            reset_game()
            game_state = "playing"
            return

    # ------ GAME OVER ------
    if game_state == "gameover":
        game_state = "menu"
        return


# -------------------------
# DESENHAR TELA
# -------------------------
def draw():
    screen.clear()

    # ------ MENU ------
    if game_state == "menu":
        bg_menu.draw()

        screen.draw.text("Who, The Owl", (10, 10),
                         fontsize=60, color=WHITE, fontname="publicpixel")

        screen.draw.text("Jogar Game", (50, 90),
                         fontsize=40, color=WHITE, fontname="publicpixel")

        screen.draw.text("Jogar Game Sem Musica", (50, 150),
                         fontsize=35, color=WHITE, fontname="publicpixel")
        return

    # ------ GAMEPLAY ------
    if game_state == "playing":
        bg.draw()
        who.draw()
        candy.draw()
        bomb.draw()
        ant.draw()
        screen.draw.text(f"Score: {score}", (15,10), color=WHITE, fontsize=15, fontname="publicpixel")
        screen.draw.text(f"Lives: {lives}", (650,10), color=WHITE, fontsize=15, fontname="publicpixel")
        return

    # ------ GAME OVER ------
    if game_state == "gameover":
        bg.draw()
        screen.draw.text("GAME OVER", (10, 10),
                         fontsize=60, color=WHITE, fontname="publicpixel")

        screen.draw.text(f"Score: {score}", (50,90), color=WHITE, fontsize=15, fontname="publicpixel")

        screen.draw.text("Retornar ao menu", (50, 150),
                         fontsize=35, color=WHITE, fontname="publicpixel")
        return


# -------------------------
# ATUALIZAÇÃO DO JOGO
# -------------------------
def update():
    global score, lives, game_state

    if game_state != "playing":
        return

    # candy
    if score <= 0:
        score = 0
        
    candy.y += 4 + score / 4
    if candy.y > 600:
        candy.x = get_random_x()
        candy.y = 0

    if candy.colliderect(who):
        sounds.colliderect.play()
        candy.x = get_random_x()
        candy.y = 0
        score += 1

    # ant
    ant.y += 4 + score/4
    if ant.y > 600:
        ant.x = get_random_x()
        ant.y = 0

    if ant.colliderect(who):
        sounds.lose.play()
        ant.x = get_random_x()
        ant.y = 0
        score -= 1

    # bomb
    bomb.y += 4 + score/4
    if bomb.y > 600:
        bomb.x = get_random_x()
        bomb.y = 0

    if bomb.colliderect(who):
        sounds.explosao.play()
        bomb.x = get_random_x()
        bomb.y = 0
        score -= 5
        lives -= 1

    # GAME OVER
    if lives <= 0:
        if score <= 0:
            score = 0
            
        sounds.gameover.play()
        game_state = "gameover"


# -------------------------
# RESET DO JOGO
# -------------------------
def reset_game():
    global score, lives
    score = 0
    lives = 3
    candy.x = get_random_x(); candy.y = 0
    ant.x = get_random_x(); ant.y = 0
    bomb.x = get_random_x(); bomb.y = 0
    who.x = 400


# -------------------------
# MÚSICA PADRÃO: ligada ao iniciar
# -------------------------
music.play("background.wav")

pgzrun.go()
