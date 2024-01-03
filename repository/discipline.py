from prisma.models import Discipline
from prisma.partials import DisciplineRequest


class DisciplineRepository:

    def __init__(self):
        self.repository = Discipline

    def create(self, request: DisciplineRequest):
        return self.repository.prisma().create(request)

    def get_all(self):
        return self.repository.prisma().find_many(include={'course': True})

    def get_by_id(self, id: str):
        return self.repository.prisma().find_unique({'id': id })
    
    def get_by_id_with_details(self, id: str):
        return self.repository.prisma().find_unique({'id': id}, include={'course': True})

    def change(self, id: str, request: DisciplineRequest):
        return self.repository.prisma().update(data=request, where={'id': id})

    def remove(self, id: str):
        return self.repository.prisma().delete({'id': id})

    def count(self):
        return self.repository.prisma().count()
    
    def get_class_disciplines(self, course_id: str, period: str):
        return self.repository.prisma().find_many(where={
            'courseId': course_id,
            'referencePeriod': period
        })
    
    def get_course_disciplines(self, course_id: str):
        return self.repository.prisma().find_many(where={
            'courseId': course_id,
        })