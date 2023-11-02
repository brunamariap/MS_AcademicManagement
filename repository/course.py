from prisma.models import Course, Discipline, SchoolClass
from prisma.partials import CourseRequest


class CourseRepository:

    def __init__(self):
        self.repository = Course

    def create(self, request: CourseRequest):
        return self.repository.prisma().create(request)

    def get_all(self):
        return self.repository.prisma().find_many()

    def get_by_id(self, id: str):
        return self.repository.prisma().find_unique({'id': id})
    
    def get_disciplines(self, courseId: str):
        return Discipline.prisma().find_many(where={'courseId': courseId})
    
    def get_classes(self, courseId: str):
        return SchoolClass.prisma().find_many(where={'courseId': courseId})

    def change(self, id: str, request: CourseRequest):
        return self.repository.prisma().update(data=request, where={'id': id})
    
    def remove(self, id: str):
        return self.repository.prisma().delete({'id': id})
