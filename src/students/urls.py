from django.urls import path


from students.views import (
    generate_student,
    students,
    students_add,
    students_edit,
    contact, register, custom_login
)
from students.views import (
    generate_group,
    groups,
    groups_add,
    groups_edit
)
urlpatterns = [
    path('generate_student/', generate_student, name='gen-student'),
    path('students_list/', students, name='students'),
    path('students_add/', students_add, name='students-add'),
    path('students_edit/<int:pk>/', students_edit, name='students-edit'),
    path('contact/', contact, name='contact'),
    path('register/', register, name='register'),
    path('login/', custom_login, name='login'),

    path('generate_group/', generate_group, name='gen-group'),
    path('groups_list/', groups, name='groups'),
    path('groups_add/', groups_add, name='groups-add'),
    path('groups_edit/<int:pk>/', groups_edit, name='groups-edit'),
]
