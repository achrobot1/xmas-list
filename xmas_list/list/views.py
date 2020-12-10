from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, get_user_model

from .models import Gift, UserProfile

# Create your views here.
    
###########################################################################
def index(request):
    # Check if user is logged in
    if not request.user.is_authenticated:
        # Redirect to login if user is not logged in
        return redirect('/login/') 
    else: 
        User = get_user_model()
        users = User.objects.all()

        context = []
        for u in users:
            try:
                g = list(Gift.objects.filter(requestor=u.id))
            except :
                g = None

            context.append({'users':u, 'gifts_requested':g})

        return render(request=request,
                template_name='all_lists_view.html',
                context={'context':context})

###########################################################################
def robots(request):
    return HttpResponse('Disallow: *')


from django.contrib.auth.forms import AuthenticationForm

###########################################################################
def login_request(request): 
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return redirect('/login/')

    form = AuthenticationForm()
    return render(request=request,
                template_name='login.html',
                context={'form':form})

###########################################################################
def logout_request(request):
    logout(request)
    return redirect('/login/')

###########################################################################
from .forms import GiftForm

def edit_list(request):
    # Check if user is logged in
    if not request.user.is_authenticated:
        # Redirect to login if user is not logged in
        return redirect('/login/') 

    else:
        try:
            g = list(Gift.objects.filter(requestor=request.user.id))
        except :
            g = None

        context = {'username':request.user.username, 'gifts_requested':g}

        if request.method == 'POST':
            # handle Post data
            form = GiftForm(request.POST)
            if form.is_valid():
                new_gift = form.save(commit=False)
                new_gift.requestor = request.user
                new_gift.save()

            return redirect('/edit_list')


        form = GiftForm() 
        return render(request=request,
                    template_name='edit_list.html',
                    context={'form':form, 'context':context})

###########################################################################
def delete_gift(request, gift_id):
    g = Gift.objects.get(id=gift_id)
    g.delete()
    return redirect('/edit_list')

########################################################################### 
from .notify import *
def claim_gift(request, gift_id):
    g = Gift.objects.get(id=gift_id)
    g.gift_claimed_by = request.user
    g.gift_claimed = True
    g.save()

    users = UserProfile.objects.exclude(user=g.requestor)
    recipients = [u.email for u in users]


    print('sending email to:')
    for r in recipients:
        print(r)

    send_email(f'{g.gift_claimed_by.username} has claimed the following gift for {g.requestor.username}:\n\n {g.description}', recipients)

    return redirect('/')

###########################################################################
def unclaim_gift(request, gift_id):
    g = Gift.objects.get(id=gift_id)
    g.gift_claimed_by = None
    g.gift_claimed = False
    g.save()

    users = UserProfile.objects.exclude(user=g.requestor)
    recipients = [u.email for u in users]

    print('sending email to:')
    for r in recipients:
        print(r)


    send_email(f'{g.gift_claimed_by.username} has unclaimed the following gift for {g.requestor.username}:\n\n {g.description}\n\nThis gift is currently UNCLAIMED', recipients)

    return redirect('/')

###########################################################################
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserProfileForm

def account(request):
    # Check if user is logged in
    if not request.user.is_authenticated:
        # Redirect to login if user is not logged in
        return redirect('/login/') 

    # Get all context variables
    message = request.GET.get('message')
    success = (message == 'success')
    fail = (message == 'fail')

    pass_form = PasswordChangeForm(request.user)

    user_profile = list(UserProfile.objects.filter(user=request.user))[0] 
    user_form = UserProfileForm(instance=user_profile)

    context = {
        'pass_form':pass_form,
        'user_form':user_form,
        'user_profile': user_profile,
        'success':success, 'fail':fail
    }

    return render(request=request,
            template_name='account_view.html',
            context=context)


###########################################################################
def update_account_info(request):
    # Check if user is logged in
    if not request.user.is_authenticated:
        # Redirect to login if user is not logged in
        return redirect('/login/') 

    user_profile = list(UserProfile.objects.filter(user=request.user))[0] 

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()

    return redirect('account')

###########################################################################
from django.contrib.auth import update_session_auth_hash

def change_password(request):
    # Check if user is logged in
    if not request.user.is_authenticated:
        # Redirect to login if user is not logged in
        return redirect('/login/') 

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            response = redirect('account')
            response['Location'] += '?message=success'
            return response
        else:
            response = redirect('account')
            response['Location'] += '?message=fail'
            return response


    else:
        return redirect('account')
