import pygame,sys
from pygame.locals import * 
import random 
from time import time 
pygame.init()
size=[1200,600]
screen=pygame.display.set_mode(size)

#小恐龙类
class XKL(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load(r"images\恐龙1.png")
        self.rect=self.image.get_rect()
        self.rect.x=100
        self.rect.y=size[1]-70-76
        self.jump=False
        self.speed=-10
    def show(self):
        screen.blit(self.image,self.rect)
    def Jump(self):
        if self.jump==True:
            self.rect.y+=self.speed
            self.speed+=0.2
            if self.rect.y>=size[1]-70-76:
                self.rect.y=size[1]-70-76
                self.speed=-10
                self.jump=False


# 仙人掌类
class XRZ(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size=random.randint(50,100)/100
        
        self.w=int(69*self.size)
        self.s=5
        self.h=int(177/2*self.size)
        self.image=pygame.image.load(r"images\仙人掌.png")
        self.image=pygame.transform.scale(self.image,[self.w,self.h])
        self.rect=self.image.get_rect()
        self.rect.y=size[1]-70-self.h
        self.rect.x=size[0]

    def show (self):
        screen.blit(self.image,self.rect)
    def move(self):
        self.rect.x=self.rect.x-self.s
        

class Game():
    state="READY"
    xkl=XKL()
    xrzs=pygame.sprite.Group()
    it=3
    It=0
    score=0

def  check():
    for x in Game.xrzs:
        if pygame.sprite.collide_rect(Game.xkl,x):
            Game.state="END"
            music=pygame.mixer.Sound(r"sounds\失败音效.wav")
            music.play()

        if x.rect.x<0:
            Game.score+=int(x.size*3)
            x.kill()

def addxrz():
    now=time()
    if now-Game.It>Game.it:
        Game.xrzs.add(XRZ())
        Game.It=now
        Game.it=random.randint(100,200)/100

def writetext(size,text,color,pos):
    font=pygame.font.Font(r"fonts\字体1.TTF",size)
    render=font.render(text,True,color)
    screen.blit(render,pos)

def bg():
    screen.fill("white")
    pygame.draw.line(screen,"grey",[0,size[1]-70],[size[0],size[1]-70],5)
    Game.xkl.show()
    Game.xkl.Jump()
    writetext(50,"分数:%d"%Game.score,"orange",[0,0])

while True:
    bg()
    if Game.state=="RUNNING":
        addxrz()
        check()
        for x in Game.xrzs:
            x.move()
            x.show()
    elif Game.state=="END":
        writetext(100,"Game over","black",[size[0]//2-250,size[1]-400])
        if Game.xkl.rect.y<size[1]:
            Game.xkl.rect.y=Game.xkl.rect.y+Game.xkl.speed
            Game.xkl.speed+=1
        
    writetext(150,"按空格开始游戏","black",[50,50])
    for event in pygame.event.get():
        if event.type==QUIT or event.type==KEYDOWN and event.key==K_ESCAPE:
            sys.exit()

        

        if event.type==KEYDOWN and event.key==K_SPACE:
            sound=pygame.mixer.Sound(r"sounds\跳跃音效.wav")
            sound.play()
            if Game.state=="READY":
                Game.state="RUNNING"
                Game.xkl.jump=True
            elif Game.state=="RUNNING":
                Game.xkl.jump=True
    pygame.time.delay(5)
    pygame.display.update()