from django.shortcuts import render
from .forms import UserRegister
from django.http import HttpResponse

# Фейковые имена
users = ['userVasil', 'userIvan', 'userEgor']

# Create your views here.
def sign_up_by_django(request):
    info = {}
# получение данных из POST-запроса как в шаблоне
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            # обработка данных из POST-запроса
            if password != repeat_password:
                info['error'] = 'Несовпадение паролей'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                users.append(username)
                return HttpResponse(f'Вы зарегистрировались как {username}')
        else:
            form = UseRegister()
            info['message'] = form
        return render(request, 'fifth_task/registration_page.html', info)

# обработка get-запроса как в шаблоне
def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        if username in users:
            info['error'] = 'Пользователь уже существует'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        users.append(username)
        return HttpResponse(f'Вы зарегистрировались как {username}')
    else:
        info['username'] = request.POST.get('username')
    return render(request, 'fifth_task/registration_page.html', info)
