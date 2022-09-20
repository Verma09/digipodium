import pgzrun
HEIGHT = 500
WIDTH = 600
p = Actor('ironman',pos=(100,100)) # p = actor 

def draw(): # drraw = function
    screen.clear()
    screen.draw.text("welcome to pgzero",(10,10), color= 'red', fontsize=50)
    screen.draw.text('create by Sandhya',(10,460), color = 'white')
    p.draw()
    
    # outside function
pgzrun.go()