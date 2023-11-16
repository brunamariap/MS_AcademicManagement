from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from prisma.partials import DiaryRequest
from .test_base import TestBase
from main import app
import datetime

client = TestClient(app)
prefix = "/diaries"


class TestApp(TestBase):

    def test_get_all_diaries(self, setUp):
        response = client.get(f"{prefix}/all")

        assert response.status_code == 200

    def test_create_diary(self, setUp):
        day = datetime.datetime.utcnow().isoformat() + 'Z'
        diary = {
            "referencePeriod": 2,
            "referenceYear": 2023,
            "startDate": day,
            "endDate": day
        }
        request = DiaryRequest(**diary)

        response = client.post(
            f"{prefix}/create", json=jsonable_encoder(request))
        print(response)
        assert response.status_code == 201
        # assert response.json() == diary

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

        request = DiaryRequest(**diary)
        response_create_diary = client.post(
            f"{prefix}/create", json=jsonable_encoder(request))
        diary_res = response_create_diary.json()
        diary_id = diary_res["id"]

        request = DiaryRequest(**edited_diary)
        response = client.put(
            f"{prefix}/{diary_id}/modify", json=jsonable_encoder(request))
        
        assert response.status_code == 200

    def test_delete_diary(self, setUp):
        day = datetime.datetime.utcnow().isoformat() + 'Z'
        diary = {
            "referencePeriod": 2,
            "referenceYear": 2023,
            "startDate": day,
            "endDate": day
        }

        request = DiaryRequest(**diary)
        response_create_diary = client.post(
            f"{prefix}/create", json=jsonable_encoder(request))
        diary_res = response_create_diary.json()
        diary_id = diary_res["id"]
        print(diary_id)

        response = client.delete(
            f"{prefix}/remove", params={"id": diary_id})
        
        assert response.status_code == 204
