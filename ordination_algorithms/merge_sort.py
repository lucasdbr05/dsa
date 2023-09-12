from random import sample


def merge(lista, inicio=0, meio=None, fim=None):
    if fim==None:
        fim=len(lista)
        meio = fim//2
    left = lista[inicio:meio]
    right = lista[meio:fim]
    left_index = 0
    right_index = 0
    for i in range(inicio, fim):
        if left_index>= len(left):
            lista[i]= right[right_index]
            right_index+= 1
        elif right_index>= len(right):
            lista[i]= left[left_index]
            left_index+= 1
        elif left[left_index]<=right[right_index]:
            lista[i]= left[left_index]
            left_index+=1
        elif right[right_index]<left[left_index]:
            lista[i]= right[right_index]
            right_index+=1
    return lista


def merge_sort(lista, inicio=0, fim=None):
    if fim == None:
        fim=len(lista)
    if (fim-inicio>1):
        meio = (inicio+fim)//2
        merge_sort(lista, inicio, meio)
        merge_sort(lista, meio, fim)
        return merge(lista, inicio, meio, fim)
    

lista = sample(range(0,100), 100)
merge_sort(lista)
print(lista)