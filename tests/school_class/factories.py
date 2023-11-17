from faker import Faker
import random


fake = Faker('pt_BR')
shift = [
    'Morning', 
    'Afternoon',
    'Night'
]

class SchoolClassFactory:

    def __init__(self, courseId):
        self.referencePeriod = random.randint(1, 8)
        self.shift = shift[random.randint(0, 2)]
        self.courseId = courseId

    def dict(self):
        return {
            "referencePeriod": self.referencePeriod,
            "shift": self.shift,
            "courseId": self.courseId
        }