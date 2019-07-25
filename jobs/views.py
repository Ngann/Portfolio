from django.shortcuts import render, get_object_or_404
from .models import Job

# Create your views here.
def home(request):
    # variable jobs is equal to job objects from the database, class.objects
    # {'jobs': jobs} dictionary to render the objects
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})

def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request,'jobs/detail.html', {'job':job_detail})