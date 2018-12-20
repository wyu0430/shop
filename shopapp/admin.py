from django.contrib import admin
from shopapp.models import Category,Product

# Register your models here.
# 增加产品信息表到后台管理页面

class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product,ProductAdmin)

# 增加产品分类表到后台管理页面

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category,CategoryAdmin)