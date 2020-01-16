class Car:
    # Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
    # Поля должны задаваться через конструктор
    def __init__(self, brand, model):
        self.brand = str(brand)
        self.model = str(model)

    def __repr__(self):
        return ' '.join([self.brand, self.model])

class Garage:
    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # Реализовать методы add и delete(удалять по индексу) машин из гаража
    def __init__(self, cars):
        self.cars = cars

    def __getitem__(self, position):
        return self.cars[position]

    def __add__(self, other):
        # Check that we can add Car in list
        if not isinstance(self.cars, list):
            self.cars = list(self.cars)
        # Check that we add Car
        assert isinstance(other, Car), print('Need Car class to add in %s' % self.__class__.__name__)
        # Add Car in Garage
        self.cars.append(other)

    def __delete__(self, position):
        try:
            del self.cars[position]
        except IndexError:
            print('No Car on position {}'.format(position))


if __name__ == '__main__':
    cars = [Car('BMW', 3), Car('Lada', '10')]
    garage = Garage(cars)
    garage.__add__(Car('Oka', 0))
    garage.__delete__(3)
    for c in garage:
        print(c)
    garage.__add__(Car('Oka', 1))

