from tkinter import *
import random

yvol = -20
menu = 5
score = 0
speed = -5
length = 0
gamemode = 1
flip = False
pause = False

class scene:
    def __init__(self, canvas):
        self.canvas = canvas
        self.bg = self.canvas.create_rectangle(0, 0, 999, 999, fill='Light Blue')
        self.dirt = self.canvas.create_rectangle(0, 490, 999, 999, fill='Light Green')

        self.sender = self.canvas.create_rectangle(-100, 0, -50, 999, fill='Red')
        self.score = self.canvas.create_text(10, 15, fill="black", text='Score: 0', anchor="w", justify='left')
        self.gm = self.canvas.create_text(10, 32, fill="black", text='Mode: Classic', anchor="w", justify='left')

        self.diebg = self.canvas.create_rectangle(250, 150, 550, 350, fill='Light Gray', tags="death")
        self.dietitle = self.canvas.create_text(400, 180, fill="black", text='Get rekt lozer', font=('Arial', 25), tags="death")
        self.diescore = self.canvas.create_text(400, 205, fill="black", text='Score: 0', tags="death")
        #self.diehiscore = self.canvas.create_text(400, 250, fill="black", text='Hi-Score: 0', tags="death")
        self.medal = self.canvas.create_oval(355, 220, 445, 310, fill='Gray', tags="death")
        self.medalrank = self.canvas.create_text(400, 265, fill="white", text='#1', font=('Arial', 37), tags="death")
        self.dierestart = self.canvas.create_rectangle(265, 320, 395, 340, fill='Light Green', tags="death", activefill='Pale Green')
        self.dierestarttxt = self.canvas.create_text(330, 330, fill="black", text='Restart', tags="death")
        self.diemenu = self.canvas.create_rectangle(405, 320, 535, 340, fill='White', tags="death", activefill='gray90')
        self.diemenutxt = self.canvas.create_text(470, 330, fill="black", text='Main Menu', tags="death")

        self.canvas.tag_bind(self.dierestart, "<ButtonPress-1>", self.restartgame)
        self.canvas.tag_bind(self.diemenu, "<ButtonPress-1>", menu)
        self.aliv()

        
        self.menubg = self.canvas.create_rectangle(250, 150, 550, 350, fill='Light Gray', tags="menu")
        self.menutitle = self.canvas.create_text(400, 180, fill="black", text='Flappy Burd v1.0', font=('Arial', 25), tags="menu")
        self.menutip = self.canvas.create_text(400, 205, fill="black", text='Select a gamemode to start playing', tags="menu")

        self.classic = self.canvas.create_rectangle(265, 220, 395, 240, fill='White', tags="menu", activefill='gray90')
        self.classictxt = self.canvas.create_text(330, 230, fill="black", text='Classic', tags="menu")
        self.speed = self.canvas.create_rectangle(405, 220, 535, 240, fill='White', tags="menu", activefill='gray90')
        self.speedtxt = self.canvas.create_text(470, 230, fill="black", text='Score = Speed', tags="menu")
        self.tight = self.canvas.create_rectangle(265, 250, 395, 270, fill='White', tags="menu", activefill='gray90')
        self.tighttxt = self.canvas.create_text(330, 260, fill="black", text='Tight Pipes', tags="menu")
        self.moon = self.canvas.create_rectangle(405, 250, 535, 270, fill='White', tags="menu", activefill='gray90')
        self.moontxt = self.canvas.create_text(470, 260, fill="black", text='Moon Gravity', tags="menu")
        self.flip = self.canvas.create_rectangle(265, 280, 395, 300, fill='White', tags="menu", activefill='gray90')
        self.fliptxt = self.canvas.create_text(330, 290, fill="black", text='Gravity Flip', tags="menu")
        self.thicc = self.canvas.create_rectangle(405, 280, 535, 300, fill='White', tags="menu", activefill='gray90')
        self.thicctxt = self.canvas.create_text(470, 290, fill="black", text='Sticc Burd', tags="menu")
        self.bounce = self.canvas.create_rectangle(265, 310, 395, 330, fill='White', tags="menu", activefill='gray90')
        self.bouncetxt = self.canvas.create_text(330, 320, fill="black", text='Obese Burd', tags="menu")
        self.random = self.canvas.create_rectangle(405, 310, 535, 330, fill='Light Cyan', tags="menu", activefill='Light Blue')
        self.randomtxt = self.canvas.create_text(470, 320, fill="black", text='Random Gamemode', tags="menu")

        self.canvas.tag_bind(self.classic, "<ButtonPress-1>", lambda event: match(1, self))
        self.canvas.tag_bind(self.speed, "<ButtonPress-1>", lambda event: match(2, self))
        self.canvas.tag_bind(self.tight, "<ButtonPress-1>", lambda event: match(3, self))
        self.canvas.tag_bind(self.moon, "<ButtonPress-1>", lambda event: match(4, self))
        self.canvas.tag_bind(self.flip, "<ButtonPress-1>", lambda event: match(5, self))
        self.canvas.tag_bind(self.thicc, "<ButtonPress-1>", lambda event: match(6, self))
        self.canvas.tag_bind(self.bounce, "<ButtonPress-1>", lambda event: match(8, self))
        self.canvas.tag_bind(self.random, "<ButtonPress-1>", lambda event: match("r", self))

    def aliv(self):
        self.canvas.tag_lower("death")

    def kil(self):
        self.canvas.tag_raise("death")

    def menukil(self):
        self.canvas.tag_lower("menu")

    def menualiv(self):
        self.canvas.tag_raise("menu")

    def restartgame(self, event):
        global menu
        menu = 2
        reset()
        self.menukil()

