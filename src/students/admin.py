from django.contrib import admin

from students.models import Student, Group
from teachers.models import Teacher
from students.forms import StudentAdminForm


class GroupInline(admin.TabularInline):
    model = Group


class StudentAdmin(admin.ModelAdmin):
    # readonly_fields = ('email',)
    list_display = ('id', 'first_name', 'last_name', 'email', 'telephone', 'st_group')
    list_select_related = ('st_group',)
    list_per_page = 10
    form = StudentAdminForm

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)

        if request.user.groups.filter(name='manager').exists():
            return readonly_fields + ('telephone',)
        return readonly_fields

    def has_delete_permission(self, request, obj=None):
        return False


class StudentAdminInline(admin.TabularInline):
    model = Student
    readonly_fields = ('email',)
    show_change_link = True


class TeacherAdminInline(admin.TabularInline):
    model = Teacher


class GroupAdmin(admin.ModelAdmin):
    readonly_fields = ('group_name',)
    list_display = ('group_name', 'curator', 'headman', 'start_date')
    list_select_related = ('curator', 'headman',)
    list_per_page = 10
    inlines = [TeacherAdminInline, ]
    inlines = [StudentAdminInline, ]

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)

        if request.user.groups.filter(name='manager').exists():
            return readonly_fields + ('start_date',)
        return readonly_fields


admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)