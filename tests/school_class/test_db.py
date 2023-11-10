from fastapi.testclient import TestClient
from services.course import CourseService
from services.school_class import SchoolClassService
from .test_base import TestBase
from main import app


client = TestClient(app)
course_service = CourseService()
class_service = SchoolClassService()

class TestDatabase(TestBase):

    def test_insert_class(self, setUp):
        course = {
            'name': 'Informática',
            'byname': 'Info',
            'periodsQuantity': 4,
            'degree': 'Ensino técnico',
        }

        response = course_service.create(course)
        course_id = response.id

        school_class = {
            "referencePeriod": 2,
            "shift": "Morning",
            "courseId": course_id
        }

        response = class_service.create(school_class)

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

        school_class = {
            "referencePeriod": 2,
            "shift": "Morning",
            "courseId": course_id
        }

        response = class_service.create(school_class)
        object_id = response.id

        response = class_service.get_by_id(object_id)

        assert response.id == object_id

    def test_update_class(self, setUp):
        course = {
            'name': 'Informática',
            'byname': 'Info',
            'periodsQuantity': 4,
            'degree': 'Ensino técnico',
        }

        response = course_service.create(course)
        course_id = response.id

        school_class = {
            "referencePeriod": 2,
            "shift": "Morning",
            "courseId": course_id
        }

        response = class_service.create(school_class)
        object_id = response.id

        edited_school_class = {
            "referencePeriod": 3,
            "shift": "Night",
            "courseId": course_id
        }

        response = class_service.change(object_id, edited_school_class)

        assert response.id == object_id

    def test_delete_class(self, setUp):
        course = {
            'name': 'Informática',
            'byname': 'Info',
            'periodsQuantity': 4,
            'degree': 'Ensino técnico',
        }

        response = course_service.create(course)
        course_id = response.id

        school_class = {
            "referencePeriod": 2,
            "shift": "Morning",
            "courseId": course_id
        }

        response = class_service.create(school_class)
        object_id = response.id

        response = class_service.remove(object_id)

        assert response
