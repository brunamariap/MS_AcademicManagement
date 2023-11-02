from prisma.models import SchoolClass
from prisma.partials import SchoolClassRequest


class SchoolClassRepository:
    def __init__(self):
        pass

    def create(self, request: SchoolClassRequest):
        return SchoolClass.prisma().create(request)

    def get_all(self):
        return SchoolClass.prisma().find_many()

    def get_by_id(self, id: str):
        pass

    def change(self, id: str, request: SchoolClassRequest):
        return SchoolClass.prisma().update(data=request, where={'id': id})
    
    def remove(self, id: str):
        return SchoolClass.prisma().delete({'id': id})
