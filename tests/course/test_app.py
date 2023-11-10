# from fastapi.encoders import jsonable_encoder
# from fastapi.testclient import TestClient
# from prisma.partials import CourseRequest
# from .test_base import TestBase
# from main import app

# client = TestClient(app)
# prefix = "/courses"


# class TestApp(TestBase):

#     def test_get_all_courses(self, setUp):
#         response = client.get(f"{prefix}/all")

#         assert response.status_code == 200

#     def test_create_course(self, setUp):
#         course = {
#             "name": "Informática",
#             "byname": "Info",
#             "periodsQuantity": 4,
#             "degree": "Ensino técnico"
#         }
#         request = CourseRequest(**course)

#         response = client.post(
#             f"{prefix}/create", json=jsonable_encoder(request))

#         assert response.status_code == 201
#         # assert response.json() == course

#     def test_edit_course(self, setUp):
#         course = {
#             "name": "Informática",
#             "byname": "Info",
#             "periodsQuantity": 4,
#             "degree": "Ensino técnico"
#         }

#         edited_course = {
#             "name": "Alimentos",
#             "byname": "Ali",
#             "periodsQuantity": 4,
#             "degree": "Ensino técnico"
#         }

#         request = CourseRequest(**course)
#         response_create_course = client.post(
#             f"{prefix}/create", json=jsonable_encoder(request))
#         course_res = response_create_course.json()
#         course_id = course_res["id"]

#         request = CourseRequest(**edited_course)
#         response = client.put(
#             f"{prefix}/{course_id}/modify", json=jsonable_encoder(request))
        
#         assert response.status_code == 200

#     def test_delete_course(self, setUp):
#         course = {
#             "name": "Informática",
#             "byname": "Info",
#             "periodsQuantity": 4,
#             "degree": "Ensino técnico"
#         }

#         request = CourseRequest(**course)
#         response_create_course = client.post(
#             f"{prefix}/create", json=jsonable_encoder(request))
#         course_res = response_create_course.json()
#         course_id = course_res["id"]

#         response = client.delete(
#             f"{prefix}/remove", params={"id": course_id})
        
#         assert response.status_code == 204
