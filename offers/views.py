from django.shortcuts import render
from django.views.generic import ListView,CreateView
from .models import Offer

class CurrentOffers(ListView):
   model = Offer
   context_object_name = 'offers'



class CreateOfferView(CreateView):
    model = Offer
    fields = ['title','description','payment']

    def form_valid(self,form):
        form.instance.username = self.request.user
        return super().form_valid(form)

def terms_and_conditions(request):
    return render (request,"jobs/tandc.html")