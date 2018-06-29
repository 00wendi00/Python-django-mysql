# Python-Django
Basic knowledge of Django and mysql

环境: win10  Python3.6.4  Django2.0.6  Pycharm2018.1


-------------------- django_mysql 基本页面和mysql的增删改查 --------------------
1. 在项目目录中创建APP--django_mysql, 输入即可自动创建python manage.py startapp django_mysql

2. 在settings中配置DATABASES 和 INSTALLED_APPS

3. 编辑models, 生成数据表python manage.py makemigrations mysqltest, python manage.py migrate mysqltest

4. 编写路由, 并指向工程中的url.py

5. 编写模板index.html和edituser.html,  编写views, 实现简单的增删改查    http://127.0.0.1:8000/index/

