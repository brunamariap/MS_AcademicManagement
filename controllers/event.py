from fastapi import APIRouter
from services.event import EventService   
from prisma.partials import EventRequest, EventResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response
from typing import List
from fastapi import status
import requests

router = APIRouter(prefix="/events", tags=['Evento'])
event_service = EventService()

@router.get("/all")
def list_events() -> List[EventResponse]:
    response = event_service.get_all()

    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

@router.get("/{id}/details")
def get_event(id: str) -> List[EventResponse]:
    try:
        response = event_service.get_by_id(id)
        if not response:
            return JSONResponse(content={"details": "Não foi encontrado evento com o id especificado"}, status_code=status.HTTP_404_NOT_FOUND)
		
        return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)
    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)

@router.post("/create")
def insert_event(request: EventRequest) -> EventResponse:
    try:
        response = event_service.create(request.dict())

        return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_201_CREATED)
    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)

@router.put("/{id}/modify")
def change_event(id: str, request: EventRequest) -> EventResponse:
    try:
        response = event_service.change(id, request.dict())

        return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)
    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)

@router.delete("/remove")
def remove_event(id: str) -> EventResponse:
    try:
        response = event_service.remove(id)
        
        if not response:
            return JSONResponse(content={"details": "Não foi encontrado um evento com o id especificado"}, status_code=status.HTTP_404_NOT_FOUND)
        
        return Response(content=None, status_code=status.HTTP_204_NO_CONTENT)
    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)

@router.get("/{id}/students/all")
def get_students_participated_event(id: str):
    try:
        url = "http://127.0.0.1:8000/student/students/events/links/all"
        response = requests.get(url=url, params={'eventId': id})    

        data = {
            "message": "Falha ao tentar acessar esse recurso."
        }

        if response.status_code == 200:
            data = response.json()
            data = [obj for obj in data if obj['eventId'] == id]

            return JSONResponse(content=jsonable_encoder(data), status_code=status.HTTP_200_OK)

        return JSONResponse(content=jsonable_encoder(data), status_code=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)