class bird:
    def __init__(self, canvas):
        self.canvas = canvas

        #bird v1
#        self.body = self.canvas.create_rectangle(40, 425, 70, 500, fill='Yellow')
#        self.mouth = self.canvas.create_rectangle(50, 440, 80, 450, fill='Orange')

        #bird v2
        self.body = self.canvas.create_oval(30, 405, 75, 450, fill='Yellow', tags="bird")
        self.eye = self.canvas.create_oval(60, 405, 75, 420, fill='White', tags="bird")
        self.pupil = self.canvas.create_oval(67, 410, 70, 413, fill='Black', tags="bird")
        self.mouth = self.canvas.create_polygon(65, 440, 65, 425, 90, 430, fill='Orange', outline='Black', tags="bird")

    def move(self, vol):
        c.move('bird', 0, vol)
    
class pipe1:
    def __init__(self, canvas):
        self.canvas = canvas
        self.pipe1 = self.canvas.create_rectangle(700, 300, 750, 490, fill='Green')
        self.pipe2 = self.canvas.create_rectangle(700, 100, 750, 0, fill='Green')

def checkcollision():
    global c, gamemode, yvol, bird
    coords1 = c.coords(scene.dirt)
    overlapping = c.find_overlapping(*coords1)
    if bird.body in overlapping:
        if gamemode == 7:
            yvol = 0 - yvol
            bird.move(-10)
        else:
            die()
    
    coords1 = c.coords(pipe1.pipe1)
    overlapping = c.find_overlapping(*coords1)
    if bird.body in overlapping:
        die()
    coords1 = c.coords(pipe1.pipe2)
    overlapping = c.find_overlapping(*coords1)
    if bird.body in overlapping:
        die()

def match(gm, get):
    global gamemode, scene
    if gm == "r":
        rng = random.randint(1, 8)
        if rng == 7:
            rng = 8
        gamemode = rng
    else:
        gamemode = gm

    if gamemode == 1:
        c.itemconfig(scene.gm, text="Mode: Classic")
    elif gamemode == 2:
        c.itemconfig(scene.gm, text="Mode: Score = Speed")
    elif gamemode == 3:
        c.itemconfig(scene.gm, text="Mode: Tight Pipes")
    elif gamemode == 4:
        c.itemconfig(scene.gm, text="Mode: Moon Gravity")
    elif gamemode == 5:
        c.itemconfig(scene.gm, text="Mode: Gravity Flip")
    elif gamemode == 6:
        c.itemconfig(scene.gm, text="Mode: Sticc Burd")
    elif gamemode == 8:
        c.itemconfig(scene.gm, text="Mode: Obese Burd")
    
    get.restartgame(False)

def keybind(event):
    global yvol, gamemode, flip, pause
    if event.keysym == 'space':
        if gamemode == 7:
            yvol = -7
        elif gamemode == 5:
            flip = not flip
            yvol = 0
        else:
            yvol = -15
    elif event.keysym == 'Escape':
        pause = not pause

def upd():
    global yvol, bird, scene, gamemode, flip
    scene.canvas.tag_raise(scene.score)
    scene.aliv()
    if gamemode == 4:
        yvol = yvol + 0.6
    elif gamemode == 5:
        if flip == True:
            yvol = yvol - 0.6
        else:
            yvol = yvol + 0.6
    elif gamemode == 8:
        yvol = yvol + 3
    else:
        yvol = yvol + 1
    bird.move(yvol)
    movepipe()
    checkcollision()

