from django.shortcuts import redirect
from users.forms import UserLoginForm,UserRegForm
from django.contrib.auth import get_user_model,authenticate
from django.http import HttpResponse
from django.contrib.auth import login as user_login,logout as user_logout

# Create your views here.

User = get_user_model()
def login(request):
    data = UserLoginForm(request.POST)
    if not data.is_valid():
        return HttpResponse('数据不合法')
    res = data.cleaned_data
    user = authenticate(**res)
    if user is None:
        return HttpResponse('用户名或密码错误')
        user_login(request,user)
    url_source = request.META['HTTP_REFERER']

    return redirect(url_source)



def logout(request):
    user = user_logout(request)
    url_source = request.META['HTTP_REFERER']
    return redirect(url_source)


def register(request):
    data = UserRegForm(request.POST)
    if not data.is_valid():
        return HttpResponse('数据不合法')
    res = data.cleaned_data
    # 表里面创建用户
    user = User.objects.create_user(**res)
    user_login(request, user)
    url_source = request.META['HTTP_REFERER']
    return redirect(url_source)