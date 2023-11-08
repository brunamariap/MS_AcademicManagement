from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from prisma.partials import CourseRequest, DisciplineRequest
from .test_base import TestBase
from main import app

client = TestClient(app)
prefix = "/disciplines"


class TestApp(TestBase):

    def test_get_all_disciplines(self, setUp):
        response = client.get(f"{prefix}/all")

        assert response.status_code == 200

    def test_create_discipline(self, setUp):
        course = {
            "name": "Informática",
            "byname": "Info",
            "periodsQuantity": 4,
            "degree": "Ensino técnico"
        }
        request = CourseRequest(**course)

        response_create_course = client.post(
            "/courses/create", json=jsonable_encoder(request))
        
        course_res = response_create_course.json()
        course_id = course_res["id"]

        discipline = {
            "name": "Redes de computadores",
            "referencePeriod": 3,
            "code": "TEC.1234",
            "isOptative": True,
            "courseId": course_id
        }

        request = DisciplineRequest(**discipline)

        response = client.post(f"{prefix}/create", json=jsonable_encoder(request))

        assert response.status_code == 201

    def test_edit_discipline(self, setUp):
        course = {
            "name": "Informática",
            "byname": "Info",
            "periodsQuantity": 4,
            "degree": "Ensino técnico"
        }

        request = CourseRequest(**course)
        response_create_course = client.post(
            "/courses/create", json=jsonable_encoder(request))
        course_res = response_create_course.json()
        course_id = course_res["id"]
        
        discipline = {
            "name": "Redes de computadores",
            "referencePeriod": 3,
            "code": "TEC.1234",
            "isOptative": True,
            "courseId": course_id
        }

        edited_discipline = {
            "name": "Teste de software",
            "referencePeriod": 3,
            "code": "TEC.345",
            "isOptative": True,
            "courseId": course_id
        }

        request = DisciplineRequest(**discipline)

        response_create_discipline = client.post(f"{prefix}/create", json=jsonable_encoder(request))
        discipline_res = response_create_discipline.json()
        discipline_id = discipline_res["id"]

        request = DisciplineRequest(**edited_discipline)
        response = client.put(
            f"{prefix}/{discipline_id}/modify", json=jsonable_encoder(request))
        
        assert response.status_code == 200

    def test_delete_discipline(self, setUp):
        course = {
            "name": "Informática",
            "byname": "Info",
            "periodsQuantity": 4,
            "degree": "Ensino técnico"
        }

        request = CourseRequest(**course)
        response_create_course = client.post(
            "/courses/create", json=jsonable_encoder(request))
        course_res = response_create_course.json()
        course_id = course_res["id"]
        
        discipline = {
            "name": "Redes de computadores",
            "referencePeriod": 3,
            "code": "TEC.1234",
            "isOptative": True,
            "courseId": course_id
        }

        request = DisciplineRequest(**discipline)
        response_create_discipline = client.post(f"{prefix}/create", json=jsonable_encoder(request))
        discipline_res = response_create_discipline.json()
        discipline_id = discipline_res["id"]

        response = client.delete(
            f"{prefix}/remove", params={"id": discipline_id})
        
        assert response.status_code == 204
