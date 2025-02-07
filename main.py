import matplotlib.pyplot as plt
import numpy as np
from sympy import diff, symbols, sympify
from math import cos, log, sin, log10, pow, log2, tan


def value_func(math_func, x):
    return eval(math_func.replace('x', str(x)))


def find_x(math_func, elem, epsilon, maximum_iter, step):
    iterations = 0
    start = elem
    finish = elem + step
    middle = (start + finish) / 2
    while iterations < maximum_iter and epsilon < abs(value_func(math_func, middle)):
        val_num1 = value_func(math_func, start)
        val_num2 = value_func(math_func, finish)
        val_midle = value_func(math_func, middle)
        if val_midle * val_num1 > 0:
            start = middle
        elif val_midle * val_num2 > 0:
            finish = middle
        else:
            break
        middle = (start + finish) / 2
        iterations += 1
    flag = 'OK'
    if iterations >= maximum_iter:
        return '-', '-', iterations, 'Iterations error'
    else:
        return middle, value_func(math_func, middle), iterations, 'OK'


def find_mas_x(math_func, start, finish, step, epsilon, maximum_iter):
        res_arr = []
        for iteration in range(len(np.arange(start, finish, step))):
            elem = start + step * iteration
            x, f_x, iter_out, flag = find_x(math_func, elem, epsilon, maximum_iter, step)
            result_x = [f'{elem} : {elem + step}', x, f_x, iter_out, flag],
            res_arr.append(result_x)
        return res_arr


def createSchedule(math_func, start, finish, step, res_arr):
    sch_x = np.arange(-20, 20, 0.1)
    sch_y = []
    try:
        for i in sch_x:
            sch_y.append(eval(math_func.replace('x', str(i))))
        plt.plot(sch_x, sch_y)
    except ValueError:
        return 'Error'

    x = list(np.arange(start, finish + 1, step))
    y = []
    for i in x:
        y.append(eval(math_func.replace('x', str(i))))

    for i in range(len(res_arr)):
        item1 = res_arr[i][0][1]
        item2 = res_arr[i][0][2]
        if item1 != '-' and item2 != '-':
            plt.scatter(item1, item2, color='orange', s=40, marker='o')

    x_sym = symbols('x')
    expr = sympify(math_func)
    for i in range(len(x)):
        item1 = diff(expr, x_sym)
        val1 = item1.subs(x_sym, x[i])
        item2 = diff(item1, x_sym)
        val2 = item2.subs(x_sym, x[i])
        if abs(val1) < 0.1:
            plt.scatter(x[i], y[i], color='orange', s=40, marker='o')
        if abs(val2) < 0.1:
            plt.scatter(x[i], y[i], color='orange', s=40, marker='o')

    line = plt.gca()
    line.axhline(y=0, color='k')
    line.axvline(x=0, color='k')
    plt.show()

#
# if __name__ == '__main__':
#     createSchedule()
