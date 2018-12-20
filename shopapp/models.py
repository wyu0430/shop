from django.db import models
from datetime import datetime
from uuid import  uuid4

# Create your models here.


def upload_image(instance,filename):
    '''

    :param instance:
    :param filename:
    :return: 处理上传的产品图片名称
    '''
    time = datetime.now()
    image_end = filename.split('.')
    res_filename = uuid4().hex
    return '{}/{}/{}.{}'.format(time.year, time.month, res_filename, image_end[-1])


class Category(models.Model):
    '''
    创建产品分类表
    '''
    name = models.CharField(max_length=20, verbose_name='分类名称')

    def __str__(self):
        return self.name

    class Rname:
        '''
        表名为产品分类表
        '''
        verbose_name = '产品分类'
        verbose_name_plural = verbose_name



class Product(models.Model):
    '''
    创建产品表，定义产品字段
    '''
    name = models.CharField(max_length=50,verbose_name='产品名字')
    image = models.ImageField(upload_to=upload_image, blank=True)
    price = models.IntegerField(verbose_name='产品价格')
    description =models.CharField(max_length=200,verbose_name='产品描述')
    addtime = models.DateField()
    # 产品表中的外键，关联产品分类表的分类名称
    kind = models.ForeignKey(Category, verbose_name='产品分类', on_delete=None, default=None, null=True)
# 是否是特色产品字段
    featureproduct = models.BooleanField(choices=((True,'是'), (False, '否')), default=True, verbose_name='特色产品')


    def __str__(self):
        return self.name

    class Rname:
        '''
        表的名称为产品信息表
        '''
        verbose_name = '产品信息'
        verbose_name_plural = verbose_name



