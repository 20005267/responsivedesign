from django.shortcuts import render

# Create your views here.
def responsivepage(request):
    context = {}
    return render(request,'responcivesesignapp/responsivepage.html',context) 