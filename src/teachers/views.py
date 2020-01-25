from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q

from teachers.models import Teacher
from teachers.forms import TeacherAddForm


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
        queryset = queryset.filter(
            Q(first_name__contains=info) |
            Q(last_name__contains=info) |
            Q(email__contains=info))

    for teacher in queryset:
        response += teacher.get_info() + '<br>'

    return render(request,
                  'teachers_list.html',
                  context={'teachers_list': response})


def teachers_add(request):

    if request.method == 'POST':
        form = TeacherAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/')
    else:
        form = TeacherAddForm()

    return render(request, 'teachers_add.html', context={'form': form})
