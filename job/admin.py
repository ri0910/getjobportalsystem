from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(Job_seeker)
@admin.register(Company)
@admin.register(Job)
@admin.register(Apply)
class usrdet(ImportExportModelAdmin):
    pass
