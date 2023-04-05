from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'status':'homepage'}
    return render(request,'core/home.html',context)
