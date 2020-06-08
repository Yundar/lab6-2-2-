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


class Array:
    def __init__(self, length):
        self.length = length

    def generate_array(self):
        array = list()
        while len(array) != self.length:
            i = random.randrange(self.length*10)
            if i not in array:
                array.append(i)
        array.sort()
        return array

    def fib(self, value, array, index):
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