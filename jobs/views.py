from jobs.models import Job
from django.views.generic import ListView,DetailView
from django.views.generic import CreateView
from django.shortcuts import render

class CurrentJobs(ListView):
    model = Job
    template_name = "jobs/jobs.html"
    context_object_name= "jobs"
    


class CreateJobView(CreateView):
    model = Job
    fields = ['title','description','payment']

    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)

def accept_job(request):
    return render(request,"jobs/accept_job.html")