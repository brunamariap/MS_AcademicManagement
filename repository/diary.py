from prisma.models import Diary
from prisma.partials import DiaryRequest


class DiaryRepository:
    def create(self, request: DiaryRequest):
        return Diary.prisma().create(request)

    def get_all(self):
        return Diary.prisma().find_many()

    def get_by_id(self):
        return Diary.prisma().find_unique({'id': id})

    def change(self, id: str, request: DiaryRequest):
        return Diary.prisma().update(data=request, where={'id': id})

    def remove(self, id: str):
        return Diary.prisma().delete({'id': id})
