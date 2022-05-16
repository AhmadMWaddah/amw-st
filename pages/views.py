from django.shortcuts import render, get_object_or_404
from pages.models import Faq, Term, SalesOffice, Country, LocalStore, Distributor, Project, Image


def index(request):
    faqs = Faq.objects.all()
    page = 'Home Page'
    context = {
        'page': page,
        'faqs': faqs,
    }
    return render(request, 'index.html', context)


def all_distributors(request):
    distributors = Distributor.objects.all()
    page = 'Distribtors'
    context = {'page': page, 'distributors': distributors}
    return render(request, 'pages/distributors.html', context)


def sales_offices(request):
    offices = SalesOffice.objects.all()
    page = 'Sales Offices'
    context = {'page': page, 'offices': offices}
    return render(request, 'pages/sales-offices.html', context)


def our_stores(request):
    stores = LocalStore.objects.all()
    page = 'Our Stores'
    context = {'stores': stores, 'page': page}
    return render(request, 'pages/our-stores.html', context)


def faqs(request):
    faqs = Faq.objects.all()
    page = 'FAQs'
    context = {'faqs': faqs, 'page': page}
    return render(request, 'pages/faqs.html', context)


def history(request):
    page = 'History'
    context = {'page': page}
    return render(request, 'pages/history.html', context)


def all_projects(request):
    projects = Project.objects.all()
    page = 'Projects'
    context = {
        'page': page,
        'projects': projects,
    }
    return render(request, 'pages/projects.html', context)


def detail_project(request, slug):
    project = get_object_or_404(Project, slug=slug)
    project_images = project.images()
    page = f'{project.name} - {project.area}'
    context = {
        'page': page,
        'project': project,
        'project_images': project_images,
    }
    return render(request, 'pages/detail-project.html', context)


def room_concepts(request):
    page = 'Room Concepts Ideas'
    context = {'page': page}
    return render(request, 'pages/room-concept.html', context)


def safety_cetificates(request):
    page = 'Safety and Certificates'
    context = {
        'page': page,
    }
    return render(request, 'pages/safety-cetificates.html', context)


def size_guide(request):
    page = 'Size Guide'
    context = {'page': page}
    return render(request, 'pages/size-guide.html', context)


def terms_conditions(request):
    terms = Term.objects.all()
    page = 'Terms & Conditions'
    context = {'terms': terms, 'page': page}
    return render(request, 'pages/terms-conditions.html', context)


def timeline(request):
    page = 'Timeline'
    context = {'page': page}
    return render(request, 'pages/timeline.html', context)


def vision_mission(request):
    page = 'Vision & Mission'
    context = {'page': page}
    return render(request, 'pages/vision-mission.html', context)


def development_milestone(request):
    page = 'Child Development Milestone'
    context = {'page': page}
    return render(request, 'pages/development-milestone.html', context)


def world_wide(request):
    countries = Country.objects.all()
    page = 'Representative Worldwide'
    context = {'countries': countries, 'page': page}
    return render(request, 'pages/world-wide.html', context)
