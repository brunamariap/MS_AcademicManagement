from repository.diary import DiaryRepository
from prisma.partials import DiaryRequest


class DiaryService:

    def __init__(self):
        self.service = DiaryRepository()

    def create(self, request: DiaryRequest):
        return self.service.create(request)

    def get_all(self):
        return self.service.get_all()

    def get_by_id(self, id: str):
        return self.service.get_by_id(id)

    def change(self, id: str, request: DiaryRequest):
        return self.service.change(id, request)

    def remove(self, id: str):
        return self.service.remove(id)
