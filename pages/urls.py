from django.urls import path

from pages import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('distributors', views.all_distributors, name='all_distributors'),
    path('our-stores', views.our_stores, name='our_stores'),
    path('sales-offices', views.sales_offices, name='sales_offices'),
    path('faqs', views.faqs, name='faqs'),
    path('terms-conditions', views.terms_conditions, name='terms_conditions'),
    path('history', views.history, name='history'),
    path('projects', views.all_projects, name='all_projects'),
    path('room-concepts', views.room_concepts, name='room_concepts'),
    path('safety-cetificates', views.safety_cetificates, name='safety_cetificates'),
    path('size-guide', views.size_guide, name='size_guide'),
    path('timeline', views.timeline, name='timeline'),
    path('vision-mission', views.vision_mission, name='vision_mission'),
    path('development-milestone', views.development_milestone, name='development_milestone'),
    path('world-wide', views.world_wide, name='world_wide'),
    path('project/<slug:slug>', views.detail_project, name='detail_project'),
]
