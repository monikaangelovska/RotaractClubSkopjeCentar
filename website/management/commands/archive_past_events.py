from django.core.management.base import BaseCommand
from website.models import UpcomingEvents, EventProject
from django.utils import timezone

class Command(BaseCommand):
    help = "Moves past events(events whose date is less than today) to EventProject and deletes them from UpcomingEvents."

    def handle(self, *args, **kwargs):
        # Get all past events
        past_events = UpcomingEvents.objects.filter(date__lt=timezone.now())

        for event in past_events:
            # Create a new record in EventProject with event data
            EventProject.objects.create(
                name=event.name,
                description=event.description,
                date=event.date,
                location=event.Location
            )
            # Delete the event from UpcomingEvents
            event.delete()

        self.stdout.write(self.style.SUCCESS('Successfully archived past events.'))
