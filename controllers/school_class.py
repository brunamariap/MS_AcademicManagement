from fastapi import APIRouter
from services.school_class import SchoolClassService   
from prisma.partials import SchoolClassRequest, SchoolClassResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response
from typing import List
from fastapi import status

router = APIRouter(prefix="/classes", tags=['Turma'])
class_service = SchoolClassService()

@router.get("/all")
async def list_classes() -> List[SchoolClassResponse]:
    response = await class_service.get_all()

    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

@router.get("/{id}/details")
async def get_class(id: str) -> List[SchoolClassResponse]:
    response = await class_service.get_by_id(id)
    if not response:
        return JSONResponse(content={"details": "Não foi encontrada turma com o id especificado"}, status_code=status.HTTP_404_NOT_FOUND)
		
    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

@router.post("/create")
async def insert_class(request: SchoolClassRequest) -> SchoolClassResponse:
    response = await class_service.create(request.dict())

    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_201_CREATED)

@router.put("/{id}/modify")
async def change_class(id: str, request: SchoolClassRequest) -> SchoolClassResponse:
    response = await class_service.change(id, request.dict())

    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

@router.delete("/remove")
async def remove_class(id: str) -> SchoolClassResponse:
    response = await class_service.remove(id)
    
    if not response:
        return JSONResponse(content={"details": "Não foi encontrado uma turma com o id especificado"}, status_code=status.HTTP_404_NOT_FOUND)
    
    return Response(content=None, status_code=status.HTTP_204_NO_CONTENT)