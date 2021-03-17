class Cat:
    def __init__(self, name, breed, gender, age):
        self.name = name
        self.breed = breed
        self.gender = gender
        self.age = age

    def get_name(self):
        return self.name

    def get_breed(self):
        return self.breed

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age

    def get_all(self):
        print(f'Кот на сайте "Дом питомца": имя - {self.get_name()}, порода - {self.get_breed()}, '
              f'пол - {self.get_gender()}, возраст - {self.get_age()} года.')
