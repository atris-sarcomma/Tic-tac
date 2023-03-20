import pygame
import time
import easygui
pygame.init()
even=0
fin_x=0
fin_y=0
mid_x=0
mid_y=0
selected=1
tagged=[]
def bg():
    for i in range(0,4):
        for j in range(0,4):
            pygame.draw.rect(ok, (10,10,10), pygame.Rect((i*300),(j*300),300,300),width=2)
x,y = 15,15
img = pygame.image.load(r'Artboard 1.png')
cir = pygame.image.load(r'cir.png')
done = False
color=(254,253,252)
black=(0,0,0)
ok=pygame.display.set_mode((900,900)) 
fm=pygame.time.Clock()
pygame.display.set_caption('YOU fucked up :)')
set=True
blank=False
up=False
cos=False
loc_cross=[]
loc_cirlce=[]
key_name=''
even=0
fin_x=0
fin_y=0
mid_x=0
mid_y=0
set=True
blank=False
up=False
cos=False
loc_cross=[]
loc_cirlce=[]
tagged_cross=[]
tagged_cricle=[]
while not done:
    print(tagged_cricle,'   ',tagged_cross)
    for i in range(1,4):
        if all(i in tagged_cricle for i in (i, i+3, i+6)) or all(i in tagged_cross for j in (1,4,7) for i in (j,j+1,j+2)) or all(i in tagged_cricle for i in (1, 5, 9)) or all(i in tagged_cricle for i in (3, 5, 7)):
            easygui.msgbox('Circle won, congratulations!')
            done = True
            break
        elif all(i in tagged_cross for i in (i, i+3, i+6)) or \
            all(i in tagged_cross for j in (1,4,7) for i in (j,j+1,j+2)) or \
            all(i in tagged_cross for i in (1, 5, 9)) or \
            all(i in tagged_cross for i in (3, 5, 7)):
            easygui.msgbox('Cross won, congratulations!')
            done = True
            break        
    if (len(tagged_cross)+len(tagged_cricle))==9:
        if easygui.ynbox('you wanna continue?', title='you messed up >:('):
            even=0
            fin_x=0
            fin_y=0
            mid_x=0
            mid_y=0
            set=True
            blank=False
            up=False
            cos=False
            loc_cross=[]
            loc_cirlce=[]
            tagged=[]
            tagged=[]
        else:
            done = True
    set=True
    fm.tick(120)
    ok.fill(color)
    bg()
    img.blit(img,(0,0))
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True
        if event.type == (pygame.KEYDOWN):  
        # gets the key name  
            key_name = pygame.key.name(event.key).upper()
        if event.type == (pygame.KEYUP):
            set=False  
    if key_name == 'SPACE': 
        ok.fill(black)
        even=0
        fin_x=0
        fin_y=0
        mid_x=0
        mid_y=0
        set=True
        blank=False
        up=False
        cos=False
        loc_cross=[]
        loc_cirlce=[]
        tagged=[]
    if not set:
        if key_name == 'W' and y > 16:
            y-=300
            selected-=3
            set=True
        elif key_name == 'S' and y < 614:
            y+=300
            selected+=3
            set=True
        elif key_name == 'D' and x < 614 :
            x+=300
            selected+=1
            set=True
        elif key_name == 'A' and x > 16:
            x-=300
            selected-=1
            set=True
    for i in loc_cross:
        if even == 0:
            fin_x = i
        if even == 1:
            fin_y=i
        even+=1
        if even == 2:  
            ok.blit(img,(fin_x,fin_y))
            even=0
    for i in loc_cirlce:
        if even == 0:
            mid_x = i
        if even == 1:
            mid_y=i
        even+=1
        if even == 2:  
            ok.blit(cir,(mid_x,mid_y))
            even=0
    if key_name != 'RETURN':
        pygame.draw.rect(ok,(57, 255, 20),pygame.Rect(x,y,270,270,),width=2)
    else:
        if not cos:
            loc_cross.append(x)
            loc_cross.append(y)
            cos = True
            tagged_cross.append(selected)
        else:
            loc_cirlce.append(x)
            loc_cirlce.append(y)
            cos=False
            tagged_cricle.append(selected)
        key_name=''
    pygame.display.update()
