# Generated by Django 5.0.3 on 2024-10-08 07:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='MembersInfo',
            fields=[
                ('MemberID', models.AutoField(primary_key=True, serialize=False)),
                ('Surname', models.CharField(max_length=255)),
                ('Name', models.CharField(max_length=255)),
                ('JobDescription', models.TextField(blank=True, null=True)),
                ('MyRotaryID', models.IntegerField(blank=True, null=True)),
                ('ClubPosition', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'MembersInfo',
            },
        ),
        migrations.CreateModel(
            name='UpcomingEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('location', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'UpcomingEvents',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_date', models.DateField()),
                ('image_data', models.BinaryField()),
                ('project_id', models.ForeignKey(db_column='project_id', default=1, on_delete=django.db.models.deletion.CASCADE, to='website.eventproject')),
            ],
            options={
                'db_table': 'Images',
            },
        ),
        migrations.CreateModel(
            name='MembersImages',
            fields=[
                ('ImageID', models.AutoField(primary_key=True, serialize=False)),
                ('Image', models.BinaryField()),
                ('MemberID', models.ForeignKey(db_column='MemberID', on_delete=django.db.models.deletion.CASCADE, related_name='members_images', to='website.membersinfo')),
            ],
            options={
                'db_table': 'MembersImages',
            },
        ),
    ]