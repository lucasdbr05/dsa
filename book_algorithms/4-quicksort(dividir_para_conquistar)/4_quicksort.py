"Quicksort"
"Sua notacao Big O depende do pivot escolhido"
"No pior dos casos= O(n*n)"
"No caso medio = O(n log2 (n))"
def quicksort(array):
    if len(array) < 2: 
        return array   #retorna arrays vazios e com elementos menores que um
    else:
        pivo = array[0] #primeiro elemento do array
        menores = [i for i in array[1:] if i <= pivo] #cria array(desordenado) com elementos menores que o pivot 
        maiores = [i for i in array[1:] if i > pivo] #cria array(desordenado) com elementos maiores que o pivot 
        "chama a funcao recursivamente para os menores que o pivot(ordenando o subarray) + pivot + chama a funcao recursivamente para os maiores que o pivot(ordenando o subarray)"
        return quicksort(menores) + [pivo] + quicksort(maiores)
print(quicksort([10, 5, 2, 3]))

"A estratégia DC funciona por meio da divisão do problema em problemas menores. Se você estiver utilizando DC em uma lista, o caso-base provavelmente será um array vazio ou um array com apenas um elemento."
"A constante, na notação Big O, pode ser relevante em alguns casos. Esta é a razão pela qual o quicksort é mais rápido do que o merge sort."



"recursao com soma em array"
def soma(arr):
    if arr == []:
        return 0
    else:
        return arr[0] + soma(arr[1:])   #return arr.pop(0) + soma(arr[1:])
print(soma([1,4,10,8,5]))

"uma função recursiva que conta o número de itens em uma lista"
def counter(arr):
    if arr == []:
        return 0
    return 1 + counter(arr[1:])   
print(counter([1,4,10,8,5]))

"Encontrar o valor mais alto em uma lista"
def maximo(lista):
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    return lista[0] if lista[0] > maximo(lista[1:]) else maximo(lista[1:])
print(maximo([1,4,10,8,5]))
