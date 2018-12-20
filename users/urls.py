from django.conf.urls import  url
from users.views import login,logout,register

urlpatterns = [
    # users/urls 里面负责用户登录，注销，注册的url

    url(r"login",login,name='user_login'),
    url(r"logout",logout,name='user_logout'),
    url(r"register",register,name='user_register'),



]