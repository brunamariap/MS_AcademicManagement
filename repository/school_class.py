from prisma.models import SchoolClass
from prisma.partials import SchoolClassRequest


class SchoolClassRepository:

    def __init__(self):
        self.repository = SchoolClass

    def create(self, request: SchoolClassRequest):
        return self.repository.prisma().create(request)

    def get_all(self):
        return self.repository.prisma().find_many(include={'course': True, 'diary': True})

    def get_by_id(self, id: str):
        return self.repository.prisma().find_unique({'id': id}, include={'course':True})

    def change(self, id: str, request: SchoolClassRequest):
        return self.repository.prisma().update(data=request, where={'id': id})
    
    def remove(self, id: str):
        return self.repository.prisma().delete({'id': id})
