from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm
from .models import announcement
from django.contrib import messages


def home(request):
    return render(request, 'main/home.html')


def index(request):
    return render(request, 'main/index.html')


def basket(request):
    return render(request, 'main/basket.html')


def take(request):
    return render(request, 'main/take.html')


def getby(request):
    return render(request, 'main/getby.html')


def category(request):
    return render(request, 'main/category.html')


def sport(request):
    return render(request, 'main/sport.html')


def child(request):
    return render(request, 'main/child.html')


def cloth(request):
    return render(request, 'main/cloth.html')


def other(request):
    return render(request, 'main/other.html')


# def home(request):
#     return render(request, 'main/home.html')


def rest(request):
    return render(request, 'main/rest.html')


def register(request):
    return render(request, 'main/register.html')


def catalog(request):
    tasks = announcement.objects.all()
    return render(request, 'main/catalog.html', {'tasks': tasks})


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'main/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт создан для {username}')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})
