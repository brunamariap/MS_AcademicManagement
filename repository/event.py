from prisma.models import Event
from prisma.partials import EventRequest


class EventRepository:

    def __init__(self):
        self.repository = Event

    def create(self, request: EventRequest):
        return self.repository.prisma().create(request)

    def get_all(self):
        return self.repository.prisma().find_many()

    def get_by_id(self, id: str):
        return self.repository.prisma().find_unique({'id': id})

    def change(self, id: str, request: EventRequest):
        return self.repository.prisma().update(data=request, where={'id': id})

    def remove(self, id: str):
        return self.repository.prisma().delete({'id': id})
