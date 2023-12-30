from repository.discipline import DisciplineRepository
from prisma.partials import DisciplineRequest


class DisciplineService:

    def __init__(self):
        self.repository = DisciplineRepository()

    def create(self, request: DisciplineRequest):
        return self.repository.create(request)

    def get_all(self):
        return self.repository.get_all()
    
    def get_discipline(self, id: str):
        return self.repository.get_by_id(id)
    
    def get_discipline_with_details(self, id: str):
        return self.repository.get_by_id_with_details(id)
    
    def list_by_course(self, courseId: str):
        pass
    
    def change(self, id: str, request: DisciplineRequest):
        return self.repository.change(id, request)
    
    def remove(self, id: str):
        return self.repository.remove(id)