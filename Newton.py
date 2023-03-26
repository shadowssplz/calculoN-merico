def newton(f, df, x0, tol=1e-6, max_iter=100):
    """
    Encontra a raiz da função f usando o método de Newton.

    Parâmetros:
    f: função para encontrar a raiz
    df: derivada da função f
    x0: estimativa inicial da raiz
    tol: tolerância para convergência (default = 1e-6)
    max_iter: número máximo de iterações (default = 100)

    Retorna:
    x: estimativa da raiz
    """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(fx) < tol:
            return x
        if dfx == 0:
            raise ValueError("Derivada zero. Impossível continuar.")
        x = x - fx / dfx
    raise ValueError("Número máximo de iterações excedido.")

def f(x):
    return x**2 - 2

def df(x):
    return 2 * x

x0 = 1.5
raiz = newton(f, df, x0)
print(raiz)
