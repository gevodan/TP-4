from math import exp, log, sin, cos

epsilon = 1e-10
Nitermax = 500

def Newton (f, fder, x0, epsilon, Nitermax, alpha) :
    xold = x0
    xnew = f(x0)
    n = 0
    l_n = []
    l_xnew = []
    l_en = []
    while abs (xnew - xold) > epsilon and n < Nitermax :
        xold = xnew
        xnew = xold - (f(xold) / fder(xold))
        en = abs(xnew - alpha)
        n = n + 1
        l_n.append(n)
        l_xnew.append(xnew)
        l_en.append(en)
    return (l_n, l_xnew, l_en, n)

def PointFixe (g, x0, epsilon, Nitermax, alpha) :
    xold = x0
    xnew = g(x0)
    n = 0
    l_n = []
    l_xnew = []
    l_en = []
    while abs (xnew - xold) > epsilon and n < Nitermax :
        xold = xnew
        xnew = g(xold)
        n = n + 1
        en = abs(xnew - alpha)
        l_n.append(n)
        l_xnew.append(xnew)
        l_en.append(en)
    return ("liste des n : ", l_n, "liste des xn : ", l_xnew, "liste des en : ", l_en, n)

def dichotomie (f, a0, b0, epsilon, Nitermax, alpha) :
    an = a0
    bn = b0
    n = 0
    l_n = []
    l_an = []
    l_en = []
    while (abs((bn - an)) > epsilon and n < Nitermax) :
        m = (an + bn) / 2
        if f(an) * f(m) <= 0 :
            bn = m
        else :
            an = m
        en = abs (an - alpha)
        n = n + 1
        l_n.append(n)
        l_an.append(an)
        l_en.append(en)
    return (l_n, l_an, l_en, n)

def secante (f, x0, x1, epsilon, Nitermax, alpha) :
    xn = x0
    xn1 = x1
    n = 0
    l_n = []
    l_xn2 = []
    l_en = []
    while (abs(xn1-xn)) > epsilon and n < Nitermax :
        xn2 = xn1 - f(xn1) * (xn1 - xn) / (f(xn1) - f(xn))
        xn = xn1
        xn1 = xn2
        en = abs(xn2 - alpha)
        n = n + 1
        l_n.append(n)
        l_xn2.append(xn2)
        l_en.append(en)
    return (l_n, l_xn2, l_en, n)

def f1 (x) :
    return (x * exp(x) - 7)

def f1der (x) :
    x = exp(x) + x * exp(x)
    return x

def g1 (x) :
    x = log(7/x)
    return x

def f2 (x) :
    return (exp(x) - 2* sin(x) - 7)

def f2der (x) :
    x = exp(x) - 2 * cos(x)
    return x

def g2 (x) :
    x = log (2 * sin(x) + 7)
    return x

def f3 (x) :
    return (exp(x) - x**2 - 3)

def f3der (x) :
    x = exp(x) - 2 * x
    return x

def g3 (x) :
    x = log (x**2 + 3)
    return x

alphasec1 = secante (f1, 2, 3, epsilon, Nitermax, 1.524345204984144)
print (alphasec1)

alphadic1 = dichotomie (f1, -1, 30, epsilon, Nitermax, 1.524345204984144)
print (alphadic1)

alphanew1 = Newton (f1, f1der, 2, epsilon, Nitermax, 1.524345204984144)
print (alphanew1)

alphapoint1 = PointFixe (g1, 1, epsilon, Nitermax, 1.524345204984144)
print (alphapoint1)

alphasec2 = secante (f2, 2, 3, epsilon, Nitermax, 2.159143931310106)
print (alphasec2)

alphadic2 = dichotomie (f2, 1, 3, epsilon, Nitermax, 2.159143931310106)
print (alphadic2)

alphanew2 = Newton (f2, f2der, 2.5, epsilon, Nitermax, 2.159143931310106)
print (alphanew2)

alphapoint2 = PointFixe (g2, 2, epsilon, Nitermax, 2.159143931310106)
print (alphapoint2)

alphasec3 = secante (f3, 2, 3, epsilon, Nitermax, 1.873122547713044)
print (alphasec3)

alphadic3 = dichotomie (f3, 1, 2, epsilon, Nitermax, 1.873122547713044)
print (alphadic3)

alphanew3 = Newton (f3, f3der, 1, epsilon, Nitermax, 1.873122547713044)
print (alphanew3)

alphapoint3 = PointFixe (g3, 1.8, epsilon, Nitermax, 1.873122547713044)
print (alphapoint3)



