from fastapi.testclient import TestClient
from services.course import CourseService
from .factories import CourseFactory
from .test_base import TestBase
from main import app


client = TestClient(app)
service = CourseService()

class TestDatabase(TestBase):

    def test_insert_course(self, setUp):
        factory = CourseFactory()

        course = service.create(factory.dict())
        assert course

    def test_get_by_id(self, setUp):
        factory = CourseFactory()

        course = service.create(factory.dict())
        object_id = course.id

        response = service.get_by_id(object_id)

        assert response.id == object_id

    def test_update_course(self, setUp):
        factory = CourseFactory()

        course = service.create(factory.dict())
        object_id = course.id

        edited_course = CourseFactory()

        response = service.change(object_id, edited_course.dict())

        assert response.id == object_id

    def test_delete_course(self, setUp):
        factory = CourseFactory()

        course = service.create(factory.dict())
        object_id = course.id

        response = service.remove(object_id)

        assert response
