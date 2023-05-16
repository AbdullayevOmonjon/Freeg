from django.shortcuts import render,redirect
from django.views import View
from .models import *
# Create your views here.


class Index_view(View):
  def get(self,request):
    data={
      "about":About.objects.all(),
      "azolar":Profil.objects.all(),
      "f":Profil.objects.all()[1],
    }
    return render(request,'index.html',data)
  
  
class About_view(View):
  def get(self,request):
    data={
      "about":About.objects.last()
    }
    return render(request, 'about.html',data)
  
  
class Contact_view(View):
  def get(self,request):
    return render(request, 'contact.html')
  
  def post(self,request):
    Profil.objects.create(
      name=request.POST.get('name'),
      email=request.POST.get('email'),
      tel=request.POST.get('tel'),
      media=request.POST.get('img'),
      uzi_malumot=request.POST.get('my_about')      
    )
    return redirect('contact')
  
  
class Service_view(View):
  def get(self,request):
    data={
      "maqolalar":Maqola.objects.all()
    }
    return render(request, 'service.html',data)