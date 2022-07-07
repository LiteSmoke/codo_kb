from django.contrib import admin
from .models import Video, Tag, TagType

# Register your models here.

# class VideoAdmin(admin.ModelAdmin):

#     list_display = ('filename', 'filepath', 'meeting_name', 'meeting_date', 'participants', 'tags')
#     list_display_links = ('filename')

admin.site.register(Video)
admin.site.register(Tag)
admin.site.register(TagType)