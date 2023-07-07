from django.contrib import admin
from .models import StudentExtra
from .models import TeacherExtra


class StudentExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(StudentExtra,StudentExtraAdmin)

# Register your models here.
class TeacherExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(TeacherExtra,TeacherExtraAdmin)