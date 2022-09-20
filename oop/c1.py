class Cat:
    breed = None
    gender = None
    fur_color = None
    age = None
    hieght = None
    weight = None
    is_tamed = None
    
    def eat(self, food = 'catfood'):
        print(f'🐈 is eating{food}')
        
    def play(self):
        print('🐈 is playing')
        
    def sleep(self):
         print('🐈 is sleeping')
            
billu = Cat() # constructor calling
tom = Cat()
bagadbilla = Cat()

billu.breed = 'persian'
billu.weight = '1.5'
billu.age = '100'
billu.fur_color = 'white'
billu.height = 1
billu.is_tamed = True
billu.gender = 'M'
        
tom.breed = 'street cat'
tom.weight = '1.5'
tom.age = '3'
tom.fur_color = 'grey'
tom.height = 1.1
tom.is_tamed = True
tom.gender = 'M'
        
        
bagadbilla.breed = 'billa'
bagadbilla.weight = '1.7'
bagadbilla.age = '6'
bagadbilla.fur_color = 'black'
bagadbilla.height = 1
bagadbilla.is_tamed = True
bagadbilla.gender = 'M'

print('billu details')
print('gender:', billu.gender)
print('age:', billu.age)
print('weight:', billu.weight)
print('height:', billu.height)
print('color:', billu.fur_color)
print('pet:', 'yes' if billu.is_tamed else 'no')
billu.sleep()
billu.play()
billu.eat()

print('tom details')
print('gender:', tom.gender)
print('age:', tom.age)
print('weight:', tom.weight)
print('height:', tom.height)
print('color:', tom.fur_color)
print('pet:', 'yes' if billu.is_tamed else 'no')
tom.sleep()
tom.play()
tom.sleep()

print('billu details')
print('gender:', bagadbilla.gender)
print('age:', bagadbilla.age)
print('weight:', bagadbilla.weight)
print('height:', bagadbilla.height)
print('color:', bagadbilla.fur_color)
print('pet:', 'yes' if billu.is_tamed else 'no')
bagadbilla.sleep()
bagadbilla.eat('mouse')
            
            
                