"""定义learning_logs的URL模式"""
from django.urls import path
from . import views

urlpatterns = [
    # 主页
    # 这个列表包含可在应用程序learning_logs中请求的网页
    # 第一个参数是一个正则表达式，^让python查看字符串的开头；美元符号让python查看字符串的末尾
    # 这个参数现在就是让python查看开头和末尾之间没有任何东西的URL 即基础URL
    # path('^$', views.index, name='index')
    path('', views.index, name='index'),
    # 显示所有主题
    path('topics/', views.topics, name='topics'),
    # 显示特定主题的页面
    # 发现URL与这个模式匹配时，django会调用视图函数topic()
    path(r"^topics/(?P<topic_id>\d+)/$", views.topic, name='topic')
]
