from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('past_projects/', views.past_projects, name='past_projects'),
    path('about_us/', views.about_us, name='about_us'),
    path('upcoming_events/', views.upcoming_events, name='upcoming_events'),
    path('project/<int:id>/', views.project_detail, name='project_detail'),
]