from fastapi import APIRouter
from services.diary import DiaryService
from prisma.partials import DiaryRequest, DiaryResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response
from typing import List
from fastapi import status

router = APIRouter(prefix="/diaries", tags=['Diário'])
diaryService = DiaryService()

@router.get("/all")
def list_diaries() -> List[DiaryResponse]:
    response = diaryService.get_all()
		
    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

@router.post("/create")
def insert_diary(request: DiaryRequest) -> DiaryResponse:
    try:
        response = diaryService.create(request.dict())
            
        return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_201_CREATED)
    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)

@router.put("/{id}/modify")
def change_diary(id: str, request: DiaryRequest) -> DiaryResponse:
    try:
        response = diaryService.change(id, request.dict())
            
        return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)
    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)

@router.delete("/remove")
def remove_diary(id: str):
    try:
        response = diaryService.remove(id)
        
        if not response:
            return JSONResponse(content={"details": "Não foi encontrado um diário com o id especificado"}, status_code=status.HTTP_404_NOT_FOUND)
        
        return Response(content=None, status_code=status.HTTP_204_NO_CONTENT)
    except Exception as error:
        return JSONResponse(content=jsonable_encoder(error), status_code=status.HTTP_400_BAD_REQUEST)