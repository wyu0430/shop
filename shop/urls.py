"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.staticfiles import views
from django.views.static import serve
from shop import settings

urlpatterns = [
    # 后台admin页面url
    url(r'^admin/', admin.site.urls),
    # 展示shop主页面url，跳转到shopapp/urls.py 下面
    url(r'^shop/',include('shopapp.urls')),
    # 加载静态文件js，css
    url(r'^static(?P<path>.*)$', views.serve),
    # 加载media文件，包含图片
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    # 展示user登录和注册页面
    url(r'^user/', include('users.urls')),

    # 展示用户评论页面
    url(r'operations/',include('user_operations.urls')),
]

