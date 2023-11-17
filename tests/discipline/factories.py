from faker import Faker
import datetime
import random


fake = Faker('pt_BR')

class DisciplineFactory:

    def __init__(self, courseId):
        self.name = fake.job()
        self.referencePeriod = random.randint(1, 8)
        self.code = 'TEC.' + str(random.randint(12000, 20000))
        self.isOptative = bool(random.randint(0, 1))
        self.courseId = courseId

    def dict(self):
        return {
            "name": self.name,
            "referencePeriod": self.referencePeriod,
            "code": self.code,
            "isOptative": self.isOptative,
            "courseId": self.courseId
        }