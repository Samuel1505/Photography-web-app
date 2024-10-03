
from django.urls import path
from landing.views import homepage, about

urlpatterns = [
    path('', homepage.as_view(), name='homepage' ),
    path('about', about.as_view(), name='about_us')
]
