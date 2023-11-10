from fastapi.testclient import TestClient
from services.course import CourseService
from .test_base import TestBase
from main import app


client = TestClient(app)
service = CourseService()

class TestDatabase(TestBase):

    def test_insert_course(self, setUp):
        course = {
            'name': 'Informática',
            'byname': 'Info',
            'periodsQuantity': 4,
            'degree': 'Ensino técnico',
        }

        response = service.create(course)
        assert response

    def test_get_by_id(self, setUp):
        course = {
            'name': 'Informática',
            'byname': 'Info',
            'periodsQuantity': 4,
            'degree': 'Ensino técnico',
        }

        response = service.create(course)
        object_id = response.id

        response = service.get_by_id(object_id)

        assert response.id == object_id

    def test_update_course(self, setUp):
        course = {
            'name': 'Informática',
            'byname': 'Info',
            'periodsQuantity': 4,
            'degree': 'Ensino técnico',
        }

        response = service.create(course)
        object_id = response.id

        edited_course = {
            'name': 'Alimentos',
            'byname': 'Ali',
            'periodsQuantity': 4,
            'degree': 'Ensino técnico',
        }

        response = service.change(object_id, edited_course)

        assert response.id == object_id

    def test_delete_course(self, setUp):
        course = {
            'name': 'Informática',
            'byname': 'Info',
            'periodsQuantity': 4,
            'degree': 'Ensino técnico',
        }

        response = service.create(course)
        object_id = response.id

        response = service.remove(object_id)

        assert response
