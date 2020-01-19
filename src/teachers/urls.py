from django.urls import path


from teachers.views import (
    generate_teacher,
    teachers,
    teachers_add,
    teachers_edit
)


urlpatterns = [
    path('generate_teacher/', generate_teacher, name='gen-teacher'),
    path('teachers_list/', teachers, name='teachers'),
    path('teachers_add/', teachers_add, name='teachers-add'),
    path('teachers_edit/<int:pk>/', teachers_edit, name='teachers-edit'),
]
