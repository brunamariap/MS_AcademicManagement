from prisma.models import Course
from prisma.partials import CourseRequest


class CourseRepository:
    def __init__(self):
        pass

    def create(self, request: CourseRequest):
        return Course.prisma().create(request)

    def get_all(self):
        return Course.prisma().find_many()

    def get_by_id(self, id: str):
        return Course.prisma().find_unique({'id': id})

    def change(self, id: str, request: CourseRequest):
        return Course.prisma().update(data=request, where={'id': id})
    
    def remove(self, id: str):
        return Course.prisma().delete({'id': id})
