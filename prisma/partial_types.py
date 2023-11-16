from prisma.models import Course, SchoolClass, Discipline, Event, Diary


Course.create_partial('CourseRequest', exclude=['id'], exclude_relational_fields=True)
Course.create_partial('CourseResponse', exclude_relational_fields=True)

SchoolClass.create_partial('SchoolClassRequest', exclude=['id'], exclude_relational_fields=True)
SchoolClass.create_partial('SchoolClassResponse', exclude_relational_fields=True)

Discipline.create_partial('DisciplineRequest', exclude=['id'], exclude_relational_fields=True)
Discipline.create_partial('DisciplineResponse', exclude_relational_fields=True)

Event.create_partial('EventRequest', exclude=['id'], exclude_relational_fields=True)
Event.create_partial('EventResponse', exclude_relational_fields=True)

Diary.create_partial('DiaryRequest', exclude=['id'], exclude_relational_fields=True)
Diary.create_partial('DiaryResponse', exclude_relational_fields=True)