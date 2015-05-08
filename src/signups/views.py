
#python first
#django second
#your apps
#local directory 

from django.conf import settings 
from django.contrib import messages
from django.core.mail import send_mail 
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect

# Create your views here.
from .forms import SignUpForm

def home(request):    
    return render_to_response("signup.html", locals(), context_instance=RequestContext(request))   
    
def thankyou(request):
    
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        #send_mail(subject, message, from_email, to_list, fail_silently=True)
        subject = 'Thank you for kissing Bao'
        message = 'You have sign up for kissing Bao list.'
        from_email = settings.EMAIL_HOST_USER
        to_list = [save_it.email, settings.EMAIL_HOST_USER]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        messages.success(request, 'Thank you for kissing Bao!!')
        return HttpResponseRedirect('/thank-you/')
    
    return render_to_response("thankyou.html", locals(), context_instance=RequestContext(request))
        
def aboutus(request):
    return render_to_response("aboutus.html", locals(), context_instance=RequestContext(request))

def googlemap(request):
    return render_to_response("google-map.html", locals(), context_instance=RequestContext(request))

def googlemap2(request):
    return render_to_response("google-map-2.html", locals(), context_instance=RequestContext(request))


    