from django.shortcuts import render
from .models import Job

# Create your views here.
def home(request):
    # variable jobs is equal to job objects from the database, class.objects
    # {'jobs': jobs} dictionary to render the objects
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})