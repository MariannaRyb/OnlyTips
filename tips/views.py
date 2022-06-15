from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from .models import Cafe, WaiterProfile
from .forms import WaiterProfileForm, ExtendedRegistrationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    #starting page - a list of all waiters
    cafes_names = Cafe.objects.all() # can add .order_by

    return render(request, 'tips/index.html', {
        'tips': cafes_names
    })

def cafe_waiters(request, cafe_slug):
    #starting page - a list of all waiters
    selected_cafe = Cafe.objects.get(slug=cafe_slug)
    selected_waiters_list = list(WaiterProfile.objects.filter(cafe__title=selected_cafe.title))
    selected_users = [] #print(User.objects.get(username=selected_waiters_list).first_name)
    #print(User.objects.get(username=selected_waiters_list[0]).first_name)
    #print(selected_waiters_list[0])
   # waiters_names = User.objects.all() # can add .order_by

    return render(request, 'tips/list_of_waiters_cafe.html', {
        'tips': (selected_waiters_list) # waiters_usernames
        #'wallets': selected_users
    })


def waiter_details(request, waiter_wallet):
    try:
        print(waiter_wallet)
        selected_waiter = WaiterProfile.objects.get(wallet=waiter_wallet)

        return render(request, 'tips/about_waiter.html', {
            'waiter_found': True,
            #'waiter_name': selected_waiter.name,
            'waiter_cafe': selected_waiter.cafe.title,
            'waiter_description': selected_waiter.description,
            'waiter_wallet': selected_waiter.wallet,
            'waiter_image': selected_waiter.image
           # 'waiter_password': selected_waiter.password
        })
    except Exception as exc:
        return render(request, 'tips/about_waiter.html', {
            'waiter_found': False
        })


def registerPage(request):
    if request.method == 'POST':
        form = ExtendedRegistrationForm(request.POST)
        profile_form = WaiterProfileForm(request.POST, request.FILES)
        if 'image' in request.FILES:
            profile_form.image = request.FILES['image']
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('all-cafes')
    else:
        form = ExtendedRegistrationForm()
        profile_form = WaiterProfileForm()

    context = {'form':form, 'profile_form': profile_form}
    #return redirect("all-cafes")
    return render(request, 'tips/registration.html', context)

def loginPage(request):

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            user = form.get_user()
            login(request, user)
            return redirect('all-cafes')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'tips/login.html', context)