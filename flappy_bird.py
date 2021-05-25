import pygame , sys , random
class Bird(object):
    def __init__(self):
        self.birdRect = pygame.Rect(65,50,50,50) # 鸟的矩形
        self.birdStatus = [pygame.image.load("像素鸟FlappyBird游戏源码-1_爱给网_aigei_com.png"),
                             pygame.image.load("像素鸟FlappyBird游戏源码-2_爱给网_aigei_com.png"),
                             pygame.image.load("像素鸟FlappyBird游戏源码-3_爱给网_aigei_com.png")] #鸟的三种状态
        self.status = 0 #默认飞行位置
        self.birdx = 120 #鸟所在的x轴坐标
        self.birdY = 350 #鸟所在的y轴坐标
        self.jump =False #自动降落 
        self.jumpSpeed = 10 #跳跃高度
        self.gravity = 5 #重力
        self.dead = False #默认小鸟还活着

    def birdUpdate(self):
        if self.jump: #跳跃
            self.jumpSpeed -= 1 #速度递减
            self.birdY -= self.jumpSpeed #y轴减少
        else:
            self.gravity +=0.2 #重力递减
            self.birdY +=self.gravity #y轴增加
        self.birdRect[1] = self.birdY #更改y轴位置

class Pipeline(object):
    def __init__(self):
        self.wallx = 288;
        self.pineUp = pygame.image.load("像素鸟FlappyBird游戏源码-管道上(pipe)_爱给网_aigei_com.png")  #上管道
        self.pineDown = pygame.image.load("像素鸟FlappyBird游戏源码-管道下(pipe)_爱给网_aigei_com.png") #下管道
    def updatePipeline(self):
        self.wallx -= 5
        if self.wallx < -10 :
            global score
            score += 1
            self.wallx = 288

def creatMap():
    screen.fill((255,255,255))# 填充颜色
    screen.blit(background,(0,0)) #填入到背景

    screen.blit(Pipeline.pineUp,(Pipeline.wallx,0)) 
    screen.blit(Pipeline.pineDown,(Pipeline.wallx,412))
    Pipeline.updatePipeline()

    if Bird.dead:
        Bird.status = 2
    elif Bird.jump:
        Bird.status = 1 
    
    screen.blit(Bird.birdStatus[Bird.status],(Bird.birdx,Bird.birdY))
    
    Bird.birdUpdate()
    

    screen.blit(font.render('score ' +str(score),-1,(255,255,255)),(100,50)) #设置颜色及坐标位置
    pygame.display.update() #更新

def checkDead():
    upRect = pygame.Rect(Pipeline.wallx,-300,
                         Pipeline.pineUp.get_width() -10 ,
                         Pipeline.pineUp.get_width())
    
    downRect = pygame.Rect(Pipeline.wallx,500,
                         Pipeline.pineDown.get_width() -10 ,
                         Pipeline.pineDown.get_width())
    if upRect.colliderect(Bird.birdRect) or downRect.colliderect(Bird.birdRect):
        Bird.dead = True
        return True
    else:
        return False

def getResutl():
    pygame.init
    final_text1 = 'GAME OVER'
    final_text2 = "your score is "+ str(score)
    ft1_font = pygame.font.SysFont("Arial",70)
    ft1_surf = font.render(final_text1,1,(242,3,36))
    ft2_font = pygame.font.SysFont("Arial",10)
    ft2_surf = font.render(final_text2,1,(253,177,6))

    screen.blit(ft1_surf,[screen.get_width()/2 - ft1_surf.get_width()/2,100])
    screen.blit(ft2_surf,[screen.get_width()/2 - ft2_surf.get_width()/2,150])
    pygame.display.flip()

if __name__ == '__main__':
    pygame.init()  #初始化pygame
    pygame.font.init()  #初始化字体
    font = pygame.font.SysFont(None,50)  #设置默认字体大小
    size = width , height=288,512  #设置窗口
    screen = pygame.display.set_mode(size) #显示窗口
    clock = pygame.time.Clock() #设置时钟
    Pipeline = Pipeline()  #实例化
    Bird = Bird() #实例化
    score = 1 #初始化分数
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
            if (event.type==pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN)and not Bird.dead:
                Bird.jump = True
                Bird.gravity = 5
                Bird.jumpSpeed = 10

        background = pygame.image.load("像素鸟FlappyBird游戏源码-bg 光(light)_爱给网_aigei_com.png")
        if checkDead():
            getResutl()
        else:
            creatMap()