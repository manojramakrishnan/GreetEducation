from django.contrib import admin
from .models import StudentExtra


class StudentExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(StudentExtra,StudentExtraAdmin)

# Register your models here.
