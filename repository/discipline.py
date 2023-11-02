from prisma.models import Discipline
from prisma.partials import DisciplineRequest


class DisciplineRepository:
    def __init__(self):
        pass

    def create(self, request: DisciplineRequest):
        return Discipline.prisma().create(request)

    def get_all(self):
        return Discipline.prisma().find_many()

    def get_by_id(self, id: str):
        pass

    def change(self, id: str, request: DisciplineRequest):
        return Discipline.prisma().update(data=request, where={'id': id})
    
    def remove(self, id: str):
        return Discipline.prisma().delete({'id': id})
