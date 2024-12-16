from django.urls import path 

from . import views 

app_name = "website"
urlpatterns = [
    path("", views.home, name="home"),
    path('timeline-data/', views.timeline_data, name='timeline_data'),
]