from fastapi import APIRouter
from services.discipline import DisciplineService   
from prisma.partials import DisciplineRequest, DisciplineResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response
from typing import List
from fastapi import status

router = APIRouter(prefix="/disciplines", tags=['Disciplina'])
discipline_service = DisciplineService()

@router.get("/all")
def list_disciplines() -> List[DisciplineResponse]:
    response = discipline_service.get_all()

    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

@router.get("/{id}")
def get_discipline(id: str) -> List[DisciplineResponse]:
    try:
        response = discipline_service.get_discipline(id)
        if not response:
            return JSONResponse(content={"details": "Não foi encontrada disciplina com o id especificado"}, status_code=status.HTTP_404_NOT_FOUND)
            
        return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)
    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)

@router.get("/{id}/details")
def get_discipline_details(id: str) -> List[DisciplineResponse]:
    try:
        response = discipline_service.get_discipline_with_details(id)
        if not response:
            return JSONResponse(content={"details": "Não foi encontrada disciplina com o id especificado"}, status_code=status.HTTP_404_NOT_FOUND)
            
        return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)
    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)

@router.post("/create")
def insert_discipline(request: DisciplineRequest) -> DisciplineResponse:
    try:
        response = discipline_service.create(request.dict())

        return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_201_CREATED)
    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)

@router.put("/{id}/modify")
def change_discipline(id: str, request: DisciplineRequest) -> DisciplineResponse:
    try:
        response = discipline_service.change(id, request.dict())

        return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)
    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)

@router.delete("/remove")
def remove_discipline(id: str) -> DisciplineResponse:
    try:
        response = discipline_service.remove(id)
        
        if not response:
            return JSONResponse(content={"details": "Não foi encontrado uma disciplina com o id especificado"}, status_code=status.HTTP_404_NOT_FOUND)
        
        return Response(content=None, status_code=status.HTTP_204_NO_CONTENT)
    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)
