from django.urls import path
from .views import logout_user, LoginUser, signup

app_name = 'userauth'
urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('sign-up/', signup, name='signup'),
]