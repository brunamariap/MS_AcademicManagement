# from fastapi.encoders import jsonable_encoder
# from fastapi.testclient import TestClient
# from prisma.partials import CourseRequest, SchoolClassRequest
# from .test_base import TestBase
# from main import app

# client = TestClient(app)
# prefix = "/classes"


# class TestApp(TestBase):

#     def test_get_all_classes(self, setUp):
#         response = client.get(f"{prefix}/all")

#         assert response.status_code == 200

#     def test_create_class(self, setUp):
#         course = {
#             "name": "Informática",
#             "byname": "Info",
#             "periodsQuantity": 4,
#             "degree": "Ensino técnico"
#         }
#         request = CourseRequest(**course)

#         response_create_course = client.post(
#             "/courses/create", json=jsonable_encoder(request))
        
#         course_res = response_create_course.json()
#         course_id = course_res["id"]

#         school_class = {
#             "referencePeriod": 2,
#             "shift": "Morning",
#             "courseId": course_id
#         }

#         request = SchoolClassRequest(**school_class)

#         response = client.post(f"{prefix}/create", json=jsonable_encoder(request))

#         assert response.status_code == 201

#     def test_edit_class(self, setUp):
#         course = {
#             "name": "Informática",
#             "byname": "Info",
#             "periodsQuantity": 4,
#             "degree": "Ensino técnico"
#         }

#         request = CourseRequest(**course)
#         response_create_course = client.post(
#             "/courses/create", json=jsonable_encoder(request))
#         course_res = response_create_course.json()
#         course_id = course_res["id"]
        
#         school_class = {
#             "referencePeriod": 2,
#             "shift": "Morning",
#             "courseId": course_id
#         }

#         edited_school_class = {
#             "referencePeriod": 3,
#             "shift": "Night",
#             "courseId": course_id
#         }

#         request = SchoolClassRequest(**school_class)

#         response_create_school_class = client.post(f"{prefix}/create", json=jsonable_encoder(request))
#         school_class_res = response_create_school_class.json()
#         school_class_id = school_class_res["id"]

#         request = SchoolClassRequest(**edited_school_class)
#         response = client.put(
#             f"{prefix}/{school_class_id}/modify", json=jsonable_encoder(request))
        
#         assert response.status_code == 200

#     def test_delete_class(self, setUp):
#         course = {
#             "name": "Informática",
#             "byname": "Info",
#             "periodsQuantity": 4,
#             "degree": "Ensino técnico"
#         }

#         request = CourseRequest(**course)
#         response_create_course = client.post(
#             "/courses/create", json=jsonable_encoder(request))
#         course_res = response_create_course.json()
#         course_id = course_res["id"]
        
#         school_class = {
#             "referencePeriod": 2,
#             "shift": "Morning",
#             "courseId": course_id
#         }

#         request = SchoolClassRequest(**school_class)
#         response_create_school_class = client.post(f"{prefix}/create", json=jsonable_encoder(request))
#         school_class_res = response_create_school_class.json()
#         school_class_id = school_class_res["id"]

#         response = client.delete(
#             f"{prefix}/remove", params={"id": school_class_id})
        
#         assert response.status_code == 204
