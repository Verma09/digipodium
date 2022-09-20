import pgzrun 

HEIGHT = 300
WIDTH = 500

class Player(Actor):
    speed = 3
    
    def move(self):
        if keyboard.LEFT and self.left > 0:
            self.x += -self.speed
        if keyboard.RIGHT and self.right < WIDTH:
            self.x += self.speed
        print('move', self.x, self.y)
        
        
class Enemy(Actor):
    speed = 2
    
    def chase(self, player):
        if self.x < player.x :
            self.x += self.speed
        if self.x > player.x:
            self.x =+ -self.speed
            
p = Player('ironman', pos=(100,100))
e = Enemy('zombie', pos=(250,250))

def draw():
    screen.clear()
    p.draw()
    e.draw()
    
def update():
    p.move()
    e.chase(p)
    

pgzrun.go()
    