import math


def print_matrix( matrix ):
    print "\n"
    for r in matrix:
        for c in r:
            print c,
        print "\n"

def ident( matrix ):
    for c in xrange(len(matrix)):
        for r in xrange(len(matrix[c])):
            if c == r:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    rowm1 = len(m1)
    rowm2 = len(m2)
    colm2 = len(m2[0])
    tmp = new_matrix(rows = len(m2[0]),cols = len(m2))
    for a in range(rowm1):
        for b in range(colm2):
            for c in range(rowm2):
                tmp[a][b] += m1[a][c] * m2[c][b]
    for c in range(rowm2):
        for r in range(colm2):
            m2[c][r] = tmp[c][r]

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
