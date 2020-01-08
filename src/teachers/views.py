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

    print("request.GET.get('first_name')")
    print(request.GET)
    info = request.GET.get('last_name')
    # ln = request.GET.get('last_name')
    # em = request.GET.get('email')
    if info:
        # __contains LIKE %{}%
        queryset = queryset.filter(last_name__contains=info)
        # queryset = queryset.filter(Q(first_name__contains=info) | Q(last_name__contains=info) | Q(email__contains=info))

        # __endswith LIKE %{}
        # queryset = queryset.filter(first_name__endswith=fn)

        # __startswith LIKE {}%
        # queryset = queryset.filter(first_name__startswith=fn)

    for teacher in queryset:
        response += teacher.get_info() + '<br>'
    print('queryset.query')
    print(queryset.query)
    return render(request,
                  'teachers_list.html',
                  context={'teachers_list': response})
