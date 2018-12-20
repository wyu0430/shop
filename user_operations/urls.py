from django.conf.urls import url
from user_operations.views import comment


urlpatterns = [
    # 用户评论页面
    url(r'comment/', comment, name='product_comment')


]