from services.diary import DiaryService
from .factories import DiaryFactory
from .test_base import TestBase
import datetime


diaryService = DiaryService()

class TestApp(TestBase):

    def test_get_all_diaries(self, setUp):
        response = diaryService.get_all()

        assert len(response) >= 0

    def test_create_diary(self, setUp):
        factory = DiaryFactory()

        diary = diaryService.create(factory.dict())
        
        assert diary.referencePeriod == factory.referencePeriod
        assert diary.referenceYear == factory.referenceYear

    def test_edit_diary(self, setUp):
        factory = DiaryFactory()

        diary = diaryService.create(factory.dict())
        diary_id = diary.id
        
        edited_diary = DiaryFactory()
        
        response = diaryService.change(diary_id, edited_diary.dict())
        
        assert response

    def test_delete_diary(self, setUp):
        factory = DiaryFactory()
        
        diary = diaryService.create(factory.dict())
        diary_id = diary.id

        response = diaryService.remove(diary_id)
        
        assert response
