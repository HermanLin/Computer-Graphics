from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    A = y1 - y0
    B = -1 * (x1 - x0)
    
    if A == 0:
        while x <= x1:
            plot(screen, color, x, y)
            x += 1
    elif B == 0:
        while y <= y1:
            plot(screen, color, x, y)
            y += 1
    
    else:
        slope = A / (x1 - x0)
        
        #octant 1
        if slope >= 0 and slope <= 1: 
            d = (2 * A) + B
            while x <= x1:
                plot(screen, color, x, y)
                if d > 0:
                    y += 1
                    d += 2 * B
                x += 1
                d += 2 * A

        #octant 2
        elif slope > 1:
            d = A + (2 * B)
            while y <= y1:
                plot(screen, color, x, y)
                if d < 0:
                    x += 1
                    d += 2 * A
                y += 1
                d += 2 * B

        #octant 7        
        elif slope < -1:
            d = A - (2 * B)
            while y >= y1:
                plot(screen, color, x, y)
                if d > 0:
                    x += 1
                    d += 2 * A
                y -= 1
                d -= 2 * B

        #octant 8
        elif slope >= -1:
            d = (2 * A) - B
            while x <= x1:
                plot(screen, color, x, y)
                if d < 0:
                    y -= 1
                    d -= 2 * B
                x += 1
                d += 2 * A
