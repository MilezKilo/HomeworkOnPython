import math
import time

#Декоратор
def myDecorator(myFunction):
        print('Вызвана функция: {}'.format(myFunction.__name__)) #Выводит в консоль название вызванной функции
        myFunction() #Вызов функции
        print('затраченное время: %s' % time.perf_counter()) #Выводит в консоль затраченное время

#Найти площадь участка. Создайте программу, запрашиваемого у пользователя длину и ширину садового участка в футах. Выведите на экран площадь участка в акрах
def areaCalculation():
    print('Введите длину и ширину:')
    lenght = int(input())
    width = int(input())
    temporary = lenght * width
    SQFT_PER_ACRE = temporary / 43560
    print("Результат =", SQFT_PER_ACRE, "акров")

def freeFall(accseleration = 9.8):
    print('Введите дистанцию:')
    distance = int(input())
    Vf = math.sqrt(2 * (accseleration * distance))
    print('Скорость объекта при его соприкосновении с землей: ', Vf)
    
myDecorator(areaCalculation)
myDecorator(freeFall)