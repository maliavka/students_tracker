from django.http import HttpResponse, \
    HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse

from students.models import Student
from students.models import Group
from students.forms import StudentAddForm, GroupAddForm, ContactForm


def generate_student(request):
    student = Student.generate_student()
    return HttpResponse(f'{student.get_info()}')


def students(request):
    queryset = Student.objects.all().select_related('st_group')
    fn = request.GET.get('first_name')
    if fn:
        queryset = queryset.filter(first_name__contains=fn)

    print('VIEW STUDENTS')

    return render(request,
                  'students_list.html',
                  context={'students': queryset})


def generate_group(request):
    group = Group.generate_group()
    return HttpResponse(f'{group.get_info_group()}')


def groups(request):
    queryset = Group.objects.all().select_related('curator', 'headman')
    cur = request.GET.get('curator')
    if cur:
        # __contains LIKE %{}%
        queryset = queryset.filter(curator__contains=cur)
    return render(request, 'groups_list.html',
                  context={'groups': queryset})


def students_add(request):

    if request.method == 'POST':
        form = StudentAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentAddForm()

    return render(request, 'students_add.html', context={'form': form})


def students_edit(request, pk):

    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return HttpResponseNotFound(f'Students with id {pk} does not exist')

    if request.method == 'POST':
        form = StudentAddForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentAddForm(instance=student)

    return render(request, 'students_edit.html', context={'form': form, 'pk': pk})


def groups_add(request):

    if request.method == 'POST':
        form = GroupAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups'))
    else:
        form = GroupAddForm()

    return render(request, 'groups_add.html', context={'form': form})


def groups_edit(request, pk):

    try:
        group = Group.objects.get(id=pk)
    except Group.DoesNotExist:
        return HttpResponseNotFound(f'Group with id {pk} does not exist')

    if request.method == 'POST':
        form = GroupAddForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups'))
    else:
        form = GroupAddForm(instance=group)

    return render(request, 'groups_edit.html', context={'form': form, 'pk': pk})


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('text')
            with open('logs.txt', 'a') as f:

                f.write(f'{email}: {subject} ("{message}")\n')
            return HttpResponseRedirect(reverse('students'))
    else:
        form = ContactForm()

    return render(request, 'contact.html', context={'form': form})
