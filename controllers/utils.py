from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response
from typing import List
from fastapi import status
from services.utils import UtilsService

router = APIRouter(prefix="/utils", tags=['Utilidades'])
utilsService = UtilsService()

@router.get("/count")
def list_diaries():
    response = utilsService.get_resources_count()
		
    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)
