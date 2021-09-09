from django.shortcuts import render, redirect
from . form import ObjectForm
from . models import Object

# Create your views here

def object(request):
    if request.method=="POST":
        form = ObjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = ObjectForm()
    return render(request,'app/object.html', {'form':form})




