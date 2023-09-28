

from django.db import models


#不可能做一个模型写一个代码，所以要定义公共字段把公共字段的代码都抽离出来
class BaseModel(models.Model):
    #将每个表要重复的字段全部抽离出来放在公共类里面，注释掉非公共类里面相同数据
    id = models.AutoField(primary_key=True, verbose_name='id主键', help_text='id主键描述')
    creat_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间描述')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间', help_text='更新时间描述')

    class Meta:
    #在内部类Meta中，一旦指定abstract = True，那么当前模型类为抽象模型类,在迁移时不会创建表，仅仅是为了供其他类维
        abstract = True
