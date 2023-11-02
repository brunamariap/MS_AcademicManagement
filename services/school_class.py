from repository.school_class import SchoolClassRepository
from prisma.partials import SchoolClassRequest


class SchoolClassService:

    def __init__(self):
        self.service = SchoolClassRepository()

    def create(self, request: SchoolClassRequest):
        return self.service.create(request)

    def get_all(self):
        return self.service.get_all()
    
    def get_by_id(self, id: str):
        return self.service.get_by_id(id)
    
    def change(self, id: str, request: SchoolClassRequest):
        return self.service.change(id, request)
    
    def remove(self, id: str):
        return self.service.remove(id)