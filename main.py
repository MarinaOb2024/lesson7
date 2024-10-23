#1. Создайте базовый класс `Animal`, который будет содержать
# общие атрибуты (например, `name`, `age`)
# и методы (`make_sound()`, `eat()`) для всех животных.
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} издает звук.")

    def eat(self):
        print(f"{self.name} ест.")
#2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`. Добавьте специфические атрибуты и
# переопределите методы, если требуется (например, различный звук для
# `make_sound()`). 3. Продемонстрируйте полиморфизм: создайте функцию
# `animal_sound(animals)`, которая принимает список животных и
# вызывает метод `make_sound()` для каждого животного.
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} чирикает.")

    def fly(self):
        print(f"{self.name} летит с размахом крыльев {self.wing_span} метров.")


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} рычит.")


class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        print(f"{self.name} шипит.")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

#4. Используйте композицию для создания класса `Zoo`, который будет содержать
# информацию о животных и сотрудниках. Должны быть методы для добавления животных
# и сотрудников в зоопарк.
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} добавлен в зоопарк.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"{staff_member.name} нанят в зоопарк.")

    def show_animals(self):
        for animal in self.animals:
            print(f"{animal.name}, Возраст: {animal.age}")

    def show_staff(self):
        for staff_member in self.staff:
            print(f"{staff_member.name}, Должность: {staff_member.__class__.__name__}")
#5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
# которые могут иметь специфические методы (например, `feed_animal()`
# для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")

# Создаем животных
parrot = Bird("Попугай", 3, 1.2)
tiger = Mammal("Тигр", 5, "Оранжевый")
snake = Reptile("Змея", 2, "Чешуйчатая")

# Создаем сотрудников
keeper = ZooKeeper("Алексей")
vet = Veterinarian("Ольга")

# Создаем зоопарк и добавляем туда животных и сотрудников
zoo = Zoo()
zoo.add_animal(parrot)
zoo.add_animal(tiger)
zoo.add_animal(snake)

zoo.add_staff(keeper)
zoo.add_staff(vet)

# Демонстрация животных и сотрудников
zoo.show_animals()
zoo.show_staff()

# Вызов полиморфной функции для всех животных
animal_sound([parrot, tiger, snake])

# Действия сотрудников
keeper.feed_animal(tiger)
vet.heal_animal(snake)


