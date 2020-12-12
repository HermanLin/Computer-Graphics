from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

print "testing make_translate(7, 8, 9)"
make_translate(7, 8, 9)
print "testing make_scale(4, 5, 6)"
make_scale(4, 5, 6)
print "testing make_rotX(30)"
make_rotX(30)
print "testing make_rotY(30)"
make_rotY(30)
print "testing make_rotZ(30)"
make_rotZ(30)

print "testing parser and script"
parse_file( 'script', edges, transform, screen, color )

screen = new_screen()
edges = []
transform = new_matrix()
print "testing my_script"
parse_file('my_script', edges, transform, screen, color) 
