from timeit import default_timer as timer
from random import randint

def insertionSort(list):
    for j in range(1,len(list)):
        key = list[j]

        i = j-1

        while (i > -1) and key < list[i]:
            list[i+1]=list[i]
            i=i-1

        list[i+1] = key

    return list

if __name__== "__main__":

    x = []

    for y in range(11):
        x.append(randint(0, 100))

    print("input list:", x)

    start = timer()
    insertionSort(x)
    end = timer()

    print("sorted list:",  x)
    print("sort executon time:", end - start)