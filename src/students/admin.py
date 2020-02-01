from django.contrib import admin

from students.models import Student


class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ('email', 'telephone')
    list_display = ('id', 'first_name', 'last_name', 'email', 'st_group')
    list_select_related = ('st_group',)
    list_per_page = 10


admin.site.register(Student, StudentAdmin)