def movepipe():
    global gamemode, c, scene, pipe1, score, speed, length
    if gamemode == 5:
        speed = speed - 0.01
    c.move(pipe1.pipe1, speed, 0)
    c.move(pipe1.pipe2, speed, 0)
    coords1 = c.coords(pipe1.pipe1)
    overlapping = c.find_overlapping(*coords1)
    if scene.sender in overlapping:
        score = score + 1
        if gamemode == 1:
            speed = -8
            length = 0
        elif gamemode == 2:
            speed = speed - 0.5
            length = 0
        elif gamemode == 3:
            length = -70
            speed = -10
        elif gamemode == 4:
            length = 20
        elif gamemode == 6:
            length = 30
            speed = -7
        
        c.itemconfig(scene.score, text="Score: " + str(score))
        c.itemconfig(scene.diescore, text="Score: " + str(score))

        if score >= 100:
            c.itemconfig(scene.medal, fill="Black", outline='White')
            c.itemconfig(scene.medalrank, text="#00")
        elif score > 40:
            c.itemconfig(scene.medal, fill="#f7fbff", outline='Black')
            c.itemconfig(scene.medalrank, text="#0")
        elif score > 30:
            c.itemconfig(scene.medal, fill="Gold", outline='Black')
            c.itemconfig(scene.medalrank, text="#1")
        elif score > 20:
            c.itemconfig(scene.medal, fill="#cad9e3", outline='Black')
            c.itemconfig(scene.medalrank, text="#2")
        elif score > 10:
            c.itemconfig(scene.medal, fill="Sienna4", outline='Black')
            c.itemconfig(scene.medalrank, text="#3")
        else:
            c.itemconfig(scene.medal, fill="Grey", outline='Black')
            c.itemconfig(scene.medalrank, text="")

        size = random.randint(10, 200)
        c.coords(pipe1.pipe1, 900, 0, 950, (size-length))
        c.coords(pipe1.pipe2, 900, (size+200), 950, 490)
        #c.move(pipe1.pipe1, 900, 0)
        #c.move(pipe1.pipe2, 900, 0)

def resizerectangle(canvas, rect_id, new_width, new_height):
    x0, y0, x1, y1 = canvas.coords(rect_id)
    canvas.coords(rect_id, x0, y0, x0 + new_width, y0 + new_height)

def die():
    global menu
    menu = 3

def menu(*args):
    global scene, menu
    menu = 5

def reset():
    global menu, scene, yvol, score, speed, pause
    c.itemconfig(scene.score, text="Score: 0")
    c.itemconfig(scene.medal, fill="Dark Gray", outline='Black')
    yvol = -20
    menu = 2
    score = 0
    speed = -5
    length = 0
    pause = False
    if gamemode == 6:
        c.coords(bird.body, 60, 405, 75, 550)
        c.coords(bird.eye, 60, 405, 75, 420)
        c.coords(bird.pupil, 67, 410, 70, 413)
        c.coords(bird.mouth, 65, 440, 65, 425, 90, 430)
        bird.move(-50)
    else:
        c.coords(bird.body, 30, 405, 75, 450)
        c.coords(bird.eye, 60, 405, 75, 420)
        c.coords(bird.pupil, 67, 410, 70, 413)
        c.coords(bird.mouth, 65, 440, 65, 425, 90, 430)

    c.coords(pipe1.pipe1, 700, 300, 750, 490)
    c.coords(pipe1.pipe2, 700, 100, 750, 0)
    c.itemconfig(scene.medal, fill="Grey")
    c.itemconfig(scene.medalrank, text="")

def rootloop():
    global yvol, menu, c, scene, pause
    if menu == 1:
        scene.menukil()
        reset()
    elif menu == 2:
        if pause == False:
            upd()
    elif menu == 3:
        scene.kil()
    elif menu == 5:
        scene.menualiv()
        scene.aliv()
    
    tk.after(20, rootloop)


tk = Tk()
tk.title('Flappy Bird')
c = Canvas(tk, height=500, width=800)
tk.resizable(False, False)
c.pack()


tk.bind("<KeyPress>", keybind)

scene = scene(c)
pipe1 = pipe1(c)
bird = bird(c)

rootloop()
tk.mainloop()
