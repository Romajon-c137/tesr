from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator

from apps.slide.models import Slide
from apps.services.models import Service, Category as ServiceCategory
from apps.specialists.models import Department, Person, Role
from apps.prices.models import Analysis
from apps.reviews.models import Review
from apps.news.models import News
from .models import FreeCall, Page
from .forms import Form


def main(request):
    doctors = Person.objects.filter(published=True, role=2)
    slides = Slide.objects.filter(is_active=True).order_by('order')
    reviews = Review.objects.filter(published=True)[:3]
    hiddenreviews = Review.objects.filter(published=True)[3:]
    return render(request, 'main/index.html', {'slides': slides, 'doctors': doctors, 'reviews': reviews, 'hiddenreviews': hiddenreviews})


def services(request):
    services = Service.objects.filter(
        category__slug=request.GET['category']) if 'category' in request.GET else Service.objects.all()
    serviceCategory = ServiceCategory.objects.filter(is_active=True)
    active = request.GET['category'] if 'category' in request.GET else 'all'
    return render(request, 'services/index.html', {'services': services.filter(published=True, category__is_active=True), 'serviceCategory': serviceCategory, 'active': active})


def service(request, slug):
    service = Service.objects.get(slug=slug)
    return render(request, 'services/service.html', {'service': service})

def labs(request):
    analysises = Analysis.objects.filter(published=True)
    return render(request, 'labs/index.html', {'analysises': analysises})

def all_news(request):
    news_list = News.objects.all()
    paginator = Paginator(news_list, 10)
    page_number = request.GET.get('page')
    all_news = paginator.get_page(page_number)
    return render(request, 'news/index.html', {'all_news': all_news})

def news(request, slug):
    news = News.objects.get(slug=slug)
    return render(request, 'news/detail.html', {'news': news})


def prices(request):
    analysises = Analysis.objects.filter(published=True)
    first = analysises.first()
    active = request.GET['active'] if 'active' in request.GET else 'first'
    analysis = first if active == 'first' else Analysis.objects.get(id=active)
    context = {'analysises': analysises[1:], 'first': first,
               'active': active, 'analysis': analysis}
    return render(request, 'prices/index.html', context)


def clinic(request):
    departments = Department.objects.filter(published=True)
    people = Person.objects.filter(
        department__slug=request.GET['department']) if 'department' in request.GET else Person.objects.all()
    active = request.GET['department'] if 'department' in request.GET else 'all'
    return render(request, 'clinic/index.html', {'departments': departments, 'people': people.filter(published=True, department__published=True), 'active': active})


def specialists(request):
    roles = Role.objects.filter(published=True)
    departments = Department.objects.filter(published=True)
    role = Role.objects.get(slug=request.GET['role']) if 'role' in request.GET else Role.objects.first()
    active = request.GET['role'] if 'role' in request.GET else 'all'
    people = Person.objects.filter(published=True, roles=role)
    context = {'roles': roles[1:], 'first': roles.first(), 'departments': departments, 'people': people, 'active': active, 'role': role}
    return render(request, 'specialists/index.html', context)


def form(request):
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if FreeCall.objects.filter(e_mail=instance.e_mail).exists():
                messages.warning(
                    request, "Вы уже отправляли заявку на получение консультации")
            else:
                instance.save()
                messages.success(request, "Ваша заявка отправлена")
            return render(request, 'components/free_call.html', {'form': form})
    else:
        form = Form()
        return render(request, "components/free_call.html", {'form': form})


def page(request, slug):
    page = Page.objects.get(slug=slug)
    return render(request, 'main/page.html', {'page': page})


def review(request, id):
    review = Review.objects.get(id=id)
    return render(request, 'main/review.html', {'review': review})