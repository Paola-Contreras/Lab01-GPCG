#Universidad del Valle de Guatemala
#Graficos por computador - S20 
#Gabriela Paola Contreras Guerra
#LAB 01 -- Fill polgygon

from poligonos import Renderer, color, V2

w = 900
h = 500

rend = Renderer (w,h)
rend.glClearColor(0,0,0)
rend.glColor(1,1,1)
rend.glClear()

#Arrays of points 
P1 = [V2(165, 380), V2(185, 360), V2(180, 330), V2(207, 345),
      V2(233, 330), V2 (230, 360),V2(250, 380), V2(220, 385),
      V2(205, 410), V2(193, 383)]

P2 = [V2(321, 335), V2(288, 286), V2(339, 251), V2(374, 302)]

P3 = [V2(377, 249), V2(411, 197), V2(436, 249)]

P4 = [V2(413, 177), V2(448, 159), V2(502, 88),  V2(553, 53),
      V2(535, 36),  V2(676, 37),  V2(660, 52),  V2(750, 145),
      V2(761, 179), V2(672, 192), V2(659, 214), V2(615, 214), 
      V2(632, 230), V2(580, 230), V2(597, 215), V2(552, 214),
      V2(517, 144), V2(466, 180)]

P5 = [V2(682, 175), V2(708, 120), V2(735, 148), V2(739, 170)]


def draw (polygon, clr):
    for i in range (len(polygon)):
        rend.glLine(polygon[i], polygon[(i + 1) % len(polygon)], clr)


#Draw each polygon 
draw(P1, color(1,1,0))
draw(P2, color(0,0.8,0.8))
draw(P3, color(0,0.8,0.4))
draw(P4, color(0.75,0.75,0.75))
draw(P5, color(0.75,0.75,0.75))

#Fill each polygon
rend.glFill(P1,color(1,1,0))
rend.glFill(P2,color(0,0.8,0.8))
rend.glFill(P3,color(0,0.8,0.4))
rend.glFill(P4,color(0.75,0.75,0.75))
rend.glFill(P5,color(0,0,0))

#GENEATE IMG 
rend.glFinish("lab1.bmp")