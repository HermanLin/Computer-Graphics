from display import *
from draw import *

screen = new_screen()
color = [ 255, 255, 255 ]

#testing
draw_line(250, 0, 250, 500, screen, color)
draw_line(0, 250, 500, 250, screen, color)
draw_line(0, 0, 500, 500, screen, color)
draw_line(0, 500, 500, 0, screen, color)
draw_line(250, 250, 500, 300, screen, color)
draw_line(250, 250, 350, 500, screen, color)
draw_line(250, 250, 350, 0, screen, color)
draw_line(250, 250, 500, 150, screen, color)
clear_screen(screen)

#tribute to the Falcon Heavy launch by SpaceX 2/6/18
color = [ 255, 0, 0 ]
#lefthalf
draw_line(0, 180, 75, 200, screen, color)
draw_line(25, 220, 75, 200, screen, color)
draw_line(25, 220, 25, 250, screen, color)
draw_line(25, 250, 70, 250, screen, color)
draw_line(70, 250, 75, 200, screen, color)
#righthalf
draw_line(75, 200, 100, 310, screen, color)
draw_line(100, 310, 400, 310, screen, color)
draw_line(400, 310, 425, 200, screen, color)
draw_line(425, 200, 430, 250, screen, color)
draw_line(430, 250, 475, 250, screen, color)
draw_line(475, 220, 475, 250, screen, color)
draw_line(425, 200, 475, 220, screen, color)
draw_line(425, 200, 500, 180, screen, color)
#windshield
draw_line(85, 200, 110, 300, screen, color)
draw_line(110, 300, 390, 300, screen, color)
draw_line(390, 300, 415, 200, screen, color)
draw_line(85, 200, 415, 200, screen, color)
draw_line(85, 200, 119, 250, screen, color)
draw_line(381, 230, 415, 200, screen, color)
#wheel
draw_line(340, 225, 366, 201, screen, color)
draw_line(305, 225, 340, 225, screen, color)
draw_line(280, 201, 305, 225, screen, color)
#hood
draw_line(70, 0, 85, 160, screen, color)
draw_line(85, 160, 200, 140, screen, color)
draw_line(200, 140, 300, 140, screen, color)
draw_line(300, 140, 415, 160, screen, color)
draw_line(415, 160, 430, 0, screen, color)
draw_line(80, 40, 420, 40, screen, color)
draw_line(85, 70, 415, 70, screen, color)

color = [ 0, 0, 255 ]
#righthandseat
draw_line(140, 270, 150, 299, screen, color) 
draw_line(120, 250, 140, 270, screen, color)
draw_line(120, 201, 120, 250, screen, color)
draw_line(170, 299, 180, 270, screen, color)
draw_line(180, 270, 200, 250, screen, color)
draw_line(200, 201, 200, 250, screen, color)

color = [ 255, 255, 255 ]
#starman
draw_line(250, 201, 250, 260, screen, color)
draw_line(250, 260, 280, 265, screen, color)
draw_line(270, 299, 285, 255, screen, color)
draw_line(285, 255, 325, 255, screen, color)
draw_line(325, 255, 345, 299, screen, color)
draw_line(330, 265, 345, 262, screen, color)
draw_line(345, 262, 398, 260, screen, color)
draw_line(365, 232, 405, 227, screen, color)
draw_line(360, 210, 365, 232, screen, color)
draw_line(270, 312, 285, 342, screen, color)
draw_line(285, 342, 325, 342, screen, color)
draw_line(325, 342, 345, 312, screen, color)

display(screen)
save_extension(screen, 'img.png')
