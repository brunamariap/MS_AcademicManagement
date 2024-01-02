from services.school_class import SchoolClassRepository
from services.course import CourseRepository
from services.discipline import DisciplineRepository
from services.diary import DiaryRepository

schoolClassRepository = SchoolClassRepository()
courseRepository = CourseRepository()
disciplineRepository = DisciplineRepository()
diaryRepository = DiaryRepository()

class UtilsService:

    def get_resources_count(self):
        classes_count = schoolClassRepository.count()
        courses_count = courseRepository.count()
        disciplines_count = disciplineRepository.count()
        diaries_count = diaryRepository.count()

        return {
            "classes": classes_count,
            "courses": courses_count,
            "disciplines": disciplines_count,
            "diaries":diaries_count
        }