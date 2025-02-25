
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def men_view(request):
    return render(request, 'men.html')

def women_view(request):
    return render(request, 'women.html')

def kids_view(request):
    return render(request, 'kids.html')

def personalize_view(request):
    return render(request, 'personalize.html')

def sales_view(request):
    return render(request, 'sales.html')

def trending_view(request):
    return render(request, 'trending.html')

def brands_view(request):
    return render(request, 'brands.html')

def product_view(request):
    return render(request, 'product1.html','product2.html','product3.html','product4.html','product5.html','product5.html')

def product1(request):
    return render(request, 'product1.html')

def product2(request):
    return render(request, 'product2.html')

def shop(request):
    return render(request, 'shop.html')

def brands(request):
    return render(request, 'brands.html')

