import mdl
from display import *
from matrix import *
from draw import *

def run(filename):
    """
    This function runs an mdl script
    This is the only file you need to modify in order
    to get a working mdl project (for now).

    my_main.c will serve as the interpreter for mdl.
    When an mdl script goes through a lexer and parser,
    the resulting operations will be in the array op[].

    Your job is to go through each entry in op and perform
    the required action from the list below:

    push: push a new origin matrix onto the origin stack

    pop: remove the top matrix on the origin stack

    move/scale/rotate: create a transformation matrix
                     based on the provided values, then
                     multiply the current top of the
                     origins stack by it.

    box/sphere/torus: create a solid object based on the
                    provided values. Store that in a
                    temporary matrix, multiply it by the
                    current top of the origins stack, then
                    call draw_polygons.

    line: create a line based on the provided values. Store
        that in a temporary matrix, multiply it by the
        current top of the origins stack, then call draw_lines.

    save: call save_extension with the provided filename

    display: view the screen
    """
    view = [0,
            0,
            1];
    ambient = [50,
               50,
               50]
    light = [[0.5,
              0.75,
              1],
             [0,
              255,
              255]]
    areflect = [0.1,
                0.1,
                0.1]
    dreflect = [0.5,
                0.5,
                0.5]
    sreflect = [0.5,
                0.5,
                0.5]

    color = [0, 0, 0]
    tmp = new_matrix()
    ident( tmp )

    stack = [ [x[:] for x in tmp] ]
    screen = new_screen()
    zbuffer = new_zbuffer()
    tmp = []
    polygons = []
    edges = []
    step_3d = 20

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
        for c in commands:
            
            if c[0] == 'push':
                stack.append([x[:] for x in stack[-1]])
            elif c[0] == 'pop':
                stack.pop()

            elif c[0] == 'move':
                t = make_translate(float(c[1]), float(c[2]), float(c[3]))
                matrix_mult(stack[-1], t)
                stack[-1] = [x[:] for x in t]
            elif c[0] == 'scale':
                s = make_scale(float(c[1]), float(c[2]), float(c[3]))
                matrix_mult(stack[-1], s)
                stack[-1] = [x[:] for x in s]
            elif c[0] == 'rotate':
                theta = float(c[2]) * (math.pi / 180)
                if c[1] == 'x':
                    r = make_rotX(theta)
                elif c[1] == 'y':
                    r = make_rotY(theta)
                else:
                    r = make_rotZ(theta)
                matrix_mult(stack[-1], r)
                stack[-1] = [x[:] for x in r]

            elif c[0] == 'box':
                add_box(polygons,
                        float(c[1]), float(c[2]), float(c[3]),
                        float(c[4]), float(c[5]), float(c[6]))
                matrix_mult(stack[-1], polygons)
                draw_polygons(polygons, screen, zbuffer, view, ambient, light, areflect, dreflect, sreflect)
                polygons = []
            elif c[0] == 'sphere':
                add_sphere(polygons,
                           float(c[1]), float(c[2]), float(c[3]),
                           float(c[4]), step_3d)
                matrix_mult(stack[-1], polygons)
                draw_polygons(polygons, screen, zbuffer, view, ambient, light, areflect, dreflect, sreflect)
                polygons = []
            elif c[0] == 'torus':
                add_torus(polygons,
                          float(c[1]), float(c[2]), float(c[3]),
                          float(c[4]), float(c[5]), step_3d)
                matrix_mult(stack[-1], polygons)
                draw_polygons(polygons, screen, zbuffer, view, ambient, light, areflect, dreflect, sreflect)
                polygons = []
            elif c[0] == 'line':
                add_edge(edges,
                         float(c[1]), float(c[2]), float(c[3]),
                         float(c[4]), float(c[5]), float(c[6]))
                matrix_mult(stack[-1], edges)
                draw_lines(edges, screen, zbuffer, color)
                edges = []
                
            elif c[0] == 'save':
                save_extension(screen, c[1] + c[2])
            elif c[0] == 'display':
                display(screen)
            
    else:
        print "Parsing failed."
        return
