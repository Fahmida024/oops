import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))
playing=True
while playing:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            playing=False
    screen.fill('white')
    class Rectangle():
        def __init__(self,color,dimensions):
            self.s=screen
            self.c=color
            self.d=dimensions
        def draw(self):
            pygame.draw.rect(self.s,self.c,self.d)
    rectangle1=Rectangle('blue',(50,20,100,100))
    rectangle2=Rectangle('red',(150,120,100,100))
    rectangle3=Rectangle('black',(250,220,100,100))

    rectangle1.draw()
    rectangle2.draw()
    rectangle3.draw()
    

            
        







    pygame.display.update()
