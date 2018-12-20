from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView,DetailView
from shopapp.models import Product,Category
from users.forms import UserLoginForm,UserRegForm
from user_operations.form import CommentForm
from user_operations.models import Comments


# Create your views here.
class Index(TemplateView):
    """
        inedx 主页面
    """
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        # 获取产品表中的产品
        products = Product.objects.order_by('-id')

    # 获取分类表中信息
        category = Category.objects.order_by('id')

# 产品表中的分类信息sql
        MobilePhones = Product.objects.filter(kind__name="Mobile Phones").order_by('id')
        Desktop = Product.objects.filter(kind__name="Desktop").order_by('id')
        Laptop = Product.objects.filter(kind__name="Laptop").order_by('id')
        Accessories = Product.objects.filter(kind__name="Accessories").order_by('id')
        Software = Product.objects.filter(kind__name="Software").order_by('id')
        addtime = Product.objects.filter(kind__name="addtime").order_by('-time')

        # 产品表中获得特色产品
        featureproduct = Product.objects.filter(featureproduct=True)

        # 实例化表单
        login_form = UserLoginForm()
        reg_form = UserRegForm()

        # 返回信息
        kwargs['products'] = products
        kwargs['category'] = category
        kwargs['MobilePhones'] = MobilePhones
        kwargs['Desktop'] = Desktop
        kwargs['Laptop'] = Laptop
        kwargs['Accessories'] = Accessories
        kwargs['Software'] = Software
        kwargs['addtime'] = addtime
        kwargs['featureproduct'] = featureproduct
        kwargs['login_form'] = login_form
        kwargs['reg_form'] = reg_form


        return super().get_context_data(**kwargs)

class Preview(DetailView):
    '''
    每个产品的详细页面
    '''
    # 取到product表的的数据
    queryset = Product.objects.all()
    template_name = 'preview.html'
    # 上面取到的product表数据传给变量'product', 在preview.html页面中显示一个产品的详细信息的时候要用到这个数据produc
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        # 获取分类表中信息
        category = Category.objects.order_by('id')
        # 实例化表单
        login_form = UserLoginForm()
        reg_form = UserRegForm()
        products = Product.objects.order_by('-id')

        # 返回信息
        kwargs['products'] = products
        kwargs['login_form'] = login_form
        kwargs['reg_form'] = reg_form
        kwargs['comment_form'] = CommentForm()
        kwargs['comments'] = Comments.objects.filter(product=kwargs['object'].id).order_by("-time")
        kwargs['category'] = category



        return super().get_context_data(**kwargs)

