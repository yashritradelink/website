from email.quoprimime import body_check
import http
from pyexpat.errors import messages
from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.contrib import messages



# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("Hello world")

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def blog(request):
    return render(request,'blog.html')

def service(request):
    return render(request,'service.html')

def projectn(request):
    return render(request,'projectn.html')

def testimonial(request):
    return render(request,'testimonial.html')

def team(request):
    return render(request,'team.html')

def blog(request):
    return render(request,'blog.html')

# def detail(request):
#     return render(request,'detail.html')

def pp(request):
    return render(request,'pp.html')

def ps(request):
    return render(request,'ps.html')

def pet(request):
    return render(request,'pet.html')

def pe(request):
    return render(request,'pe.html')

def masterbatch(request):
    return render(request,'masterbatch.html')

def recycled(request):
    return render(request,'recycled.html')

def sendmail(request):
    if request.method== 'POST':
        username = request.POST['username']
        email = request.POST['email']
        date = request.POST['date']
        time= request.POST['time']
        subject=request.POST['subject']
        message=request.POST['message']
        # email_content= ["Message from ",
        #                                 f"the user with name {username}", f"with the email {email}", f"requested to contact on {date}",
        #                                  f"and time on {time}", f"with subjected details as following: \n",
        #                                 f" Message: {message}"]
        body={'name':username,'email':email,'date':date,'time':time,'message':message}
        email_content= "\n".join(body.values())
        # print(email_content)

        send_mail(
        subject,
        email_content,
        'bijav132@gmail.com',
        ['patel.nirav15.5@gmail.com'],
        fail_silently=False,
        )
        messages.info(request,"Mail Send successfully")
        return render(request,'contact.html')
    else:
        messages.info(request,"Mail Not Send")
        return render(request,'contact.html')
