from faker import Faker
import random


fake = Faker('pt_BR')
degree = [
    "Ensino técnico",
    "Ensino superior",
]

class CourseFactory:

    def __init__(self):
        self.name = fake.job()
        self.byname = self.name[:2]
        self.periodsQuantity = random.randint(1, 8)
        self.degree = degree[random.randint(0, 1)]

    def dict(self):
        return {
            "name": self.name,
            "byname": self.byname,
            "periodsQuantity": self.periodsQuantity,
            "degree": self.degree
        }