from django.shortcuts import render
from .models import Job

# Create your views here.
def jobs(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})