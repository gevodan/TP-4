from math import exp, log, sin, cos
import matplotlib.pyplot as plt

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
    return (l_n, l_xnew, l_en, n)

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
        en = abs(xn1 - alpha)
        n = n + 1
        l_n.append(n)
        l_xn2.append(xn2)
        l_en.append(en)
    return (l_n, l_xn2, l_en, n)

def f0(x):
    return (2*x)-(1+sin(x))

def g0(x):
    return (1+sin(x))/2

def f0der(x):
    return 2-cos(x)

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

alphasec0 = secante(f0,0,1,epsilon, Nitermax,0.8878622115708659)
alphanew0 = Newton (f0, f0der, 0, epsilon, Nitermax,0.8878622115708659)
alphapoint0 = PointFixe (g0, 0, epsilon, Nitermax, 0.8878622115708659)
alphadic0 = dichotomie (f0, 0, 1, epsilon, Nitermax, 0.8878622115708659)


alphasec1 = secante (f1, 2, 3, epsilon, Nitermax, 1.5243452049841444)

alphadic1 = dichotomie (f1, -1, 30, epsilon, Nitermax, 1.5243452049841444)

alphanew1 = Newton (f1, f1der, 2, epsilon, Nitermax, 1.5243452049841444)


alphapoint1 = PointFixe (g1, 1, epsilon, Nitermax, 1.5243452049841444)

alphasec2 = secante (f2, 2, 3, epsilon, Nitermax, 2.1591439313101066)


alphadic2 = dichotomie (f2, 1, 3, epsilon, Nitermax, 2.1591439313101066)


alphanew2 = Newton (f2, f2der, 2.5, epsilon, Nitermax, 2.1591439313101066)

alphapoint2 = PointFixe (g2, 2, epsilon, Nitermax, 2.1591439313101066)


alphasec3 = secante (f3, 2, 3, epsilon, Nitermax,1.8731225477130433)


alphadic3 = dichotomie (f3, 1, 2, epsilon, Nitermax, 1.8731225477130433)


alphanew3 = Newton (f3, f3der, 1, epsilon, Nitermax, 1.8731225477130433)


alphapoint3 = PointFixe (g3, 1.8, epsilon, Nitermax, 1.8731225477130433)

def graph(alphasec,alphanew,alphapoint,alphadic):
     a=alphasec[3]
     a=str(a)
     a1="méthode de la sécante:" + a + " itération(s)"
     b=alphanew[3]
     b=str(b)
     b1="méthode de newton:" + b + " itération(s)"
     c=alphapoint[3]
     c=str(c)
     c1="méthode du point fixe:" + c + " itération(s)"
     d=alphadic[3]
     d=str(d)
     d1="méthode de la dichotomie:" + d + " itération(s)"
     plt.semilogy(alphasec[0] ,alphasec[2],color='r',label=a1)
     plt.semilogy(alphanew[0] ,alphanew[2],color='green',label=b1)
     plt.semilogy(alphapoint[0] ,alphapoint[2],color='y',label=c1)
     plt.semilogy(alphadic[0] ,alphadic[2],color='b',label=d1)
     plt.xlabel('itérations')
     plt.ylabel("erreur")
     plt.title("Evolution de l'erreur en fonction du nombre d'itérations")
     plt.legend()
     plt.show()
     print("erreur dicho=", alphadic[2][-1])
     print("erreur newton=", alphanew[2][-1])
     print("erreu point fixe=",alphapoint[2][-1])
     print("erreur secante=", alphasec[2][-1])
print(graph(alphasec1,alphanew1,alphapoint1,alphadic1))
print(graph(alphasec2,alphanew2,alphapoint2,alphadic2))
print(graph(alphasec3,alphanew3,alphapoint3,alphadic3))

