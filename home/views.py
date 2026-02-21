from django.shortcuts import render, redirect
from data.data import MyInfo
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

@login_required
def about(request):
    content = {
        'firstname': MyInfo.FIRST_NAME, 'lastname': MyInfo.LAST_NAME, 'fullname': MyInfo.FULL_NAME,
        'email': MyInfo.EMAIL, 'age': MyInfo.AGE, 'short_bio': MyInfo.SHORT_BIO, 'bio': MyInfo.BIO,
        'date_of_birth': MyInfo.DATE_OF_BIRTH, 'profession': MyInfo.PROFESSION, 'pr_lang': MyInfo.PROGRAMMING_LANGUAGES,
        'socials': MyInfo.SOCIALS,
    }
    return render(request, 'about.html', content)

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'registrations/sign_up.html', {'form': form})


