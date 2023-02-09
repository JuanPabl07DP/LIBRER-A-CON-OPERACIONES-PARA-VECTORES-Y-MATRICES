#Juan Pablo Daza Pereira
#CNYT.
import math
def suma(c1, c2):

    return [c1[0] + c2[0], c1[1] + c2[1]]


def resta(c1, c2):

    return [c1[0] - c2[0], c1[1] - c2[1]]


def producto(c1, c2):

    real = c1[0] * c2[0] - c1[1] * c2[1]
    imaginario = c1[0] * c2[1] + c1[1] * c2[0]
    return [real, imaginario]


def division(c1, c2):

    num = producto(c1, conjugado(c2))
    denomi = producto(c2, conjugado(c2))
    real = num[0] / denomi[0]
    imaginario = num[1] / denomi[0]
    return [real, imaginario]


def conjugado(c1):

    return [c1[0], c1[1]*-1]


def modulo(c1):

    return math.sqrt(c1[0]**2 + c1[1]**2)


def imprimir(c1):

    if c1[1] > 0:
        return str(c1[0])+'+'+str(c1[1]) + 'i'
    else:
        return str(c1[0])+str(c1[1]) + 'i'


def cart_pol(c1):

    r = math.sqrt(c1[0]**2 + c1[1]**2)
    angle = math.degrees(math.atan2(c1[1], c1[0]))
    return [r, angle]


def pol_cart(c1):

    r, angle = c1[0], math.radians(c1[1])
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    return [x, y]


def fase(c1):

    return math.degrees(math.atan2(c1[1], c1[0]))


def imprimir_exponencial(c1):

    return str(modulo(c1))+"e^i"+" ("+str(fase(c1))+")"

def potencia_n(c1,n):

    if n>1:
        rta = 0

        for i in range(1,n+1):
            if i == 1:
                rta = c1
            else:
                rta = producto(rta,c1)
        return rta
    elif n == 1:
        return c1

#--------------------------------------Libreria con operaciones para vectores y matrices------------------------------------------------------
"V: vectores"
"M: matrices"

def sumaV(v1, v2):

    res = []
    if len(v1) == len(v2):
        for i in range(len(v1)):
            res.append(suma(v1[i][0], v2[i][0]))
        return res
    else:
        return "Syntax Error"


def restaV(v1, v2):

    res = []
    if len(v1) == len(v2):
        for i in range(len(v1)):
            res.append(resta(v1[i][0], v2[i][0]))
        return res
    else:
        return "Syntax Error"


def inversoAditivoV(v1):

    res = []
    for i in range(len(v1)):
        res.append(producto(v1[i][0], [-1, 0]))
    return res


def productoEscalarV(v1, ec1):

    res = []
    for i in range(len(v1)):
        for j in range(len(v1[0])):
            res.append(producto(v1[i][0], ec1))
    return res


def adicionM(m1, m2):

    res = []
    if len(m1) == len(m2):
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                res.append(suma(m1[i][j], m2[i][j]))
        return res
    else:
        return "Syntax Error"


def inversoAditivoM(m1):

    res = []
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            res.append(producto(m1[i][j], [-1, 0]))
    return res


def productoEscalarM(m1, ec1):

    res = []
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            res.append(producto(m1[i][j], ec1))
    return res


def transpuestaMV(m1):

    filas = len(m1)
    columnas = len(m1[0])
    m2 = [[None for i in range(filas)]for j in range(columnas)]

    for i in range(filas):
        for j in range(columnas):
            m2[j][i] = m1[i][j]
    return m2


def conjugadoMV(m1):

    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m1[i][j] = conjugado(m1[i][j])
    return m1


def dagaMV(m1):

    return transpuestaMV(conjugadoMV(m1))


def productoM(m1, m2):

    filasm1, filasm2 = len(m1), len(m2)
    columnasm1, columnasm2 = len(m1[0]), len(m2[0])
    if columnasm1 == filasm2:
        mr = [[[0, 0] for columnas in range(columnasm2)]for filas in range(filasm1)]
        for i in range(filasm1):
            for j in range(columnasm2):
                for k in range(filasm2):
                    mr[i][j] = suma(mr[i][j],producto(m1[i][k], m2[k][j]))
        return mr
    else:
        return "Syntax Error"


def accionMV(m1, v2):

    return productoM(m1, v2)

def productoInterno(v1,v2):

    return productoM(dagaMV(v1),v2)


def normaV(v1):

    x = productoInterno(v1, v1)
    complejo = [x[0][0][0], x[0][0][1]]
    return modulo(complejo)


def distanciaV(v1,v2):

    resta = restaV(v1,v2)
    res = normaV(resta)
    return res


def unitariaM(m1):

    filas = len(m1)
    columnas = len(m1[0])
    mIdentidad = [[1 if  j==i else 0 for j in range(columnas)]for i in range(filas)]
    
    if productoM(m1,dagaMV(m1)) == mIdentidad:
        return True
    else:
        return False


def hermitianaM(m1):

    if dagaMV(m1) == m1:
        return True
    else:
        return False


def productoTensorialM(m1, m2):

    filasm1, filasm2 = len(m1), len(m2)
    columnasm1, columnasm2 = len(m1[0]), len(m2[0])
    mr = [[[0, 0] for i in range(columnasm1*columnasm2)]for j in range(filasm1*filasm2)]
    for i in range(len(mr)):
        for j in range(len(mr[0])):
            mr[i][j] = producto(m1[i//filasm2][j//columnasm2], m2[i%filasm2][j%columnasm2])
    return mr
