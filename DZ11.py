# Задача 1. Постройте график функции𝑓(𝑥)=5𝑥^2+10𝑥−30
# По графику определите, при каких значения x значение функции отрицательно.

import matplotlib.pyplot as plt
import numpy as np

def zadacha1():
    
    x_list = []
    y_list = []

    for x in range(-10, 11):
        y = 5 * x * x + 10 * x - 30
        x_list.append(x)
        y_list.append(y)
        
    plt.axhline(y = 0, color = 'r', linestyle = '--')
    plt.plot(y_list)
    plt.show()

# Задача 2. Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость квадратного 
# метра меньше 50000 рублей. Предоставьте ему графические данные 
# о стоимости квадратного метра каждого дома и список подходящих 
# ему домов, отсортированных по площади. Данные о домах сформируйте
# случайным образом. Площади от 100 до 300 кв. метров, цены от 3 до 20 млн.

def zadacha2():
    
    size = 15
    houses = np.random.randint(100, 300, size)
    prices = np.random.randint(3000000, 20000000, size)
    kv_pr = [prices[i]/houses[i] for i in range(len(prices))]
    print(kv_pr)
    h_numbers = ['№1',
                 '№2',
                 '№3',
                 '№4',
                 '№5',
                 '№6',
                 '№7',
                 '№8',
                 '№9',
                 '№10',
                 '№11',
                 '№12',
                 '№13',
                 '№14',
                 '№15']
    
    plt.axhline(y = 50000, color = 'b', linestyle = '--')
    plt.bar(h_numbers, kv_pr, width = 0.8)
    plt.show()
    
zadacha2()
