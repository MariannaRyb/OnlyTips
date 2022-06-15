from django.contrib.auth.forms import AuthenticationForm
from .models import Cafe, WaiterProfile, Transaction
from .forms import WaiterProfileForm, ExtendedRegistrationForm, CustomerProfileForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm,WaiterUpdateForm, CustomerUpdateForm, JoinForm, TokenTransactForm
from django.http import HttpResponse
from .blockchain import transac, balance

# Create your views here.

@login_required(login_url="/login")
def index(request):
    #starting page - a list of all waiters
    cafes_names = Cafe.objects.all().order_by('title') # can add .order_by

    return render(request, 'tips/index.html', {
        'tips': cafes_names
    })

@login_required(login_url="/login")
def cafe_waiters(request, cafe_slug):
    #starting page - a list of all waiters
    selected_cafe = Cafe.objects.get(slug=cafe_slug)
    selected_waiters_list = list(WaiterProfile.objects.filter(cafe__title=selected_cafe.title).order_by("user__last_name"))
    selected_users = [] #print(User.objects.get(username=selected_waiters_list).first_name)
    #print(User.objects.get(username=selected_waiters_list[0]).first_name)
    #print(selected_waiters_list[0])
   # waiters_names = User.objects.all() # can add .order_by

    return render(request, 'tips/list_of_waiters_cafe.html', {
        'tips': (selected_waiters_list) # waiters_usernames
        #'wallets': selected_users
    })

@login_required(login_url="/login")
def waiter_details(request, waiter_wallet):
    try:
        selected_waiter = WaiterProfile.objects.get(wallet=waiter_wallet)
        if request.method == "GET":
            tipping_form = TokenTransactForm()
            balance_ok = False


        else:
            tipping_form = TokenTransactForm(request.POST)
            if tipping_form.is_valid():

                instance = tipping_form.save(commit=False)
                instance.user = request.user
                try:
                    instance.sender = request.user.customerprofile.wallet
                except:
                    instance.sender = request.user.waiterprofile.wallet

                instance.receiver = waiter_wallet

                if (balance(instance.sender) < instance.amount or instance.amount <= 0
                        or isinstance(instance.amount, float) != True):
                    balance_ok = False
                else:
                    instance.save()
                    transac(instance.sender, instance.receiver, instance.amount)
                    balance_ok = True
                    return redirect('all-cafes')

        return render(request, 'tips/about_waiter.html', {
            'form': tipping_form,
            'waiter_found': True,
            'balance_ok': balance_ok,
            'waiter_first_name': selected_waiter.user.first_name,
            'waiter_last_name': selected_waiter.user.last_name,
            'waiter_description': selected_waiter.description,
            'waiter_wallet': selected_waiter.wallet,
            'waiter_image': selected_waiter.image
        })


    except Exception as exc:
        #print(exc)
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


def CustomerRegisterPage(request):
    if request.method == 'POST':
        form = ExtendedRegistrationForm(request.POST)
        customer_form = CustomerProfileForm(request.POST, request.FILES)
        if 'image' in request.FILES:
            customer_form.image = request.FILES['image']
        if form.is_valid() and customer_form.is_valid():
            user = form.save()
            profile = customer_form.save(commit=False)
            profile.user = user
            profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('all-cafes')

    else:
        form = ExtendedRegistrationForm()
        customer_form = CustomerProfileForm()

    context = {'form':form, 'customer_form': customer_form}
    return render(request, 'tips/registration customer.html', context)

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

def logoutPage(request):
    #if request.method=='POST':
    logout(request)
    return redirect('about')



def about(request):
    return render(request, 'tips/about.html')


def profile(request):
    try:
        balance_wallet = str(balance(request.user.customerprofile.wallet))
    except:
        balance_wallet = str(balance(request.user.waiterprofile.wallet))

    try:
        transactions = Transaction.objects.filter(sender=request.user.customerprofile.wallet)
    except:
        transactions = Transaction.objects.filter(sender=request.user.waiterprofile.wallet)

    try:
        transactions_received = Transaction.objects.filter(receiver=request.user.customerprofile.wallet)
    except:
        transactions_received = Transaction.objects.filter(receiver=request.user.waiterprofile.wallet)

    if len(transactions_received) > 0:
        transactions_received_len = True
    else:
        transactions_received_len = False

    if len(transactions) > 0:
        transactions_len = True
    else:
        transactions_len = False

    context = {'balance_wallet': balance_wallet,
               'transactions': transactions,
               'transactions_recieved': transactions_received,
               'transactions_len': transactions_len,
               'transactions_recieved_len': transactions_received_len
               }
    return render(request, 'tips/profile.html', context)


@login_required
def edit_profile(request):
    first_name = request.user.first_name
    last_name = request.user.last_name
    wallet = request.user.waiterprofile.wallet
    description = request.user.waiterprofile.description
    cafe = request.user.waiterprofile.cafe
    if request.method == 'POST':
        p_form = WaiterUpdateForm(request.POST, request.FILES, instance=request.user.waiterprofile)
        u_form = UserUpdateForm(request.POST,instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
            waiter_u = u_form.save(commit=False)
            waiter_u.username = request.user.username
            if not waiter_u.first_name:
                waiter_u.first_name = first_name

            if not waiter_u.last_name:
                waiter_u.last_name = last_name

            waiter_p = p_form.save(commit=False)
            if not waiter_p.wallet:
                waiter_p.wallet = wallet
            if not waiter_p.description:
                waiter_p.description = description
            if not waiter_p.cafe:
                waiter_p.cafe = cafe

            waiter_u.save()
            waiter_p.save()

            return redirect('profile')
    else:
        p_form = WaiterUpdateForm(instance=request.user)
        u_form = UserUpdateForm(instance=request.user.waiterprofile)

    context={'p_form': p_form,
             'u_form': u_form}
    return render(request, 'tips/edit_profile.html',context )

def register_choices(request):
    return render(request, 'tips/register choice.html')

@login_required
def edit_customer(request):
    first_name = request.user.first_name
    last_name = request.user.last_name
    wallet = request.user.customerprofile.wallet
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = CustomerUpdateForm(request.POST,request.FILES,instance=request.user.customerprofile)

        if p_form.is_valid() and u_form.is_valid():
            customer_u = u_form.save(commit=False)
            customer_u.username = request.user.username
            if not customer_u.first_name:
                customer_u.first_name = first_name

            if not customer_u.last_name:
                customer_u.last_name = last_name

            customer_p = p_form.save(commit=False)
            if not customer_p.wallet:
                customer_p.wallet = wallet

            customer_u.save()
            customer_p.save()

            return redirect('profile')
    else:
        p_form = CustomerUpdateForm(instance=request.user)
        u_form = UserUpdateForm(instance=request.user.customerprofile)

    context={'p_form': p_form,
             'u_form': u_form}
    return render(request, 'tips/customer_edit_profile.html',context)


def join(request):
    if request.method == 'POST':
        form = JoinForm(request.POST, request.FILES)
        if 'image' in request.FILES:
            form.image = request.FILES['image']
        if form.is_valid():
            form.save()
            return redirect('about')
    else:
        form = JoinForm()
    context = {'form': form}
    return render(request, 'tips/join.html', context)
