from django.shortcuts import render

# Create your views here.
def ngan(request):
    return render(request, 'jobs/ngan.html')