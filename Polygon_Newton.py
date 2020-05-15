import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from scipy.spatial import ConvexHull

repetir = 's'

# x**2+y**2+3*x**3+5*y+x*y**3+x*y+x*y**2
# x^2+x^2*y+y+x+y^2
# x**2*y+x+y*x**3+2*x*y**2

while repetir == 's':

    x, y = symbols('x y')

    coord_x = []
    coord_y = []


    print(""" \n\nExemplos de P(x,y):
            # x**2+y**2+3*x**3+5*y+x*y**3+x*y+x*y**2
            # x^2+x^2*y+y+x+y^2
            # y^6 + 3*x^11*y**4+2*x**10*y3-3*x**22*y**2+6*x**21*y+x**33-x**20
            # x**2*y+x+y*x**3+2*x*y**2\n
            """)
    func_xy = input('Coloque o Polinômio -> P(x,y): ')
    func_xy = sympify(func_xy)
    func_x = Poly(func_xy, x)
    func_y = Poly(func_xy, y)
    monomios_x = Poly(func_xy, x, y).monoms()

    print(f'Organizando: {func_xy}')
    print(f'Expoentes (x, y): {monomios_x}')

    contador = 0
    points = np.array([[100, 100]])

    for coordenadas in monomios_x:
        a, b = coordenadas
        coord_x.append(a)
        coord_y.append(b)

        if contador == 0:
                points = np.append(points, [[a, b]], axis=0)
                points = np.delete(points, 0, 0)
        else:   points = np.append(points, [[a, b]], axis=0)

        contador = contador + 1

    hull = ConvexHull(points)

    plt.plot(points[:, 0], points[:, 1], 'o')

    for simplex in hull.simplices:
        plt.plot(points[simplex, 0], points[simplex, 1], 'k-')

    plt.plot(points[hull.vertices, 0], points[hull.vertices, 1], 'r--', lw=2)
    plt.plot(points[hull.vertices[0], 0], points[hull.vertices[0], 1], 'ro')

    for xy in zip(coord_x, coord_y):
        plt.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')

    plt.show()

    repetir  = str(input("\n\n Deseja plotar outra curva? (s/n): "))
