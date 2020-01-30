from django.http import HttpResponse, \
    HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse

from teachers.models import Teacher
from teachers.forms import TeacherAddForm


def generate_teacher(request):
    teacher = Teacher.generate_teacher()
    return HttpResponse(f'{teacher.get_info()}')


def teachers(request):
    queryset = Teacher.objects.all()
    info = request.GET.get('info')
    if info:
        queryset = queryset.filter(
            Q(first_name__contains=info) |
            Q(last_name__contains=info) |
            Q(email__contains=info))

    return render(request,
                  'teachers_list.html',
                  context={'teachers': queryset})


def teachers_add(request):

    if request.method == 'POST':
        form = TeacherAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers'))
    else:
        form = TeacherAddForm()

    return render(request, 'teachers_add.html', context={'form': form})


def teachers_edit(request, pk):

    try:
        teacher = Teacher.objects.get(id=pk)
    except Teacher.DoesNotExist:
        return HttpResponseNotFound(f'Teacher with id {pk} does not exist')

    if request.method == 'POST':
        form = TeacherAddForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers'))
    else:
        form = TeacherAddForm(instance=teacher)

    return render(request, 'teachers_edit.html', context={'form': form, 'pk': pk})
