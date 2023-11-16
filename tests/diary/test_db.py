from fastapi.testclient import TestClient
from .test_base import TestBase
from main import app
from prisma.models import Diary
from prisma.partials import DiaryRequest
import datetime
from services.diary import DiaryService

client = TestClient(app)
prefix = "/diaries"


diaryService = DiaryService()

class TestApp(TestBase):

    def test_get_all_diaries(self, setUp):
        response = diaryService.get_all()

        assert len(response) >= 0

    def test_create_diary(self, setUp):
        day = datetime.datetime.utcnow().isoformat() + 'Z'
        diary = {
            "referencePeriod": 2,
            "referenceYear": 2023,
            "startDate": day,
            "endDate": day
        }

        response = diaryService.create(diary)
        
        assert response

    def test_edit_diary(self, setUp):
        day = datetime.datetime.utcnow().isoformat() + 'Z'
        diary = {
            "referencePeriod": 2,
            "referenceYear": 2023,
            "startDate": day,
            "endDate": day
        }

        edited_diary = {
            "referencePeriod": 1,
            "referenceYear": 2024,
            "startDate": day,
            "endDate": day
        }

        response_create_diary = diaryService.create(diary)
        diary_id = response_create_diary.id 
        
        response = diaryService.change(diary_id, edited_diary)
        
        assert response

    def test_delete_diary(self, setUp):
        day = datetime.datetime.utcnow().isoformat() + 'Z'
        diary = {
            "referencePeriod": 2,
            "referenceYear": 2023,
            "startDate": day,
            "endDate": day
        }
        
        response_create_diary = diaryService.create(diary)
        diary_id = response_create_diary.id

        response = diaryService.remove(diary_id)
        
        assert response
