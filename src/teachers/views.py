from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q

from teachers.models import Teacher


def generate_teacher(request):
    teacher = Teacher.generate_teacher()
    return HttpResponse(f'{teacher.get_info()}')


def teachers(request):
    queryset = Teacher.objects.all()
    response = ''
    print("request.GET.get('info')")
    print(request.GET)
    info = request.GET.get('info')

    if info:
        queryset = queryset.filter(Q(first_name__contains=info) | Q(last_name__contains=info) | Q(email__contains=info))

    for teacher in queryset:
        response += teacher.get_info() + '<br>'
    print('queryset.query')
    print(queryset.query)
    return render(request,
                  'teachers_list.html',
                  context={'teachers_list': response})
