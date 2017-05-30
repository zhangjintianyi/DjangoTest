from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import User
from .forms import LoginForm
from .utils import send_confirme_mail

# Create your views here.注册

def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            user_name = form.cleaned_data['user_name']
            password = form.cleaned_data['password']
            if User.objects.filter(email=email):
                print('已有')
            user = User(user_name=user_name, email=email, password=password)
            user.save()
            res = send_confirme_mail.delay()
            res.get()

            return HttpResponseRedirect('/log/thanks')
        else:
            print("valid not")
    else:
        form = LoginForm()
        return render(request, 'Log/login.html', context={'form': form})

def thank_reg(request):
    user = request.user
    return render(request, 'Log/thanks_reg.html', context={'user': user})

























