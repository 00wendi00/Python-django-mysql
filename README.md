# Python-Django
Basic knowledge of Django and mysql

环境: win10  Python3.6.4  Django2.0.6  Pycharm2018.1


-------------------- django 基本页面和mysql的增删改查 --------------------
1. 在项目目录中创建APP--django_mysql, 输入即可自动创建python manage.py startapp django_mysql

2. 在settings中配置DATABASES 和 INSTALLED_APPS

3. 编辑models, 生成数据表python manage.py makemigrations mysqltest, python manage.py migrate mysqltest

4. 编写路由, 并指向工程中的url.py

5. 编写模板index.html和edituser.html,  编写views, 实现简单的增删改查


-------------------- django url路由 + 多数据源(oracle, mysql) --------------------
1. 配置两类url路由--django_mysql.urls , 两套模板两套view , 区分oracle和mysql
http://127.0.0.1:8000/mysql/index/
http://127.0.0.1:8000/oracle/index/

2. 配置数据库路由规则--django_mysql.database_router , 在对应app的models文件中指定app_label

3. 在settings中设置DATABASES数据库, DATABASE_ROUTERS数据库路由, DATABASE_APPS_MAPPING数据库-应用映射

4. 指定应用名称python manage.py makemigrations oracletest(此为appname), 指定数据库同步python manage.py migrate --database db02

