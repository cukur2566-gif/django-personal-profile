
from datetime import date
from django.shortcuts import render

def index(request):
    context = {
        'first_name': 'abdullah',
        'last_name': 'Elkurd',
        'student_id': 120231200,
        'address': 'Gaza',
        'email': '',
        'date_of_birth': date(2003, 1, 1),
        'major': 'Web Computing',
        'university': 'Islamic University of Gaza',
    }

    return render(request, 'pages/index.html', context)
