from random import randint

class Potion:
    def __init__(self, name, quality):
        self.__name = name
        self.__quality = quality
        self.check_quality()
    
    def __str__(self):
        return (f'Название зелья - {self.__name}, качество зелья - {self.__quality}') 

    def get_quality(self):
        return self.__quality

    def get_name(self):
        return self.__name

    def set_quality(self, new_quality):
        if type(new_quality) == int:
            self.__quality = new_quality
        else:
            new_quality = (input('Вы ввели неправильно, введите число:'))
            if new_quality.isdigit():
                new_quality = int(new_quality)
            self.set_quality(new_quality)

    def set_name(self, new_name):
        if type(new_name) == str:
            self.__name = new_name
        else:
            new_name = (input('Вы ввели неправильно, введите строку:'))
            self.set_name(new_name)

    def __add__(self, other):
        new_name = self.__name + other.__name
        new_name = new_name.lower()
        new_name = new_name.title()

        new_quality = (self.__quality + other.__quality)//2
        
        obj = Potion(new_name, new_quality)
        
        return obj

    def check_quality(self):
        if self.__quality >= 50:
            print('Отличное зелье')
        else:
            print('Ваше зелье взорвалось')




    

a = Potion(input('Введите название первого зелья - '), randint(0,100))
print(a)
b = Potion(input('Введите название второго зелья - '), randint(0,100))
print(b)
print(a + b)

