from display import *
from matrix import *
from draw import *
import math

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    points = new_matrix()
    f = open(fname, 'r')
    commands = f.readlines()

    for i in range(len(commands)):
        if commands[i] == "line\n":
            print "LINE COMMAND"
            coords = commands[i + 1].split(" ")
            coords = [int(j) for j in coords]
            add_edge(points, coords[0], coords[1], coords[2],
                     coords[3], coords[4], coords[5])
        elif commands[i] == "ident\n":
            print "IDENT COMMAND"
            ident(transform)
        elif commands[i] == "scale\n":
            print "SCALE COMMAND"
            scale_f = commands[i + 1].split(" ")
            scale_f = [int(j) for j in scale_f]
            scale = make_scale(scale_f[0], scale_f[1], scale_f[2])
            matrix_mult(scale, transform)
        elif commands[i] == "move\n":
            print "MOVE COMMAND"
            trans_f = commands[i + 1].split(" ")
            trans_f = [int(j) for j in trans_f]
            translate = make_translate(trans_f[0], trans_f[1], trans_f[2])
            matrix_mult(translate, transform)
        elif commands[i] == "rotate\n":
            print "ROTATE COMMAND"
            params = commands[i + 1].split(" ")
            theta = int(params[1])
            #print "theta: " + str(theta)
            if params[0] == "x":
                rotate = make_rotX(theta)
            elif params[0] == "y":
                rotate = make_rotY(theta)
            elif params[0] == "z":
                rotate = make_rotZ(theta)
            matrix_mult(rotate, transform)
        elif commands[i] == "apply\n":
            print "APPLY COMMAND"
            matrix_mult(transform, points)
        elif commands[i] == "display\n":
            print "DISPLAY COMMAND"
            for r in range(len(points)):
                for c in range(len(points[r])):
                    points[r][c] = int(points[r][c])
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
        elif commands[i] == "save\n":
            print "SAVE COMMAND"
            filename = commands[i + 1]
            filename = filename.strip()
            save_extension(screen, filename)
        elif commands[i] == "quit\n":
            print "QUIT COMMAND"
            break
        else:
            pass
