def f(x):
    return x**3 - 9*x + 3


def q(x):
    return (x**3/9) + (1/3)


def metodo_iterativo(X0, E1, E2, max_iter):
    # 1) Dados iniciais
    # a) X0: aproximação inicial
    # b) E1 e E2: precisões
    # c) max_iter: número máximo de iterações
    # 2) Se | f(X0) | < E1 faça X' = X0. FIM
    if abs(f(X0)) < E1:
        return X0
    # 3) k=1
    k = 1
    while k <= max_iter:
        # 4) X1 = Q(X0)
        X1 = q(X0)

        #TOLERANCIA
        # 5) Se |f(X1)| < E1 ou se |X1 - X0|< E2
        # Então X' = X1. FIM
        if abs(f(X1)) < E1 or abs(X1 - X0) < E2:
            return X1
        # 6) X0 =X1
        X0 = X1
        # 7) k+1, Volte ao passo 4.
        k += 1
    # 9) Se o número máximo de iterações foi atingido e a raiz ainda não foi encontrada, retorne None
    return None

# valor de mais proximo da raiz
raiz = metodo_iterativo(0.5, 0.0005, 0.0005, 3)
print(raiz)
# valor da raiz em F(x)
X= print(f(raiz))
