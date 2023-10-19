from django.db import models

# Create your models here.
from utils.base_model import BaseModel

class Animal(models.Model):
    """
    1)一般在子应用models. py中定义模型类(相当于数据库中的一张表)
    2)必须继Model或青Model的子类
    3)在模型类中定义类属性(必须得为Field于类)相当于数据表中字段
    4) CharField ---》 varchar
       IntegerField ---> integer
       BooleanField ---》 bool
    5)在migrations里，存放迁移脚本:
        python manage.py makemigrations 子应用名称（如果不指定子应用名，会把所有于应用生成迁移脚本）
    6)查询迁移脚本生成的SQL语句: python manage.py sqlmigrate 于应用名 迁移脚本名 (无需加.  py)
    7)生成的数据表名称默认为: 子应用名_模型类名小写
    8)默认会自动创建一个名为id的自增主键


    """
    # varchar
    name = models.CharField(max_length=50)
    age =models.IntegerField()
    gengder = models.BooleanField()

#class Projects(models.Model):
class Projects(BaseModel):
    # 默认会自动生成一个主键id，
    # 如果想要自己定义
    # 在一个模型类中仅仅只能为一个宇段指定primary_key = True
    # 一旦在模型类中的某个宇段上指定了primary_key = True，那么ORM框架就不会自动创建名称为id的主链
    #ids = models.IntegerField(primary_key=True,verbose_name='项目主键',help_text='项目主键描述')

    #AutoField：
    #AutoField是Django的一个模型字段，它会自动为你的模型生成一个唯一的整数ID。这个ID是自动增加的，
    #每当添加新的记录时，ID就会增加。你可以把这个字段看作是数据库表中的自增ID列。
    #在你给出的代码中，primary_key = True意味着这个字段是表的主键，verbose_name = 'id主键'
    #是这个字段在Admin界面中的显示名称，help_text = 'id主键描述'
    #是这个字段在Admin界面中的帮助文本。
    # id = models.AutoField(primary_key=True, verbose_name='id主键', help_text='id主键描述')

    # a.CharField类型必须指定maxlength参数(改字段的最大宇节数)
    # b.如果需要给一个字添加唯一约束，unique = True(默认为False)
    name = models.CharField(max_length=20,verbose_name='项目名称',help_text='项目描述',unique=True)

    leader = models.CharField(max_length=10, verbose_name='项目负责人', help_text='项目负责人描述')

    # c.使用default指定默认值(如果指定默认值后，在创建记录时，改字段传递，会使用默认值
    is_execute = models.BooleanField(verbose_name='是否启动项目', help_text='项项目启动描述',default=True)

    #dnul1=True指定前端创建数据时，可以指定该字为nu11，默认为nul1=False,DRF进行反序列化器输入时才有效
    #e.blank =True指定前端创建数据时，可以指定该宇为空字符串，默认为blank=False,DRF进行反序列化器输入时才有效
    desc = models.TextField(verbose_name='是否启动项目', help_text='项项目启动描述',null=True,blank=True,default='')

    #models.DateTimeField是Django模型字段的一种，用于存储日期和时间。
    #字段参数auto_now_add=True表示当对象第一次被创建时，该字段会被自动设置为当前日期和时间。对于已存在的对象，如果该字段被设置为auto_now_add=True，则其值不会被改变。
    #字段参数auto_now=True表示每次对象被保存时，该字段都会被自动设置为当前日期和时间。这意味着，无论何时你更新该对象，这个字段都会反映出更新的时间。
    creat_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间', help_text='创建时间描述')
    update_time = models.DateTimeField(auto_now=True,verbose_name='更新时间', help_text='更新时间描述')

    #创建一个内部类
    #h.可以在任意一个模型类中创建Meta内部类，用于修改数据库的元数据信息
    class Meta:
        # i.db_table指定创建的数据表名称
        db_table = 'tb_projects'
        # 为当前数据表设置中文描述信息
        verbose_name = '项目表'
        verbose_name_plural = '项目表'

        #数据库排序
        ordering = ['id']

    def __str__(self):
        return f"Projects({self.name})"