from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .forms import UserForm, BookForm
from .models import Book


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

            if user is not None:

                if user.is_active:
                    user_login(request, user)
                    return redirect("home:home")
        return render(request, self.template_name, {'form': form})




# not use

class BookForm(View):
    form_class = BookForm
    template_name = 'book_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form, 'Books': Book.objects.all()})

    def post(self, request):
        book = Book()

        # cleaned (normalized) data
        book.book_id = request.POST['book_id']
        book.isbn = request.POST['isbn']
        book.book_name = request.POST['book_name']
        book.price = request.POST['price']
        book.author = request.POST['author']
        book.save()
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form, 'Books': Book.objects.all()})


def update(request):
    b = Book.objects.get(book_id=request.POST['book_id'])
    b.isbn = request.POST['isbn']
    b.book_name = request.POST['book_name']
    b.price = request.POST['price']
    b.author = request.POST['author']
    b.save()
    return render(request, 'book_form.html', {'Books': Book.objects.all()})


def delete(request):
    id = request.GET.get('id')
    b = Book.objects.get(book_id=id)
    b.delete()
    return render(request, 'book_form.html', {'Books': Book.objects.all()})


class BookDelete(View):
    form_class = BookForm
    template_name = 'book_form.html'

    def get(self, request):
        id = request.GET.get('id')
        b = Book.objects.get(book_id=id)
        print(b)
        b.delete()
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form, 'Books': Book.objects.all()})

    def post(self, request):
        b = Book.objects.get(book_id=request.POST['delete'])
        b.delete()
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form, 'Books': Book.objects.all()})
