# 1.建立项目
# 1.1制定规范：
# 完整地规范详细说明了项目的目标，阐述了项目的功能，并讨论了项目的外观和用户界面。
# 规范：我们要编写一个名为“学习笔记”的Web应用程序，让用户能够记录感兴趣的主题，并在
# 学习每个主题的过程中添加日志条目。“学习笔记”的主业对这个网站进行描述，并邀请用户注册或登录。

# 1.2建立虚拟环境

# 1.3在django中创建项目，在项目目录下运行，django-admin startproject leanring-log .(最后这个.必不可少)
# 1.4创建数据库python manage.py migrate
# django将大部分与项目相关的信息都存储在数据库中，因此我们需要创建一个供django使用的数据库。
# 1.5查看项目：运行 python manage.py runserver
# 1.6创建应用程序 python manage.py startapp learning_logs
# 1.7定义模型 (即在刚创建的learning_logs文件夹下的models文件中写模型代码)
# 模型告诉django如何处理应用程序中存储的数据，在代码层面模型就是一个类
# 1.8要使用模型，必须将其包含到项目中。方法是打开settings.py(位于learning_log中)
# 1.9接下来要让django修改数据库使其能够存储与模型TOPIC相关的信息。命令：python manage.py makemigrations learning_logs
# 上一行会创建一个迁移文件，接着应用这种迁移，python manage.py migrate
# 每当需要修改“学习笔记”管理的数据时，都采取如下三个步骤：修改model.py;对learning_logs调用makemigrations;让django迁移
# 1.10 django管理网站
# django提供的管理网站让你能够轻松处理模型，网站的管理员可使用管理网站，但普通用户不行。我们接下来建立管理网站
     # 1.10.1创建超级用户 python manage.py createsuperuser(只能用命令行)
     # 1.10.2向管理网站注册模型 django自动在管理网站中添加了一些模型如user和group，但对于我们创建的模型必须手动注册
     # 我们创建learnning_logs时，django在models.py所在的目录中创建了一个名为admin.py的文件。更改他
     # 使用超级用户访问管理网站（localhost:8000/admin）
     # 1.10.3添加主题
# 1.11定义模型entry
# 要记录学到的国际象棋和攀岩知识，需要为用户可在学习笔记中添加的条目定义模型。每个条目都与特定主题相关联，
# 这种关联被称为多对一关系，即多个条目关联到同一个主题。
# 1.12迁移模型entry
# 1.13向管理网站注册entry(admin.py中添加两行)
# 1.14django shell
# 输入一些数据后，就可通过交互式终端会话以编程方式查看这些数据了。这种交互式环境叫做django shell是测试项目和排除故障的
# 理想之地。命令：python manage.py shell

# 1.15创建网页：学习笔记主页
# 使用Django创建网页的过程通常分三个阶段：定义URL，编写视图和编写模板。
# 首先你必须定义URL模式：每个URL都被映射到特定的视图--视图函数获取并处理网页所需的数据。（更改项目文件夹中的urls.py）
# 这一步还需要在应用程序文件夹新建立urls.py
# 1.16编写视图：视图函数接收请求中的信息，准备好生成网页所需的数据，再将这些数据发给浏览器（更改views.py）
# 1.17编写模板:模板定义了网页的结构。制定了网页是什么样子的。在应用程序文件夹下新建一个文件夹，命名templates
# 1.18模板继承:创建网站时，几乎都有一些所有网页都将包含的元素，在这种情况下，可编写一个包含通用元素的父模板，并让
# 每个网页都继承这个模板。
