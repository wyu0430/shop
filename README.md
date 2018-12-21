# shop项目介绍

该项目为在django框架搭建的电子商品专卖的网站

演示站 http://132.232.148.234:9000/shop/index/

#### 1. 模块说明

shopadd目录 是index页面和详情页面preview的相关应用

users目录是用户登录注册相关应用

user_operations是用户评论相关应用

shop是主目录，主要是settings配置文件和urls路由到其他模块

#### 2. 数据表

目前主要使用的表：

1. shopadd模块models.py下定义：shopapp_producnt 商品表，shopapp_category 商品分类表

2. 默认表auth_user 

3. user_operations模块models.py下定义user_operations_comments 用户评论表

#### 3. 项目启动

在项目路面下运行

python manage.py runserver 127.0.0.1:8005



#### 4. 目前功能

#### 1.实现2个页

/shop/index/ 主要页面

shop/preview/4 商品详页面

#### 2. 页面功能

##### index 主页面：

主页面categories分类菜单从数据库中调用分类表

页面new production分类 依次 调用数据库产品表中添加时间最近的商品显示（显示图片，名称，价格）

页面feature products分类 依次 调用数据库产品表中featureproduct自动是true的产品显示（显示图片，名称，价格）

#### preview详情页面

在主页面点击任何商品进入该商品的详情页面

preview页面显示该商品的价格，描述，图片，名称

##### 评论功能

preview页面显示该商品的评论，登录用户可以针对某一个商品发布一次评论

##### 登录注册功能

在index页面和preview页面含有登录注册功能



















