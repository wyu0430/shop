from django.conf.urls import url
from shopapp.views import Index,Preview





urlpatterns = [
    # url index 页面
    url(r'^index/',Index.as_view(),name='shop_index'),
    # url到preview页面
    url(r'^preview/(?P<pk>\d+)$', Preview.as_view(), name='product_preview'),


]

