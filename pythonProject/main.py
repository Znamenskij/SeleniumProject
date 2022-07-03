# Создайте класс JellyBean, расширяющий класс Dessert (изУпражнения 11) новыми геттерами и сеттерами для атрибута flavor.
# Измените метод is_delicious таким образом, чтобы он возвращал false только в тех случаях, когда flavor
# равняется «black licorice».


class Dessert():
    def __init__(self, name, calories):
        self.__name = name
        self.__calories = calories

    def is_healthy(self, name, calories):
        self.__name = name
        self.__calories = calories
        if self.__calories < 200:
            return True

    def is_delicious(self):
        return True

class JellyBean(Dessert):
    def __init__(self, name, calories, flavor):
        super(JellyBean, self).__init__(name, calories)
        self.__flavor = flavor
    def is_delicious(self, flavor):
        self.__flavor = flavor
        if self.__flavor == 'black licorice':
            return False


