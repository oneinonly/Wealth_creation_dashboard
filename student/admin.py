from django.contrib import admin
from student.models import Student,teachers, facalty

# Register your models here.

class studentAdmin(admin.ModelAdmin):
    list_display=("id", "name", "city", "email", "age",)
    search_fields = ("name","id", "city",)
    list_filter = ("city","name",)

admin.site.register(Student, studentAdmin)

class teachersAdmin(admin.ModelAdmin):
    list_display=("id", "name", "subject", "email", "age",)
    search_fields = ("name","id", "subject",)
    list_filter = ("id", "subject","name",)
    
admin.site.register(teachers, teachersAdmin)

class facaltyAdmin(admin.ModelAdmin):
    list_display=("id", "name", "subject", "email", "age", "photo",)
    search_fields = ("name","id", "subject",)
    list_filter = ("id", "subject","name",)

admin.site.register(facalty, facaltyAdmin)