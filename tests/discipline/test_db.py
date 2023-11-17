from fastapi.testclient import TestClient
from services.course import CourseService
from services.discipline import DisciplineService
from .test_base import TestBase
from ..course.factories import CourseFactory
from .factories import DisciplineFactory
from main import app


client = TestClient(app)
course_service = CourseService()
discipline_service = DisciplineService()

class TestDatabase(TestBase):

    def test_insert_discipline(self, setUp):
        course_factory = CourseFactory()

        course = course_service.create(course_factory.dict())
        course_id = course.id

        discipline_factory =DisciplineFactory(course_id)

        discipline = discipline_service.create(discipline_factory.dict())

        assert discipline.name == discipline_factory.name

    def test_get_by_id(self, setUp):
        course_factory = CourseFactory()

        course = course_service.create(course_factory.dict())
        course_id = course.id

        discipline_factory =DisciplineFactory(course_id)

        discipline = discipline_service.create(discipline_factory.dict())
        object_id = discipline.id

        discipline = discipline_service.get_by_id(object_id)

        assert discipline.id == object_id

    def test_update_discipline(self, setUp):
        course_factory = CourseFactory()

        course = course_service.create(course_factory.dict())
        course_id = course.id

        discipline = DisciplineFactory(course_id)

        discipline = discipline_service.create(discipline.dict())
        object_id = discipline.id

        edited_discipline = DisciplineFactory(course_id)

        discipline = discipline_service.change(object_id, edited_discipline.dict())

        assert discipline.id == object_id

    def test_delete_discipline(self, setUp):
        course_factory = CourseFactory()

        course = course_service.create(course_factory.dict())
        course_id = course.id

        discipline = DisciplineFactory(course_id)

        discipline = discipline_service.create(discipline.dict())
        object_id = discipline.id

        discipline = discipline_service.remove(object_id)

        assert discipline
