from django.db import models
from django.contrib.auth import get_user_model
from shopapp.models import Product
from django.utils.timezone import now

# Create your models here.

User = get_user_model()

'''
创建用户评论表
'''
class Comments(models.Model):
    user = models.ForeignKey(User,verbose_name='评论用户',on_delete=None,null=True)
    product = models.ForeignKey(Product,verbose_name='产品评论',on_delete=None,null=True)
    content = models.TextField(max_length=2000,verbose_name='评论的内容')
    time = models.DateTimeField(default=now,verbose_name='评论的时间')

    def __str__(self):
        return '用户:{}，对产品:{}的评价'.format(self.user.id,self.product.name)


    class Rname:
        verbose_name = '产品评论'
        verbose_name_plural = verbose_name
        unique_together = ("user", 'product')
