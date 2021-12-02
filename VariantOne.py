import math
import time

#Декоратор
def myDecorator(myFunction):
    def wrapperFunc():
        startTime = time.time()
        print('Вызвана функция: {}'.format(myFunction.__name__),'.') #Выводит в консоль название вызванной функции
        myFunction() #Вызов функции
        endTime = time.time()
        print('Затраченное время: %s секунды' % (endTime - startTime)) #Выводит в консоль затраченное время
    return wrapperFunc

#Найти площадь участка. Создайте программу, запрашиваемого у пользователя длину и ширину садового участка в футах. Выведите на экран площадь участка в акрах
@myDecorator
def areaCalculation():
    print('Введите длину и ширину:')
    lenght = int(input())
    width = int(input())
    temporary = lenght * width
    SQFT_PER_ACRE = temporary / 43560
    print("Результат =", SQFT_PER_ACRE, "акров")

@myDecorator
def freeFall(accseleration = 9.8):
    print('Введите дистанцию:')
    distance = int(input())
    Vf = math.sqrt(2 * (accseleration * distance))
    print('Скорость объекта при его соприкосновении с землей: ', Vf)

areaCalculation()
print('----------------------------')
freeFall()