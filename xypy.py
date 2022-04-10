import pygame as pg
import sys
from random import randint

from myfuncs import randcol
pg.init()

"""Color constants"""

RED = (255,0,0)
BLACK = (0,0,0)
YELLOW = (255,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
GREY = (220,220,220)


"""X and Y coordinates for drawings. Consider lists of objects for animation rewards"""
xys = []

xys = list([[[0, 0, 1, 1, 2, 2, 1, 1, 2, 2, 3, 3, 5, 5, 3, 3, 6, 6, 4, 4, 5, 5, 7, 7, 0],
    [1, 6, 6, 2, 2, 7, 7, 8, 8, 8, 9, 8, 8, 7, 7, 6, 6, 5, 5, 3, 3, 2, 2, 1, 1]],
    [[7, 7, 9, 9, 7, 7, 6, 6, 2, 2, 1, 1, 3, 3, 5, 5, 7],
     [0, 4, 4, 6, 6, 7, 7, 4, 4, 5, 5, 0, 0, 1, 1, 0, 0]],
    [[1, 1, 2, 3, 4, 4, 2, 3, 4, 6, 6, 10, 10, 9, 9, 8, 7, 6, 6, 5, 5, 4, 3, 2, 2, 1],
     [3, 5, 6, 8, 8, 6, 6, 8, 9, 9, 6, 6, 3, 3, 2, 1, 1, 2, 3, 3, 2, 1, 1, 2, 3, 3]],
    [[7, 4, 2, 5, 5, 5, 7, 7, 5, 2, 2, 7],
     [5, 5, 4, 4, 1, 4, 5, 2, 1, 1, 4, 5]],
    [[5, 1, 10, 5, 5, 1, 2, 9, 10, 5, 5],
     [10, 5, 5, 10, 3, 3, 1, 1, 3, 3, 10]],
    [[2, 1, 2, 3, 6, 7, 8, 9, 10, 9, 10, 9, 8, 7, 6, 3, 2, 1, 2],
     [5, 6, 8, 9, 9, 8, 6, 8, 9, 5, 1, 2, 4, 2, 1, 1, 2, 4, 5]],
    [[5, 4, 2, 4, 5, 6, 8, 6, 5],
     [2, 5, 6, 7, 9, 7, 6, 5, 2]],
    [[2, 7, 7, 4, 2, 7, 7, 4, 2],
     [2, 4, 7, 7, 2, 7, 4, 7, 2]],
    [[3, 4, 1, 4, 6, 7, 10, 7, 8, 6, 3],
     [0, 3, 5, 6, 9, 6, 5, 3, 0, 2, 0]],
    [[5, 3, 3, 5, 7, 7, 5, 5, 6, 7, 7, 5, 7, 7, 6, 5, 4, 3, 3, 5, 3, 3, 4, 5, 5],
     [1, 2, 3, 1, 2, 3, 1, 8, 10, 10, 9, 8, 7, 6, 6, 8, 6, 6, 7, 8, 9, 10, 10, 8, 1]],
    [[2, 1, 2, 3, 4, 3, 3, 4, 5, 6, 6, 7, 6, 6, 7, 8, 8, 7, 2],
     [1, 3, 5, 4, 5, 7, 8, 9, 9, 8, 7, 6, 6, 5, 4, 3, 2, 1, 1]],
    [[5, 4, 2, 1, 2, 5, 8, 9, 8, 6, 5],
     [7, 8, 8, 6, 4, 1, 4, 6, 8, 8, 7]],
    [[1, 6, 9, 1],
     [8, 2, 7, 8]]])

def multadd1(p,q):
    prod = 0
    for i in range(p):
       for j in range(q):
          prod +=1
    return prod
"""Generate the XY Chart on its own surface:ccs. Use ratios."""
w,h = 720,1050
cell_w = cell_h = w//12
big_screen = pg.display.set_mode((w,h))
pg.display.set_caption("Connect the dots!")
ccs = pg.Surface((w,h))
ccs.fill(WHITE)
pg.draw.rect(ccs,GREY,(1.5*cell_w,0,10.5*cell_w,13*cell_w-cell_w//2))
pg.draw.rect(ccs,WHITE,(1.5*cell_w,2.5*cell_h,10*cell_w,10*cell_h))
pg.draw.rect(ccs,BLUE,(0,0,1.5*cell_w,13*cell_w-cell_w//2))
pg.draw.rect(ccs,RED,(0,13*cell_w-cell_w//2,1.5*cell_w,5.5*cell_w))
pg.draw.rect(ccs,YELLOW,(1.5*cell_w,13*cell_w-cell_w//2,11*cell_w,6*cell_h))

"""Draw diagonal of squares"""
start_x = int(cell_w * 1.5 )
start_y = int(cell_h*11.5)
for i in range(11):
    x = start_x + i*cell_w
    y = start_y - i*cell_h
    pg.draw.rect(ccs,GREY,(x,y,cell_w,cell_h))

"""Draw X and Y axes """
for x in range(cell_w//2,w,cell_w):
    pg.draw.line(ccs,(0,0,0),(x,0),(x,h),2)
pg.draw.line(ccs,BLACK,(1.5*cell_w,0),(1.5*cell_w,h),22)
for y in range(cell_w//2,h,cell_w):
    pg.draw.line(ccs,(0,0,0),(0,y),(w,y),2)
pg.draw.line(ccs,BLACK,(0,13*cell_w-cell_w//2),(w,13*cell_w-cell_w//2),22)

"""Draw dotsies at intersection points"""
for x in range(cell_w//2,w,cell_w):
    for y in range(cell_w//2,h,cell_w):
        pg.draw.circle(ccs,BLACK,(x,y),5)

"""Draw index numbers on the X and Y axes"""
font = pg.font.SysFont('Helvetica', 18)
for n in range(0,18):
    num  = font.render(str(12-n),1,WHITE)
    ccs.blit(num,(cell_h*1.4,cell_h*n+16))
for n in range(-1,13):
    if n == 0: 
        continue
    num  = font.render(str(n),1,WHITE)
    ccs.blit(num,(cell_w*n+1.4*cell_w,13*cell_w-cell_w//2-10))

"""XY Logo"""
font = pg.font.SysFont('miriam', 200)
xy = font.render('X Y',1,WHITE)
ccs.blit(xy,(6*cell_w,14*cell_h))
"""Draw dot multipication sign between X and Y"""
pg.draw.circle(ccs,WHITE,(8.5*cell_w,15.5*cell_h),10)
    
"""Draw products in corners for pattern scripts"""
font = pg.font.SysFont('Helvetica', 22)
px = 0
for x in range(cell_w//2+cell_w*2-22,w,cell_w):
    px += 1
    py = 11
    for y in range(cell_h//2+2*cell_h,h,cell_h):
        py -= 1
        if py > 0 and py < 11 and px > 0 and px < 11:
            product = font.render(str((px)*(py)),1,BLACK)
            ccs.blit(product,(x,y))
       
#***********************************************

clock = pg.time.Clock()
FPS = 60
fig = randint(0,len(xys)-1)
points = zip(xys[fig][0],xys[fig][1])
locs = []
for point in points:
    locs.append((point[0]*cell_w+95,h - point[1]*cell_h-420))
for point in locs:
    print(point)

big_screen.fill((255,255,255))
while True:
    clock.tick(FPS)
    
    for ev in pg.event.get():
        if ev.type == pg.QUIT or (ev.type == pg.KEYDOWN and pg.K_ESCAPE): 
            pg.display.quit()       
            sys.exit()
    
    big_screen.blit(ccs,(0,0))
    #pg.draw.polygon(big_screen,(150,150,0),locs,14)
    pg.draw.lines(big_screen,1,(150,150,0),locs,14)
    pg.display.flip()