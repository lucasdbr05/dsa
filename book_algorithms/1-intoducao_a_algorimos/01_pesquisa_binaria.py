"Executado e tempo logaritimo O(log2 (x))"
"A notação Big O é uma notação especial que diz o quão rápido é um algoritmo. A notação Big O informa o quão rápido é um algoritmo."
"A notação Big O leva em conta a pior das hipóteses. Então pode-se dizer que, para o pior caso, você analisou cada item da lista. Esse é o tempo O(n)."


def pesquisa_binaria(lista, item):
    baixo = 0 
    alto = len(lista) - 1 
    while baixo <= alto: 
        meio = (baixo + alto) // 2 
        chute = lista[meio]
        if chute == item: 
            return meio
        if chute > item: 
            alto = meio - 1
        else: 
            baixo = meio + 1

    return None 
    
minha_lista = [1, 3, 5, 7, 9] 
print(pesquisa_binaria(minha_lista, 3))