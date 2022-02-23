# Создать класс Pet в котором будет реализован метод возвращающий имя животного
# Создать класс Cat который наследуется от Pet
# Добавить функцию которая печатает в консоль “Мяу”
# Создать класс Dog который наследуется от Pet
# Добавить функцию которая печатает в консоль “Гав”
class Pet:
    def __init__(self, name):
        self.name = name


class Cat(Pet):
    def cat_meow(self):
        return 'Мяу'


class Dog(Pet):
    def dog_bark(self):
        return 'Гав'


cat_pet = Cat('Рич')
dog_pet = Dog('Рэм')
print(f'Имя кота: {cat_pet.name}.')
print(f'Имя собаки: {dog_pet.name}.')
print(f'Кот говорит: {cat_pet.cat_meow()}.')
print(f'Собака говорит: {dog_pet.dog_bark()}.')