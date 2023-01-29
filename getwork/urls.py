from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView
from users.views import register, UserProfileView, user_profile
from jobs.views import CurrentJobs,CreateJobView, accept_job
from django.conf import settings
from django.conf.urls.static import static
from offers.views import CurrentOffers,CreateOfferView, terms_and_conditions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobs/',CurrentJobs.as_view(),name="jobs-list"),
    path('',LoginView.as_view(template_name="users/login.html",redirect_authenticated_user= True),name="user-login"),
    path('logout/',LogoutView.as_view(template_name="users/logout.html"),name="user-logout"),
    path('register',register,name="user-register"),
    path('jobs/create',CreateJobView.as_view(),name="create-job"),
    path('profile/<int:pk>',user_profile,name="user-profile"),
    path('offers/',CurrentOffers.as_view(),name="offers-list"),
    path('offers/create',CreateOfferView.as_view(),name="create-offer"),
    path('jobs/accept',accept_job,name="accept-job"),
    path('offers/accept',accept_job,name="accept-job"),
    path("terms",terms_and_conditions,name="terms")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


