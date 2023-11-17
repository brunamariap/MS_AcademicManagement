from faker import Faker
import datetime
import random


fake = Faker('pt_BR')

class DiaryFactory:

    def __init__(self):
        self.referencePeriod = random.randint(1, 2)
        self.referenceYear = random.randint(2020, 2024)
        self.startDate = datetime.datetime.utcnow().isoformat() + 'Z'
        self.endDate = datetime.datetime.utcnow().isoformat() + 'Z'

    def dict(self):
        return {
            "referencePeriod": self.referencePeriod,
            "referenceYear": self.referenceYear,
            "startDate": self.startDate,
            "endDate": self.endDate
        }