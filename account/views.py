from django.shortcuts import render, redirect
# from django.template import ContextPopException

from .forms import CreateUserForm, LoginForm, UpdateUserForm
from django.contrib.sites.shortcuts import get_current_site
from .token import user_tokenizer_generate
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Account verification email.'
            message = render_to_string('account/registration/email-verification.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': user_tokenizer_generate.make_token(user),
            })
            user.email_user(subject, message)

            return redirect('email_verification_sent')

    context = {'form': form}

    return render(request, 'account/registration/register.html', context=context)


def email_verification(request, uidb64, token):
    unique_id = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=unique_id)

    if user and user_tokenizer_generate.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('email_verification_success')
    else:
        return redirect('email_verification_failed')


def email_verification_sent(request):
    return render(request, 'account/registration/email-verification-sent.html')


def email_verification_failed(request):
    return render(request, 'account/registration/email-verification-failed.html')


def email_verification_success(request):
    return render(request, 'account/registration/email-verification-success.html')


def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('')

    context = {'form': form}
    return render(request, 'account/my-login.html', context=context)


@login_required(login_url='my_login')
def dashboard(request):
    return render(request, 'account/dashboard.html')


def user_logout(request):
    auth.logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('store')

# def user_logout(request):
#     try:
#         for key in list(request.session.keys()):
#             if key == "session_key":
#                 continue
#             else:
#                 del request.session[key]
#     except KeyError:
#         pass
#     messages.success(request, 'You have been logged out.')
#
#     return redirect('store')

@login_required(login_url='my_login')
def profile_update(request):
    form = UpdateUserForm(instance=request.user)
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your profile has been updated.')
            return redirect('dashboard')
    context = {'user_form': form}
    render(request, 'account/update-acc.html', context=context)


@login_required(login_url='my_login')
def delete_profile(request):
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        user.delete()
        messages.error(request, 'Your account has been deleted.')
        return redirect('store')
    return render(request, 'account/delete-acc.html')


