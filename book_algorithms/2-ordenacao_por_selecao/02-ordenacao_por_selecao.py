"Array: elementos armazenados na memoria de maneira sequencial, o que torna mais facl a busca por um elemto qualquer; mas dificulta a insercao de um novo elemento(por conta do espaco na memoria sequinte ao do array estar ocupado por um outros elementos), sendo necessario o deslocamento para outro lugar(Todos os elementos de um array devem ser do mesmo tipo (todos ints, todos doubles, e assim por diante))."
"Lista encadeada: divisao dos elementos e espacos nao-sequenciais na memoria, o que facilita o armazenamento dos elementos e acoes de adicionar ou deletar itens; mas dificulta a busca por elementos especificos, por ser necessario passar por cada um dos elementos em sequencia ate encontra-lo"


def buscaMenor(arr):
    menor = arr[0] 
    menor_indice = 0 
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def ordenacaoporSelecao(arr): 
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr) 
        novoArr.append(arr.pop(menor))
    return novoArr

'=>O(n*n)'
print(ordenacaoporSelecao([5, 3, 6, 2, 10])) 