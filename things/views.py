from django.shortcuts import render

# Create your views here.
def things(request):
    return render(request,"index.html")