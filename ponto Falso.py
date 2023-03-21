def falsa_posicao(f, a, b, tol):
    # calcula o valor da função nos extremos do intervalo
    fa = f(a)
    fb = f(b)
    # verifica se a função muda de sinal no intervalo
    if fa * fb >= 0:
        # se não muda, não é possível aplicar o método
        print("A função não muda de sinal no intervalo dado.")
        return None
    # repete o processo enquanto a diferença entre a e b for maior que a tolerância
    while abs(b-a) > tol:
        # calcula o novo ponto usando a fórmula do Método da Falsa Posição
        p = (a*fb - b*fa) / (fb - fa)
        # calcula o valor da função no novo ponto
        fp = f(p)
        # verifica se o valor da função no novo ponto é suficientemente próximo de zero
        if abs(fp) < tol:
            # se for, retorna o novo ponto como a raiz
            return p
        # atualiza o intervalo com base no novo ponto
        if fp * fa < 0:
            b = p
            fb = fp
        else:
            a = p
            fa = fp
    # retorna a média do novo intervalo como a raiz aproximada
    return (a+b)/2

def f(x):
    return x**3 - 9*x + 3

raiz = falsa_posicao(f, -1, 1, 1e-6)
print(raiz)