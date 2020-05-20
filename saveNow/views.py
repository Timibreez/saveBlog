from django.shortcuts import render, redirect
from . models import SavePost
from django.contrib.auth.decorators import login_required
from . import forms

def index(request):
    savepost = SavePost.objects.all().order_by('date')
    return render (request, 'saveNow/index.html', {'savepost':savepost})

@login_required(login_url='users/login')
def createPost(request):
    if request.method == 'POST':
        form = forms.CreateSavePost(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('saveNow:index')
    else:
        form = forms.CreateSavePost()
    return render(request, 'saveNow/savepost.html',{'form':form})