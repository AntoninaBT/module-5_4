# Teplova
class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        args = args[0]
        cls.houses_history.append(args)
        return instance

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f'Название:{self.name}, кол-во этажей: {self.number_of_floors}'

    def __del__(self):
        return print(f'{self.name} снесён, но он останется в истории')




h1 = House('ЖК Горский', 35)
print(House.houses_history)
h2 = House('Домик в деревне', 2)
print(House.houses_history)
h3 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h4 = House('ЖК Акация', 20)
print(House.houses_history)
h5 = House('ЖК Матрёшки', 20)
print(House.houses_history)
# delete an object
del h3
del h5
print(House.houses_history)

