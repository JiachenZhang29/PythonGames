import random
from turtle import *

speed(0)
hideturtle()
bgcolor("black")
colors=["red","yellow","blue","green","orange","purple","white","gray"]
def draw_kaleido(x,y):
    pencolor(random.choice(colors))
    size=random.randint(10,40)
    draw_spiral(x,y,size)
    draw_spiral(-x,y,size)
    draw_spiral(-x,-y,size)
    draw_spiral(x,-y,size)
def draw_spiral(x,y,size):
    penup()
    setpos(x,y)
    pendown()
    for m in range(size):
        fd(m*2)
        left(92)
onscreenclick(draw_kaleido)
done()


from turtle import *
speed(0)
onscreenclick(setpos)
done()
'''
import pygame
pygame.init()
screen=pygame.display.set_mode([800,600])
pygame.display.set_caption("Smile Pong")
keepGoing=True
pic=pygame.image.load("CrazySmile.jpg")
colorkey=pic.get_at((0,0))
pic.set_colorkey(colorkey)
picx=0
picy=0
BLACK=(0,0,0)
WHITE=(255,255,255)
timer=pygame.time.Clock()
speedx=5
speedy=5
paddlew=200
paddleh=25
paddlex=300
paddley=550
picw=100
pich=100
points=0
lives=5
font=pygame.font.SysFont("Time",24)
while keepgoing:
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT:
            keepGoing=False
    picx+=speedx
    picy+=speedy
    if picx<=0 or picx+pic.get_width()>=800:
        speedx = -speedx
    if picy<=0:
        speedy = -speedy
    if picy>=500:
        lives-=1
        speedy = -speedy
    screen.fill(BLACK)
    screen.bilt(pic,(picx,picy))
    
    paddlex=pygame.mouse.get_pos()[0]
    paddlex-=paddlew/2
    pygame.draw.rect(screen,WHITE,(paddlex,paddley,paddlew,paddleh))

    if picy+pich>=paddley and picy+pich<=paddley+paddleh and speedy>0:
        if picx+picw/2>=paddlex and picx+picw/2<=paddlex+paddlew:
            points+=1
            speedy = -speedy
    draw_string="Lives:"+str(lives)+"Points:"+str(points)
    
    text=font.render(draw_string,True,WHITE)
    text_rect=text.get_rect()
    text_rect.centerx=screen.get_rect().centerx
    text_rect.y=10
    screen.blit(text,text_rect)
    pygame.display.undate()
    timer.tick(60)
pygame.quit()

'''












