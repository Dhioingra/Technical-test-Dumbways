#variabel
data = [['a', 'c', 'b', 'e', 'd'], ['g', 'e', 'f']]
data2 = [['g', 'h','i', 'j'], ['a', 'c', 'b', 'e', 'd'], ['g', 'e', 'f']]

#quicksort function
def quicksort (data):
    if len (data) <= 1:
        return data
    
    left = []
    right = []
    pivot = data [0]

    for i in data [1:]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)
    return quicksort (left) + [pivot] + quicksort (right)

#lengt quicksort function
def quicksort_length (data):
    if len(data) <= 1:
        return data

    left = []
    right = []
    pivot = data[0]

    for i in data [1:]:
        if len(i) <= len(pivot):
            left.append(i)
        else:
            right.append(i)
    return quicksort (left) + [pivot] + quicksort(right)

#main function
def sorting (data):
    all = []
    for i in range (len(data)):
        all.append(quicksort(data[i]))
    return quicksort_length(all)

#main function called
print (sorting(data))
print (sorting(data2))