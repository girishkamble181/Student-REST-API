from django.contrib import admin
from .models import StudentModel

admin.site.register(StudentModel)
admin.site.site_header= "Girish Projects"
admin.site.index_title= "Girish Admin"