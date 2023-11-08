from fastapi import APIRouter
from services.event import EventService   
from prisma.partials import EventRequest, EventResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response
from typing import List
from fastapi import status

router = APIRouter(prefix="/events", tags=['Evento'])
event_service = EventService()

@router.get("/all")
def list_events() -> List[EventResponse]:
    response = event_service.get_all()

    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

@router.get("/{id}/details")
def get_event(id: str) -> List[EventResponse]:
    response = event_service.get_by_id(id)
    if not response:
        return JSONResponse(content={"details": "Não foi encontrado evento com o id especificado"}, status_code=status.HTTP_404_NOT_FOUND)
		
    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

@router.post("/create")
def insert_event(request: EventRequest) -> EventResponse:
    response = event_service.create(request.dict())

    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_201_CREATED)

@router.put("/{id}/modify")
def change_event(id: str, request: EventRequest) -> EventResponse:
    response = event_service.change(id, request.dict())

    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

@router.delete("/remove")
def remove_event(id: str) -> EventResponse:
    response = event_service.remove(id)
    
    if not response:
        return JSONResponse(content={"details": "Não foi encontrado um evento com o id especificado"}, status_code=status.HTTP_404_NOT_FOUND)
    
    return Response(content=None, status_code=status.HTTP_204_NO_CONTENT)