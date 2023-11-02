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
async def list_disciplines() -> List[DisciplineResponse]:
    response = await discipline_service.get_all()

    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

@router.get("/{id}/details")
async def get_discipline(id: str) -> List[DisciplineResponse]:
    response = await discipline_service.get_by_id(id)
    if not response:
        return JSONResponse(content={"details": "Não foi encontrada disciplina com o id especificado"}, status_code=status.HTTP_404_NOT_FOUND)
		
    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

@router.post("/create")
async def insert_discipline(request: DisciplineRequest) -> DisciplineResponse:
    response = await discipline_service.create(request.dict())

    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_201_CREATED)

@router.put("/{id}/modify")
async def change_discipline(id: str, request: DisciplineRequest) -> DisciplineResponse:
    response = await discipline_service.change(id, request.dict())

    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

@router.delete("/remove")
async def remove_discipline(id: str) -> DisciplineResponse:
    response = await discipline_service.remove(id)
    
    if not response:
        return JSONResponse(content={"details": "Não foi encontrado uma disciplina com o id especificado"}, status_code=status.HTTP_404_NOT_FOUND)
    
    return Response(content=None, status_code=status.HTTP_204_NO_CONTENT)