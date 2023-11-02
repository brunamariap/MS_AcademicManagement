from repository.course import CourseRepository
from prisma.partials import CourseRequest


class CourseService:

    def __init__(self):
        self.service = CourseRepository()

    def create(self, request: CourseRequest):
        return self.service.create(request)

    def get_all(self):
        return self.service.get_all()
    
    def get_by_id(self, id: str):
        return self.service.get_by_id(id)
    
    def get_disciplines(self, courseId: str):
        return self.service.get_disciplines(courseId)
    
    def get_classes(self, courseId: str):
        return self.service.get_classes(courseId)
    
    def change(self, id: str, request: CourseRequest):
        return self.service.change(id, request)
    
    def remove(self, id: str):
        return self.service.remove(id)