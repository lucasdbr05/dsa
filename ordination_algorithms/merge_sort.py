from random import sample

# def merge(lista, inicio=0, meio=None, fim=None):
#     if fim==None:
#         fim=len(lista)
#         meio = fim//2
#     left = lista[inicio:meio]
#     right = lista[meio:fim]
#     left_index = 0
#     right_index = 0
#     for i in range(inicio, fim):
#         if left_index>= len(left):
#             lista[i]= right[right_index]
#             right_index+= 1
#         elif right_index>= len(right):
#             lista[i]= left[left_index]
#             left_index+= 1
#         elif left[left_index]<=right[right_index]:
#             lista[i]= left[left_index]
#             left_index+=1
#         elif right[right_index]<left[left_index]:
#             lista[i]= right[right_index]
#             right_index+=1
#     return lista


# def merge_sort(lista, inicio=0, fim=None):
#     if fim == None:
#         fim=len(lista)
#     if (fim-inicio>1):
#         meio = (inicio+fim)//2
#         merge_sort(lista, inicio, meio)
#         merge_sort(lista, meio, fim)
#         return merge(lista, inicio, meio, fim)
    











def merge(arr, inicio=0, meio =None, fim=None):
    if (fim is None):
        fim= len(arr)
        meio = (fim+inicio)//2

    left = arr[inicio:meio]
    right = arr[meio:fim]
    l, r= 0,0
    for k in range(inicio, fim):
        if(l>= len(left)):
            arr[k]= right[r]
            r+= 1
        elif(r>= len(right)):
            arr[k]= left[l]
            l+= 1
        elif left[l]<=right[r]:
            arr[k]= left[l]
            l+=1
        elif right[r]< left[l]:
            arr[k]= right[r]
            r+=1
    return arr





def merge_sort(arr, inicio=0, fim=None):
    if(fim is None):
        fim = len(arr)
    
    if (fim- inicio>1):
        meio = (fim+inicio)//2
        merge_sort(arr, inicio, meio)
        merge_sort(arr, meio, fim)
        return merge(arr)

lista = sample(range(0,100), 100)
print(lista)
merge_sort(lista)
print(lista)