from django.urls import path

from toys import views

app_name = 'toys'

urlpatterns = [
    path('category/<slug:slug>', views.details_category, name='details_category'),
    path('toy/<slug:slug>', views.details_toy, name='details_toy'),
]
