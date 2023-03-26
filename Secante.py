def secante(f, x0, x1, tol=1e-6, max_iter=100):
    """
    Encontra a raiz da função f usando o método da secante.

    Parâmetros:
    f: função para encontrar a raiz
    x0: primeira estimativa inicial da raiz
    x1: segunda estimativa inicial da raiz
    tol: tolerância para convergência (default = 1e-6)
    max_iter: número máximo de iterações (default = 100)

    Retorna:
    x: estimativa da raiz
    """
    fx0 = f(x0)
    fx1 = f(x1)
    for i in range(max_iter):
        dfx = (fx1 - fx0) / (x1 - x0)
        x = x1 - fx1 / dfx
        if abs(x - x1) < tol:
            return x
        x0, x1 = x1, x
        fx0, fx1 = fx1, f(x)
    raise ValueError("Número máximo de iterações excedido.")
def f(x):
    return x**3 - 3*x + 1

x0 = 0
x1 = 1

raiz = secante(f, x0, x1)

print(raiz)
