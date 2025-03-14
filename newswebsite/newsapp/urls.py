from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='home'),
    path('poltics/',views.politics,name='politics'),
    path('sports/',views.sports,name='sports'),
    path('entertainment/',views.entertainment,name='entertainment')

]
