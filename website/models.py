from django.db import models

class EventProject(models.Model):
    name = models.TextField()
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        db_table = 'EventProject'

class Image(models.Model):
    image_date = models.DateField()
    image_data = models.BinaryField()
    project_id = models.ForeignKey(EventProject, on_delete=models.CASCADE, db_column='project_id', default=1)

    class Meta:
        db_table = 'Images'

class UpcomingEvents(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)

    class Meta:
        db_table = 'UpcomingEvents'

class MembersInfo(models.Model):
    MemberID = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    Surname = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    JobDescription = models.TextField(blank=True, null=True)
    MyRotaryID = models.IntegerField(blank=True, null=True)
    ClubPosition = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'MembersInfo'

class MembersImages(models.Model):
    ImageID = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    MemberID = models.ForeignKey(MembersInfo, on_delete=models.CASCADE, db_column='MemberID', related_name='members_images')
    Image = models.BinaryField()

    class Meta:
        db_table = 'MembersImages'

class FormApplicant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        db_table = 'FormApplicant'