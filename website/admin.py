from django.contrib import admin
from website.models import EventProject, Image, UpcomingEvents, MembersInfo, MembersImages

@admin.register(EventProject)
class EventProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'start_date', 'end_date']  
    search_fields = ['name']

@admin.register(Image)  
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_date', 'project_id'] 
    search_fields = ['project_id__name'] 

@admin.register(UpcomingEvents)
class UpcomingEventsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'date']
    search_fields = ['name']

admin.site.register(MembersInfo)
admin.site.register(MembersImages)