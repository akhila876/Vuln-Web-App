from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterForm, ImageForm, PostForm, ChangePasswordForm
from .models import ImageUpload, Post

def index(request):
    return render(request, 'index.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('profile')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def profile_view(request):
    posts = Post.objects.filter(user=request.user)
    return render(request, 'profile.html', {'posts': posts})

@login_required
def gallery_view(request):
    if request.method == 'POST' and request.FILES.get('image'):
        ImageUpload.objects.create(user=request.user, image=request.FILES['image'])

    images = ImageUpload.objects.filter(user=request.user)
    return render(request, 'gallery.html', {'images': images})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(user=request.user, content=form.cleaned_data['content'])
            return redirect('profile')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            if request.user.check_password(form.cleaned_data['old_password']):
                request.user.set_password(form.cleaned_data['new_password'])
                request.user.save()
                return redirect('login')
    else:
        form = ChangePasswordForm()
    return render(request, 'change_password.html', {'form': form})

