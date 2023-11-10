from fastapi.testclient import TestClient
from services.course import CourseService
from services.discipline import DisciplineService
from .test_base import TestBase
from main import app


client = TestClient(app)
course_service = CourseService()
discipline_service = DisciplineService()

class TestDatabase(TestBase):

    def test_insert_discipline(self, setUp):
        course = {
            'name': 'Informática',
            'byname': 'Info',
            'periodsQuantity': 4,
            'degree': 'Ensino técnico',
        }

        response = course_service.create(course)
        course_id = response.id

        discipline = {
            "name": "Redes de computadores",
            "referencePeriod": 3,
            "code": "TEC.1234",
            "isOptative": True,
            "courseId": course_id
        }

        response = discipline_service.create(discipline)

        assert response

    def test_get_by_id(self, setUp):
        course = {
            'name': 'Informática',
            'byname': 'Info',
            'periodsQuantity': 4,
            'degree': 'Ensino técnico',
        }

        response = course_service.create(course)
        course_id = response.id

        discipline = {
            "name": "Redes de computadores",
            "referencePeriod": 3,
            "code": "TEC.1234",
            "isOptative": True,
            "courseId": course_id
        }

        response = discipline_service.create(discipline)
        object_id = response.id

        response = discipline_service.get_by_id(object_id)

        assert response.id == object_id

    def test_update_discipline(self, setUp):
        course = {
            'name': 'Informática',
            'byname': 'Info',
            'periodsQuantity': 4,
            'degree': 'Ensino técnico',
        }

        response = course_service.create(course)
        course_id = response.id

        discipline = {
            "name": "Redes de computadores",
            "referencePeriod": 3,
            "code": "TEC.1234",
            "isOptative": True,
            "courseId": course_id
        }

        response = discipline_service.create(discipline)
        object_id = response.id

        edited_discipline = {
            "name": "Teste de software",
            "referencePeriod": 3,
            "code": "TEC.345",
            "isOptative": True,
            "courseId": course_id
        }

        response = discipline_service.change(object_id, edited_discipline)

        assert response.id == object_id

    def test_delete_discipline(self, setUp):
        course = {
            'name': 'Informática',
            'byname': 'Info',
            'periodsQuantity': 4,
            'degree': 'Ensino técnico',
        }

        response = course_service.create(course)
        course_id = response.id

        discipline = {
            "name": "Redes de computadores",
            "referencePeriod": 3,
            "code": "TEC.1234",
            "isOptative": True,
            "courseId": course_id
        }

        response = discipline_service.create(discipline)
        object_id = response.id

        response = discipline_service.remove(object_id)

        assert response
