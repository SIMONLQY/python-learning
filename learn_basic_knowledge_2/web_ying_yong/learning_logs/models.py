from django.db import models


# Create your models here.
class Topic(models.Model):
    """用户学习的主题"""
    # 添加两个属性text和date_added
    # text是一个文本组成的数据，这里储存主题名字
    text = models.CharField(max_length=200)
    # date_added是一个记录日期和时间的数据，参数为true让用户在每次创建topic时候记录时间
    # 要知道更多类似的东西可以参阅djano model field refeence
    date_added = models.DateTimeField(auto_now_add=True)
    # 我们需要告诉django默认使用哪个属性来显示有关主题的信息
    def __str__(self):
        """返回模型的字符串"""
        return self.text

class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    # 加上外键作为关联表，on_delete参数这个值表示删除关联表则这个也删除
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    # Meta存储用于管理模型的额外信息，在这里可以设置一个特殊属性让django在需要时用entries来表示多个条目。
    # 如果没有这个类，django将自动用Entrys来表示多个条目。
    class Meta:
        verbose_name_plural = 'entries'
    def __str__(self):
        """返回模型的字符串"""
        return self.text[:50]+"..."
