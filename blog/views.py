from django.shortcuts import render
from .models import Skills,Info,Experience,Contact,Portfolio
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect
from django.core.paginator import Paginator
import os


# Create your views here.


def index(request):
    info = Info.objects.all()
    experience = Experience.objects.all()
    skills = Skills.objects.all()
    # portfolio = Portfolio.objects.all()

    user_list = Portfolio.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 2)
    try:
        portfolio = paginator.page(page)
    except :
        portfolio = paginator.page(1)

    return render(request,'index.html',{'skills':skills,'info':info,'experience':experience,'portfolio':portfolio})


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['Subject']
        email = request.POST['replyto']
        message = request.POST['message']
        tel = request.POST['tel']

        print(name,subject,email,message,tel)
        cont = Contact.objects.create(name=name,subject=subject,email=email,message=message,tel=tel)
        cont.save()
        messages.info(request,'Thank you '+name+' for your responce... I will be contact you in soon...')
        return redirect('/')

        # send_mail(subject,message,email,['lovelymanju198@gmail.com'])

    else:
        return redirect('/')
        pass
