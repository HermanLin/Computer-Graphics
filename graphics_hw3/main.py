from display import *
from draw import *
from matrix import *
import random

screen = new_screen()
color = [ 0, 255, 0 ]

matrix = new_matrix()
print_matrix(matrix)
ident(matrix)
print_matrix(matrix)

m = new_matrix()
for i in range(0, 18):
    x0 = random.randint(0, 500)
    y0 = random.randint(0, 500)
    x1 = random.randint(0, 500)
    y1 = random.randint(0, 500)
    add_edge(m, x0, y0, 0, x1, y1, 0)

draw_lines( m, screen, color )
display(screen)
