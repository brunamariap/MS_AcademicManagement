from services.school_class import SchoolClassService
from fastapi.testclient import TestClient
from services.course import CourseService
from ..course.factories import CourseFactory
from .factories import SchoolClassFactory
from .test_base import TestBase
from main import app


client = TestClient(app)
course_service = CourseService()
class_service = SchoolClassService()

class TestDatabase(TestBase):

    def test_insert_class(self, setUp):
        course_factory = CourseFactory()

        course = course_service.create(course_factory.dict())
        course_id = course.id

        school_class = SchoolClassFactory(course_id)

        response = class_service.create(school_class.dict())

        assert response

    def test_get_by_id(self, setUp):
        course_factory = CourseFactory()

        course = course_service.create(course_factory.dict())
        course_id = course.id

        school_class = SchoolClassFactory(course_id)

        school_class = class_service.create(school_class.dict())
        object_id = school_class.id

        school_class = class_service.get_by_id(object_id)

        assert school_class.id == object_id

    def test_update_class(self, setUp):
        course_factory = CourseFactory()

        course = course_service.create(course_factory.dict())
        course_id = course.id

        school_class = SchoolClassFactory(course_id)

        school_class = class_service.create(school_class.dict())
        object_id = school_class.id

        edited_school_class = SchoolClassFactory(course_id)

        response = class_service.change(object_id, edited_school_class.dict())

        assert response.id == object_id

    def test_delete_class(self, setUp):
        course_factory = CourseFactory()

        course = course_service.create(course_factory.dict())
        course_id = course.id

        class_factory = SchoolClassFactory(course_id)

        school_class = class_service.create(class_factory.dict())
        object_id = school_class.id

        school_class = class_service.remove(object_id)

        assert school_class
