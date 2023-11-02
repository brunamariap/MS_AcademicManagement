from repository.discipline import DisciplineRepository
from prisma.partials import DisciplineRequest


class DisciplineService:

    def __init__(self):
        self.service = DisciplineRepository()

    def create(self, request: DisciplineRequest):
        return self.service.create(request)

    def get_all(self):
        return self.service.get_all()
    
    def get_by_id(self, id: str):
        return self.service.get_by_id(id)
    
    def change(self, id: str, request: DisciplineRequest):
        return self.service.change(id, request)
    
    def remove(self, id: str):
        return self.service.remove(id)