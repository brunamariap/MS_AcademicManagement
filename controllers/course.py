from fastapi import APIRouter
from services.course import CourseService   
from prisma.partials import CourseRequest, CourseResponse, DisciplineResponse, SchoolClassResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response
from typing import List
from fastapi import status

router = APIRouter(prefix="/courses", tags=['Curso'])
course_service = CourseService()

@router.get("/all")
async def list_courses() -> List[CourseResponse]:
    response = await course_service.get_all()

    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

@router.get("/{id}/details")
async def get_course(id: str) -> List[CourseResponse]:
    response = await course_service.get_by_id(id)
    if not response:
        return JSONResponse(content={"details": "Não foi encontrado curso com o id especificado"}, status_code=status.HTTP_404_NOT_FOUND)
		
    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

@router.get("/{id}/disciplines")
async def get_course_disciplines(id: str) -> List[DisciplineResponse]:
    response = await course_service.get_disciplines(id)
    if not response:
        return JSONResponse(content={"details": "Não foi encontrada nenhuma disciplina para esse curso com o id específicado"}, status_code=status.HTTP_404_NOT_FOUND)
    
    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

@router.get("/{id}/classes")
async def get_course_classes(id: str) -> List[SchoolClassResponse]:
    response = await course_service.get_classes(id)
    if not response:
        return JSONResponse(content={"details": "Não foi encontrada nenhuma turma para esse curso com o id específicado"}, status_code=status.HTTP_404_NOT_FOUND)
    
    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

@router.post("/create")
async def insert_course(request: CourseRequest) -> CourseResponse:
    response = await course_service.create(request.dict())

    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_201_CREATED)

@router.put("/{id}/modify")
async def change_course(id: str, request: CourseRequest) -> CourseResponse:
    response = await course_service.change(id, request.dict())

    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

@router.delete("/remove")
async def remove_course(id: str) -> CourseResponse:
    response = await course_service.remove(id)
    
    if not response:
        return JSONResponse(content={"details": "Não foi encontrado um curso com o id especificado"}, status_code=status.HTTP_404_NOT_FOUND)
    
    return Response(content=None, status_code=status.HTTP_204_NO_CONTENT)