from django.shortcuts import render
from .models import Skills,Info,Experience
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect


# Create your views here.


def index(request):
    info = Info.objects.all()
    experience = Experience.objects.all()
    skills = Skills.objects.all()


    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['Subject']
        email = request.POST['replyto']
        message = request.POST['message']

        send_mail(subject,message,email,['lovelymanju198@gmail.com'])
        messages.info(request,"Hey "+name +"Thanks for your responce")

        print(subject,email,'**********************************************')
        return redirect('/')


    return render(request,'index.html',{'skills':skills,'info':info,'experience':experience})

#
# def contact(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         subject = request.POST['Subject']
#         email = request.POST['_replyto']
#         message = request.POST['message']
#
#         send_mail(subject,message,email,['lovelymanju198@gmail.com'])
#         return render(request,'index.html',{'skills':skills,'info':info,'experience':experience})
#
#     else:
#         pass
