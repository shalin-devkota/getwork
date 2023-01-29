from django.http import request

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404, redirect, render
from .forms import UserRegistrationForm
from django.views.generic import DetailView
from django.contrib.auth.models import User
from .forms import ProfileRegistrationForm, ProfileUpdateForm
from jobs.models import Job 

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        p_form = ProfileRegistrationForm(request.POST)
        if form.is_valid() and p_form.is_valid():
            username = form.save()
            profile = p_form.save(commit=False)
            profile.user =  username
            profile.save()
            
            return redirect('user-login')

    else:
        p_form = ProfileRegistrationForm
        form = UserCreationForm()

    context= {
        'form':form,
        'p_form':p_form
    }

    return render(request,"users/register.html",context)

class UserProfileView(DetailView):

    """
    This view is not being used anywhere. It was replaced by user_profile. I left it here cause yes
    """

    form_class= ProfileUpdateForm
    model = User
    template_name= "users/user_detail.html"
  

    def get_context_data(self,**kwargs):
        """
        posts are linked to the User model and not The profile model. Hence we always work with the user model
        and access the Profile model using the User mode (user.profile) as needded.        
        
        """
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs.get('pk')     #Extracts the user id from the url.
        username = User.objects.get(pk=user_id)  
        context['jobs']= Job.objects.filter(username = username)
        return context

def user_profile(request,pk):
    user_model = User.objects.get(pk=pk)
    jobs = Job.objects.filter(username=user_model)
    if request.method == "POST":
        u_form  =ProfileUpdateForm(request.POST,request.FILES,instance = request.user.profile)
        if u_form.is_valid():
            u_form.save()
            return redirect (f"/profile/{pk}")
    else:
        u_form= ProfileUpdateForm()
    context={
        'user_model': user_model,
        'jobs': jobs,
        'u_form' : u_form
    }
    return render(request,"users/user_detail.html",context)
    
