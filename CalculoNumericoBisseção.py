def bissecao():

    print("O código é uma implementação do método da bisseção para encontrar a raiz de uma função.")
    # inserção dos valores para o cálculo
    f = input('escreva a função: ')                               # função
    a = float(input('escreva o limite inferior: '))               # valor de a
    b = float(input('escreva o limite superior: '))               # valor de b
    tol = float(input('tolerância desejada: '))                   # tolerância 
    k_max = int(input('digite o valor de iterações: '))           # quantidade de iterações


    # O método analisa a expressão passada para esse método e executa a expressão python ( code ) dentro do programa.
    fa = eval(f.replace('x', 'a'))                                
    fb = eval(f.replace('x', 'b'))
   
    if fa * fb > 0:                                               # Essa linha verifica se o sinal da função não muda entre os limites inferior e superior.
        print(" A função não muda o sinal")                       # Se isso acontecer, o método não pode ser aplicado e uma mensagem de erro é impressa.
        return None
    
    it = 0                                                        # it = iterações para cada if

    while (b - a) / 2 > tol and it < k_max:                       # Essa linha inicia um loop enquanto a diferença entre os limites superior e inferior 
        c = (a + b) / 2                                           # dividida por dois for maior que a tolerância e o número de iterações for menor que o número máximo permitido.
        fc = eval(f.replace('x', 'c'))
        
        if fc == 0:                                               # Essa linha verifica se o ponto médio é uma raiz exata. Se for, o ponto médio é retornado como a raiz.                            
            return c
        
        if fa * fc < 0:                                           # Essa linha verifica se a raiz está no intervalo inferior ao ponto médio. Se estiver, o limite superior é atualizado para o ponto médio.
            b = c
            fb = fc
        it+= 1

        if it == k_max:                                           # Essa linha verifica se o número de iterações atingiu o limite máximo permitido. Se isso acontecer, o método não convergiu e uma
            print(" o metodo não convergiu após {} iterações".format(k_max))
            return None
        
        return (a + b) / 2
    

raiz = bissecao()
if raiz is not None:
    print("valor aproximado da raiz é: ", raiz)