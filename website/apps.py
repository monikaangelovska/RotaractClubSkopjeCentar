from django.apps import AppConfig


class WebsiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'website'


# # website/apps.py
# from django.apps import AppConfig
# from django.utils import timezone
# from django.db.models.signals import post_migrate

# class WebsiteConfig(AppConfig):
#     name = 'website'

#     def ready(self):
#         # Import models here to avoid circular imports
#         from .models import UpcomingEvents, EventProject
#         self.archive_past_events()

#     def archive_past_events(self):
#         # Get all past events
#         past_events = UpcomingEvents.objects.filter(date__lt=timezone.now())

#         for event in past_events:
#             # Create a new record in EventProject with event data
#             EventProject.objects.create(
#                 name=event.name,
#                 description=event.description,
#                 date=event.date,
#                 location=event.Location
#             )
#             # Delete the event from UpcomingEvents
#             event.delete()
