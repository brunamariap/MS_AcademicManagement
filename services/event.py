from repository.event import EventRepository
from prisma.partials import EventRequest


class EventService:

    def __init__(self):
        self.service = EventRepository()

    def create(self, request: EventRequest):
        return self.service.create(request)

    def get_all(self):
        return self.service.get_all()
    
    def get_by_id(self, id: str):
        return self.service.get_by_id(id)
    
    def change(self, id: str, request: EventRequest):
        return self.service.change(id, request)
    
    def remove(self, id: str):
        return self.service.remove(id)