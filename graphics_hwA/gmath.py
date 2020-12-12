import math
from display import *

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    a = calculate_ambient(ambient, areflect)
    d = calculate_diffuse(light, dreflect, normal)
    s = calculate_specular(light, sreflect, view, normal)

    color = [0,0,0]
    for i in range(3):
        color[i] = a[i] + d[i] + s[i]
    return color
    
def calculate_ambient(alight, areflect):
    ambient = [0,0,0]
    for i in range(3):
        ambient[i] = int(alight[i] * areflect[i])
    return limit_color(ambient)

def calculate_diffuse(light, dreflect, normal):
    dot = dot_product(normalize(normal), normalize(light[LOCATION]))
    diffuse = [0,0,0]
    for i in range(3):
        diffuse[i] = int(light[COLOR][i] * dreflect[i] * dot)
    return limit_color(diffuse)
    
def calculate_specular(light, sreflect, view, normal):
    dot = dot_product(normalize(normal), normalize(light[LOCATION]))
    if dot > 0:
        specular = [0,0,0]
        rvect = [0,0,0]
        for i in range(3):
            rvect[i] = 2 * dot * normal[i] - light[LOCATION][i]
        
        exponent = dot_product(rvect, view) ** SPECULAR_EXP
    
        for i in range(3):
            specular[i] = int(light[COLOR][i] * sreflect[i] * exponent)
        return limit_color(specular)
    return [0,0,0]
    
def limit_color(color):
    for i in range(len(color)):
        if color[i] > 255:
            color[i] = 255
        if color[i] < 0:
            color[i] = 0
    return color

#vector functions
def normalize(vector):
    magnitude = math.sqrt(vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2)
    for i in range(len(vector)):
        vector[i] = vector[i] / magnitude
    return vector

def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
