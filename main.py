# Необходимо дополнить класс House следующими специальными методами:
# __len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
# __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".

class House:
    def __init__(self, name: str, numberOfFloors: int):

        self.name: str = name
        self.numberOfFloors: int = numberOfFloors

    def goto(self, floor: int):
        if floor < 1 or floor > self.numberOfFloors:
            print('Такого этажа не существует')
        else:
            [print(x) for x in range(1, floor + 1)]

    def __len__(self):
        return self.numberOfFloors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.numberOfFloors}'


sweatyHome = House('sweatyHome', 19)
sweatyHome.goto(6)
print(sweatyHome.__len__())
print(sweatyHome.__str__())