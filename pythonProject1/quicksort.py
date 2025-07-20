
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
       pivo = arr[0]
       menores = [i for i in arr[1:]if i<=pivo]
       maiores = [i for i in arr[1:]if i>pivo]
       return quicksort(menores) + [pivo] + quicksort(maiores)

print (quicksort([15,25,36, 14,1,0,16]))