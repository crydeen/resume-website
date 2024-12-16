from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    """Render the main page with the interactive resume."""
    return render(request, 'website/home.html')

@csrf_exempt
def timeline_data(request):
    """Endpoint to serve timeline data as JSON."""
    if request.method == 'GET':
        data = {
            "timeline": [
                {
                    "date": "2013",
                    "title": "Computer Science Spark",
                    "description": "First Computer Science Project - Pac-Man",
                    "details": "My project in my high school computer science class sparked my love for computer science. Wrote a working Pac-Man game in Java."
                },
                {
                    "date": "2014",
                    "title": "College (University of Mississippi)",
                    "description": "Led a team of developers to deliver multiple successful projects.",
                    "details": "Mentored junior developers and improved overall team efficiency."
                },
                {
                    "date": "2023",
                    "title": "Freelance Developer",
                    "description": "Started freelancing to explore diverse projects.",
                    "details": "Built interactive and mobile-friendly websites for a variety of clients."
                },
                {
                    "date": "2024",
                    "title": "Freelance",
                    "description": "Started freelancing to explore diverse projects.",
                    "details": "Built interactive and mobile-friendly websites for a variety of clients."
                },
                {
                    "date": "2025",
                    "title": "Developer",
                    "description": "Started freelancing to explore diverse projects.",
                    "details": "Built interactive and mobile-friendly websites for a variety of clients."
                }
            ]
        }
        return JsonResponse(data)