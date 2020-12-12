from display import *
from matrix import *


def draw_lines( matrix, screen, color ):
    point = 0
    while point < len(matrix):
        x0 = matrix[point][0]
        y0 = matrix[point][1]
        x1 = matrix[point + 1][0]
        y1 = matrix[point + 1][1]
        draw_line(x0, y0, x1, y1, screen, color)
        point += 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point( matrix, x, y, z=0 ):
    matrix.append([x,y,z,1])

def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    A = y1 - y0
    B = x0 - x1
    x = x0
    y = y0

    # octant 1
    if (abs(B) >= abs(A) and A * B <= 0):
        d = 2 * A + B
        while (x <= x1):
            plot(screen, color, x, y)
            if (d > 0):
                y += 1
                d += 2 * B
            x += 1
            d += 2 * A

    # octant 2
    elif (abs(A) >= abs(B) and A * B <= 0):
        d = A + 2 * B
        while (y <= y1):
            plot(screen, color, x, y)
            if (d < 0):
                x += 1
                d += 2 * A
            y += 1
            d += 2 * B

    # octant 7
    elif (abs(A) >= abs(B) and A * B >= 0):
        d = A - 2 * B
        while (x <= x1):
            plot(screen, color, x, y)
            if (d > 0):
                x += 1
                d += 2 * A
            y -= 1
            d -= 2 * B

    # octant 8
    elif (abs(B) >= abs(A) and A * B >= 0):
        d = 2 * A - B
        while (x <= x1):
            plot(screen, color, x, y)
            if (d < 0):
                y -= 1
                d -= 2 * B
            x += 1
            d += 2 * A
    
    # x = x0
    # y = y0
    # A = y1 - y0
    # B = -1 * (x1 - x0)
     
    # if A == 0:
    #     while x <= x1:
    #         plot(screen, color, x, y)
    #         x += 1
    # elif B == 0:
    #     while y <= y1:
    #         plot(screen, color, x, y)
    #         y += 1
            
    # else:
    #     slope = A / (x1 - x0)
        
    #     #octant 1
    #     if slope >= 0 and slope <= 1: 
    #         d = (2 * A) + B
    #         while x <= x1:
    #             plot(screen, color, x, y)
    #             if d > 0:
    #                 y += 1
    #                 d += 2 * B
    #                 x += 1
    #                 d += 2 * A

    #     #octant 2
    #     elif slope > 1:
    #         d = A + (2 * B)
    #         while y <= y1:
    #             plot(screen, color, x, y)
    #             if d < 0:
    #                 x += 1
    #                 d += 2 * A
    #                 y += 1
    #                 d += 2 * B

    #     #octant 8
    #     elif slope >= -1:
    #         d = (2 * A) - B
    #         while x <= x1:
    #             plot(screen, color, x, y)
    #             if d < 0:
    #                 y -= 1
    #                 d -= 2 * B
    #                 x += 1
    #                 d += 2 * A

    #     #octant 7        
    #     elif slope < -1:
    #         d = A - (2 * B)
    #         while y >= y1:
    #             plot(screen, color, x, y)
    #             if d > 0:
    #                 x += 1
    #                 d += 2 * A
    #                 y -= 1
    #                 d -= 2 * B
