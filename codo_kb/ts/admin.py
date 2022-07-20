from django.contrib import admin
from .models import TsRecord, Project

# Register your models here.

class TsRecordsAdmin(admin.ModelAdmin):
    list_display = ('person', 'date', 'project', 'activity', 'fact_hours', 'payment_date')
    list_filter = ('person', 'project',)
    list_editable = ('payment_date',)
    search_fields = ('activity',)

admin.site.register(Project)
admin.site.register(TsRecord, TsRecordsAdmin)

