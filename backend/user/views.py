from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .forms import UserForm


def index(request):
    return redirect('home:home')


def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('home:home')
    return redirect('home:home')


def user_logout(request):
    logout(request)
    return redirect("home:home")


class Register(View):
    form_class = UserForm
    template_name = 'registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form, 'user': ""})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User object if credentials are correct
            user = authenticate(username=username, password=password)
            from .models import User
            u = User()
            u.username = username
            u.bio = request.POST['bio']
            u.save()
            if user is not None:
                print('not none')
                if user.is_active:
                    print('active')
                    login(request, user)
                    return redirect("home:home")
        return render(request, self.template_name, {'form': form})

def user_profile(request):
    from .models import User
    return render(request, 'profile_view.html', {'webuser': User.objects.get(username=request.user.username)})
