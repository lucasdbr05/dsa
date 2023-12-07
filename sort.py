from random import sample

def merge(arr, inicio=0, meio=None, fim=None):
    if fim == None:
        fim =len(arr)
        meio = fim//2
    left = arr[inicio:meio]
    right = arr[meio:fim]
    l_index = 0
    r_index = 0
    for i in range(inicio, fim):
        if l_index >=len(left):
            arr[i]= right[r_index]
            r_index+= 1
        elif r_index >=len(right):
            arr[i]= left[l_index]
            l_index+= 1
        elif left[l_index]<= right[r_index]:
            arr[i]= left[l_index]
            l_index+= 1
        elif right[r_index]<= left[l_index]:
            arr[i]= right[r_index]
            r_index+= 1
    return arr


def merge_sort(arr, inicio=0, fim = None):
    if fim == None:
        fim = len(arr)
    if (fim-inicio)>1:
        meio = (fim+inicio)//2
        merge_sort(arr, inicio, meio)
        merge_sort(arr, meio, fim)
        return merge(arr, inicio, meio, fim)


def quick_sort(arr):
    if len(arr)<=1: 
        return arr
    pivot = arr[0]
    left = [i for i in arr[1:] if i<=pivot]
    right = [i for i in arr[1:] if i>pivot]
    return quick_sort(left)+ [pivot] + quick_sort(right)


lista = sample(range(0,100), 100)
merge_sort(lista)
print(lista)

lista = sample(range(0,100), 100)
print(quick_sort(lista))
