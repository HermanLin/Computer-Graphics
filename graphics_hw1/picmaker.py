#Create a .ppm file with randomly colored pixels

import random
def rand():
    return random.randint(0,255)

def w2f(file):
    file.write('P3\n')
    file.write('500 500\n')
    file.write('255\n')

    for i in range(0,500):
        for j in range(0,500):
            pixel = str(rand()) + ' ' + str(rand()) + ' ' + str(rand()) + ' '
            file.write(pixel)
            #print(pixel)
        file.write('\n')
    return

def main():
    f = open('pikchurr.ppm', 'w')
    w2f(f)
    f.close
    
main()
