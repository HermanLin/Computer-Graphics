import math

def make_translate( x, y, z ):
    t = new_matrix()
    ident(t)
    t[3][0] = x
    t[3][1] = y
    t[3][2] = z
    print_matrix(t)
    return t
    
def make_scale( x, y, z ):
    s = new_matrix()
    s[0][0] = x
    s[1][1] = y
    s[2][2] = z
    s[3][3] = 1
    print_matrix(s)
    return s
    
def make_rotX( theta ):    
    x = new_matrix()
    r = math.radians(theta)
    ident(x)
    x[1][1] = math.cos(r)
    x[1][2] = math.sin(r)
    x[2][1] = math.sin(r) * -1
    x[2][2] = math.cos(r)
    print_matrix(x)
    return x

def make_rotY( theta ):
    y = new_matrix()
    r = math.radians(theta)
    ident(y)
    y[0][0] = math.cos(r)
    y[0][2] = math.sin(r) * -1
    y[2][0] = math.sin(r)
    y[2][2] = math.cos(r)
    print_matrix(y)
    return y

def make_rotZ( theta ):
    z = new_matrix()
    r = math.radians(theta)
    ident(z)
    z[0][0] = math.cos(r)
    z[0][1] = math.sin(r)
    z[1][0] = math.sin(r) * -1
    z[1][1] = math.cos(r)
    print_matrix(z)
    return z

def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print s

def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

#def scalar_mult( matrix, s ):
#    for r in range( len( matrix[0] ) ):
#        for c in range( len(matrix) ):
#            matrix[c][r]*= s
            
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):

    point = 0
    for row in m2:
        #get a copy of the next point
        tmp = row[:]
        
        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point+= 1


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
