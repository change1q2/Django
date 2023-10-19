from django.db import models

# Create your models here.
from projects.models import Projects

from utils.base_model import BaseModel
#表与表之间有哪些关系?
# Projects与Interfaces表，一对多关系

#学生表与学生详细信息表，一对一关系

#学生表与课程表，多对多的关系




class Interfaces(BaseModel):
   # id = models.AutoField(primary_key=True,verbose_name='id主键',help_text='id主键描述')

    #代码片段是Django框架的模型字段定义，定义一个名为name的字段，它是一个字符字段（CharField），最大长度为20。
    # verbose_name参数用于在Django admin界面中显示更友好的名称，而help_text参数则用于提供关于该字段的更多信息或描述。
    # unique=True表示这个字段的值在整个表中必须是唯一的。
    name = models.CharField(max_length=20, verbose_name='接口名称', help_text='接口名称描述',unique=True)

    tester = models.CharField(max_length=10, verbose_name='测试人员', help_text='测试人员描述')

    #建立表的一对多的关系

    #方式1:定义一个名为projects的字段，它是一个外键字段（ForeignKey），
    #指向Projects模型。在Django中，外键字段用于在模型之间创建关系，这种情况下，projects字段表示当前模型与Projects模型之间的关联。
    #projects = models.ForeignKey(Projects)

    #方式2:定义一个名为projects的字段，它是一个外键字段（ForeignKey），
    # 指向projects.Projects模型。在Django中，外键字段用于在模型之间创建关系，
    # 这种情况下，projects字段表示当前模型与projects.Projects模型之间的关联。

    #与之前的代码片段相比，这个代码片段指定了外键字段所关联的模型的全路径，
    # 即projects.Projects。这样做可以避免命名冲突，并确保正确引用了所需的模型。
    #relasted_name='inter'

    projects = models.ForeignKey('projects.Projects',on_delete=models.CASCADE,verbose_name='所属项目',help_text='所属项目描述',
                                 related_name='interfaces_set')
  #  creat_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间描述')
  #  update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间', help_text='更新时间描述')

    """
    总结：
    # a.如果需要创建一对多的外键，那么会在“多”的那一个模型类中定义外键字段
    # b.如果创建的是一对多的关系，使用ForeignKey
    # c.如果创建的是一对一的关系，可以在任何一个模型类使用OneToOneField
    # d.如果创建的是多对多的关系，可以在任何一个模型类使用ManyTolanyField
    # e.ForeignKey第一个参数为必传参数，指定需要关联的父表模型类
        方式一:  直接使用父表模型类的引用
        方式二:  可以使用”子应用名称.父表模型类名’（推荐）
    # f. ForeignKey需要使用on_delete指定级联删除策略
            # CASCADE: 当父表数据删除时，相对应的从表数据会被自动删除
            # SETNLL: 当父表数据删除时，相对应的从表数据会被自动设置为nul1值
            # PROTECT:当义表数据删除时，如果有相对应的从表数据会抛出异常
            # SET DEFAULT:当父表数据删除时，相对应的从表数据会被自动设置为默认值，还需要额外指定default=True
    # projects = models. Foreignkey(Projects)
    # models. ManyToManyField
    
    """

    class Meta:
        # i.db_table指定创建的数据表名称
        db_table = 'tb_interfaces'
        # 为当前数据表设置中文描述信息
        verbose_name = '接口表'
        verbose_name_plural = '接口表描述'

        # 数据库排序
        ordering = ['id']

    def __str__(self):
        return f"Interfaces({self.name})"