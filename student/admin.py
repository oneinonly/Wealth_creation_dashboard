from django.contrib import admin
from student.models import Student,teachers, facalty, registration

# Register your models here.

class studentAdmin(admin.ModelAdmin):
    list_display=("id", "name", "city", "email", "age", "education", "address", "bloodgroub", "photo")
    search_fields = ("name","id", "city",)
    list_filter = ("id" ,"city","name",)

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

class registrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email','mobile', 'password',)
    search_fields = ('id', 'name', 'email','mobile',)
    list_fields = ('id', 'name', 'email','mobile',)
    
admin.site.register(registration, registrationAdmin)