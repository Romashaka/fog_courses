"""
5. Написать функцию avaranger, которая принимает 1 аргумент - любое
число и возвращается среднее арифметическое значение, на основании
текущего числа и предыдущих, которые были введены ранее.
Например
>>> avaranger(10) # Среднее арифметическое 10
>>> 10
>>> avaranger(11) # Среднее арифметическое 10 и 11
>>> 10.5
>>> avaranger(12) # Среднее арифметическое 10, 11 и 12
>>> 11

"""
import statistics
a = []
def avaranger(n):
    a.append(n)
    return statistics.mean(a)


res = [avaranger(int (i)) for i in input().split(' ')]
print (' '.join([str(i) for i in res]))
