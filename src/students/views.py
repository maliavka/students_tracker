from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from students.models import Student
from students.models import Group
from students.forms import StudentAddForm, GroupAddForm


def generate_student(request):
    student = Student.generate_student()
    return HttpResponse(f'{student.get_info()}')


def students(request):
    queryset = Student.objects.all()
    response = ''

    print("request.GET.get('first_name')")
    fn = request.GET.get('first_name')
    if fn:
        # __contains LIKE %{}%
        # queryset = queryset.filter(first_name__contains=fn)

        # __endswith LIKE %{}
        # queryset = queryset.filter(first_name__endswith=fn)

        # __startswith LIKE {}%
        queryset = queryset.filter(first_name__istartswith=fn)

    for student in queryset:
        response += student.get_info() + '<br>'
    print('queryset.query')
    print(queryset.query)
    return render(request,
                  'students_list.html',
                  context={'students_list': response})


def generate_group(request):
    group = Group.generate_group()
    return HttpResponse(f'{group.get_info_group()}')


def groups(request):
    queryset = Group.objects.all()
    response = ''
    print("request.GET.get('curator')")
    cur = request.GET.get('curator')
    if cur:
        # __contains LIKE %{}%
        queryset = queryset.filter(curator__contains=cur)

    for group in queryset:
        response += group.get_info_group() + '<br>'
    print('queryset.query')
    print(queryset.query)
    return render(request, 'groups_list.html',
                  context={'groups_list': response})


def students_add(request):

    if request.method == 'POST':
        form = StudentAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')
    else:
        form = StudentAddForm()

    return render(request, 'students_add.html', context={'form': form})


def groups_add(request):

    if request.method == 'POST':
        form = GroupAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')
    else:
        form = GroupAddForm()

    return render(request, 'groups_add.html', context={'form': form})
