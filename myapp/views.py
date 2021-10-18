from django.shortcuts import render, redirect
from . models import Contact, Hero, About, Portfolio, Services, Stats, Testimony
# Create your views here.
def index(request):
    if request.method == "POST":
        # if request.POST.get('name') and request.POST.get('email') and request.POST.get('subject') and request.POST.get('message'):
            contact = Contact()
            contact.name = request.POST.get('name')
            print(contact.name)
            contact.email = request.POST.get('email')
            contact.subject = request.POST.get('subject')
            contact.message = request.POST.get('message')
            contact.save()
            return redirect('index')
    hero = Hero.objects.all()
    about = About.objects.all()
    services = Services.objects.all()
    stats = Stats.objects.all()
    portfolios = Portfolio.objects.all()
    testimonys = Testimony.objects.all()
    context = {'hero':hero, 'about': about, 'services': services, 'stats':stats, 'portfolios':portfolios, 'testimonys':testimonys}
    return render(request, 'index.html', context)

