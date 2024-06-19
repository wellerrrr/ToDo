from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .forms import LoginUserForm, SignUpUserForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'userauth/login.html'

    def get_success_url(self):
        return reverse_lazy('core:index')

# def login_user(request):
#     if request.method == 'POST':
#         form = LoginUserForm(request.POST)
#         if form.is_valid(): #Проверка валедности формы
#             cd = form.cleaned_data #После проверки валидности формы этот оператор извлекает очищенные данные из формы в переменную cd. Очищенные данные представляют собой словарь, где ключами являются имена полей формы, а значениями — очищенные и преобразованные значения полей.
#             user = authenticate(request, username=cd['username'],
#                                 password=cd['password'])#Тут идет проверка, сходятся ли данные полей из cd переменной с теми, что в бд
#             if user and user.is_active: #Если пользователь существует и если он активен, и не заблокирован, тогда идет вход в акканут
#                 login(request, user) #Если пользователь был успешно аутентифицирован, функция login из модуля Django django.contrib.auth используется для входа в систему пользователя. Она принимает два аргумента:
# #
# # • request: объект запроса, содержащий информацию о текущем запросе.
# # • user: объект пользователя, возвращенный функцией authenticate.
#                 return redirect('core:index')
#     else:
#         print('Такого пользователя нет!')
#         form = LoginUserForm()
#
#     return render(request, 'userauth/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('core:index')


def signup(request):
    if request.method == 'POST':
        form = SignUpUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'userauth/signup-done.html')
    else:
        form = SignUpUserForm()
    return render(request, 'userauth/signup.html', {'form': form})


