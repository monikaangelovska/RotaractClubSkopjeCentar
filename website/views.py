from django.shortcuts import render, get_object_or_404, redirect
from .models import EventProject, Image, MembersInfo, UpcomingEvents, FormApplicant
import base64
from datetime import datetime, timedelta
from django.contrib import messages
from django.core.paginator import Paginator

def count_meetings(start_date, end_date):
    meeting_count = 0
    current_date = start_date

    while current_date <= end_date:
        if current_date.weekday() == 1:
            if not (current_date.month == 6 and current_date.day > 15) and not (current_date.month == 9 and current_date.day < 15):
                meeting_count += 1
        current_date += timedelta(days=1)

    return meeting_count


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('v_message')

        FormApplicant.objects.create(name=name, email=email, message=message)

        messages.success(request, "Your application has been submitted successfully!")

        return redirect('index')

    latest_projects = EventProject.objects.order_by('-start_date')[:2]
    images = Image.objects.all()
    project_data = []

    for project in latest_projects:
        encoded_image = None
        for image in images:
            if image.project_id.id == project.id:
                encoded_image = base64.b64encode(image.image_data).decode('utf-8')
                break

        project_data.append({'project': project, 'encoded_image': encoded_image})

    project_count = EventProject.objects.count()
    people_involved_count = 100
    meetings_held_count = count_meetings(datetime(2014, 4, 2), datetime.now())

    return render(request, 'index.html', {
        'project_data': project_data,
        'project_count': project_count,
        'people_involved_count': people_involved_count,
        'meetings_held_count': meetings_held_count,
    })

def past_projects(request):
    past_projects = EventProject.objects.all()
    images = Image.objects.all()

    query = request.GET.get('q', None)
    selected_year = request.GET.get('year', None)
    
    if query:
        past_projects = past_projects.filter(name__icontains=query)

    if selected_year:
        try:
            selected_year = int(selected_year)
            past_projects = past_projects.filter(start_date__year=selected_year)
        except ValueError:
            pass

    past_projects = past_projects.order_by('-start_date')  

    paginator = Paginator(past_projects, 7) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    project_data = []
    for project in page_obj:
        encoded_image = None
        for image in images:
            if image.project_id.id == project.id: 
                encoded_image = base64.b64encode(image.image_data).decode('utf-8')
                break

        project_data.append({'project': project, 'encoded_image': encoded_image})

    return render(request, 'past_projects.html', {'project_data': project_data, 'page_obj': page_obj})

def project_detail(request, id):
    latest_projects = EventProject.objects.order_by('-start_date')[:2]
    project_data = []
    
    project = get_object_or_404(EventProject, id=id)

    images = Image.objects.filter(project_id=project).order_by('id')

    for proj in latest_projects:
        encoded_image = None
        associated_images = Image.objects.filter(project_id=proj).first()
        if associated_images:
            encoded_image = base64.b64encode(associated_images.image_data).decode('utf-8')
        
        project_data.append({'project': proj, 'encoded_image': encoded_image})

    if images:
        first_image = base64.b64encode(images[0].image_data).decode('utf-8')
        additional_images = [
            base64.b64encode(image.image_data).decode('utf-8') for image in images[1:]
        ]
    else:
        first_image = None
        additional_images = []

    context = {
        'project': project,
        'first_image': first_image,
        'additional_images': additional_images,
        'project_data': project_data
    }
    return render(request, 'project_detail.html', context)

def about_us(request):
    members = MembersInfo.objects.all()
    member_data = []

    for member in members:
        encoded_image = None
        if member.members_images.exists():
            encoded_image = base64.b64encode(member.members_images.first().Image).decode('utf-8')
        
        member_data.append({
            'member': member,
            'encoded_image': encoded_image,
        })
    
    return render(request, 'about_us.html', {'member_data': member_data})

def upcoming_events(request):
    events = UpcomingEvents.objects.all().order_by('date')
    return render(request, 'upcoming_events.html', {'events': events})

