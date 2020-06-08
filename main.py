import random


def fib(value, array, index):
    fibonachi = [1, 2]
    indices_fib = [0]
    for i in range(len(array)):
        fibonachi.append(fibonachi[-2] + fibonachi[-1])
        if fibonachi[i - indices_fib[-1]] - 1 < len(array):
            if value == array[fibonachi[i - indices_fib[-1]] - 1]:
                index += fibonachi[i - indices_fib[-1]] - 1
                print('index = ' + str(index))
                break
            elif value > array[fibonachi[i - indices_fib[-1]] - 1]:
                continue
            elif value < array[fibonachi[i - indices_fib[-1]] - 1]:
                array = array[fibonachi[i - 1 - indices_fib[-1]]:fibonachi[i]]
                index += fibonachi[i - 1 - indices_fib[-1]]
                indices_fib.append(i)
        else:
            array = array[fibonachi[i - 1 - indices_fib[-1]]::]
            index += fibonachi[i - 1 - indices_fib[-1]]
            fib(value, array, index)


def mergeSort(list):
    if len(list) > 1:
        mid = len(list) // 2
        lefthalf = list[:mid]
        righthalf = list[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                list[k] = lefthalf[i]
                i = i + 1
            else:
                list[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            list[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            list[k] = righthalf[j]
            j = j + 1
            k = k + 1


class Array:
    def __init__(self, length):
        self.length = length
        self.array = list()

    def generate_array(self):
        l = 0
        while l != self.length:
            i = random.randrange(self.length * 10)
            if i not in self.array:
                self.array.append(i)
                l += 1

    def fib(self, value, index):
        fibonachi = [1, 2]
        indices_fib = [0]
        for i in range(len(self.array)):
            fibonachi.append(fibonachi[-2] + fibonachi[-1])
            if fibonachi[i - indices_fib[-1]] - 1 < len(self.array):
                if value == self.array[fibonachi[i - indices_fib[-1]] - 1]:
                    index += fibonachi[i - indices_fib[-1]] - 1
                    print('index = ' + str(index))
                    break
                elif value > self.array[fibonachi[i - indices_fib[-1]] - 1]:
                    continue
                elif value < self.array[fibonachi[i - indices_fib[-1]] - 1]:
                    self.array = self.array[fibonachi[i - 1 - indices_fib[-1]]:fibonachi[i]]
                    index += fibonachi[i - 1 - indices_fib[-1]]
                    indices_fib.append(i)
            else:
                self.array = self.array[fibonachi[i - 1 - indices_fib[-1]]::]
                index += fibonachi[i - 1 - indices_fib[-1]]
                fib(value, self.array, index)

    def mergeSort(self):
        if len(self.array) > 1:
            mid = len(self.array) // 2
            lefthalf = self.array[:mid]
            righthalf = self.array[mid:]

            mergeSort(lefthalf)
            mergeSort(righthalf)

            i = 0
            j = 0
            k = 0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    self.array[k] = lefthalf[i]
                    i = i + 1
                else:
                    self.array[k] = righthalf[j]
                    j = j + 1
                k = k + 1

            while i < len(lefthalf):
                self.array[k] = lefthalf[i]
                i = i + 1
                k = k + 1

            while j < len(righthalf):
                self.array[k] = righthalf[j]
                j = j + 1
                k = k + 1
