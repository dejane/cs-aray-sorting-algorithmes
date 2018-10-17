from timeit import default_timer as timer
from random import randint

def quickSort(list):

  quickSortHelper(list,0,len(list)-1)

def quickSortHelper(list,first,last):

  if first<last:
      splitpoint = partition(list,first,last)
      quickSortHelper(list,first,splitpoint-1)
      quickSortHelper(list,splitpoint+1,last)

def partition(list,first,last):

  pivot = list[first]
  left = first+1
  right = last
  done = False

  while not done:
      while left <= right and list[left] <= pivot:
          left = left + 1

      while list[right] >= pivot and right >= left:
          right = right -1

      if right < left:
          done = True
      else:
          temp = list[left]
          list[left] = list[right]
          list[right] = temp

  temp = list[first]
  list[first] = list[right]
  list[right] = temp

  return right

if __name__== "__main__":

    x = []

    for y in range(10000):
        x.append(  (randint(100,10000)**(randint(100,10000))) )

    print("input list:",x)

    start = timer()
    quickSort(x)
    end = timer()

    print("sorted list:",  x)
    print("sort executon time:", end - start)