from django.db.models import Q, Count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import path
import json
from django.db import connection
from interfaces.models import Interfaces
from .serializers import ProjectSerilizer
# 在view创建的函数属于视图函数
from django.views import View
from .models import Projects


def index(request):
    return HttpResponse("欢迎测试开 发")


#
# def projects(request):
#
#    return HttpResponse("欢迎测试项目")
#
# # def get_project(request):
# #    return HttpResponse("<h1>获取一个项目信息</h1>")
# #
# # def creat_project(request):
# #    return HttpResponse("<h1>创建一个项目</h1>")
# #
# # def put_project(request):
# #    return HttpResponse("<h1>更新一个项目</h1>")
# #
# # def delete_project(request):
# #    return HttpResponse("<h1>删除一个项目</h1>")
# #
# #
# # def get_projects(request,pk):
# #    return HttpResponse(f"<h1>获取项目{pk}信息</h1>")
# #
# # def projects1(request,):
# #    return HttpResponse(f"<h1>获取projects1项目信息</h1>")
# #
# # def projects(request):
# #    """
# #    视图函数
# #    a.试图函数的第一个参数是HttpRequest对象
# #    b.HttpRequest对象包含请求的所有数据（请求头，请求体 ）
# #    c。试图函数必须得返回一个HttpResponse对象或者其子类对象
# #
# #    :param request:
# #    :return:
# #    """
# #    # print(request)
# #    # print(type(request))
# #    # print(type(request).__mro__)
# #    #
# #    # return HttpResponse(f"<h1>获取projects项目信息</h1>")
# #
# #    if request.method == 'GET':
# #       return  HttpResponse("<h1>获取项目信息get</h1>")
# #    elif request.method == "POST":
# #       return HttpResponse("<h1>获取项目信息post</h1>")
# #    elif request.method == "PUT":
# #       return HttpResponse("<h1>获取项目信息put</h1>")
# #    elif request.method == "DELETE":
# #       return HttpResponse("<h1>获取项目信息del</h1>")
# #    elif request.method == "PATCH":
# #       return HttpResponse("<h1>获取项目信息path</h1>")
# #    else :
# #       return HttpResponse("<h1>项目的其他操作</h1>")
#
#
#
# #使用类视图，管理庞大的代码量
# #1.注意点使用类视图一定要继承View从Django导入就行
# class ProjectcView(View):
#    """
# #    一、定义类视图
# #    1.继承View或者View子类
# #    2.不的请求方法有相应的方法进行对应
# #       GET  -> get
# #       POST -> post
# #       DELETE -> delete
# #       PATCH -> patch
# #    3.每一个处理请求的方法，必须得返回HttpResponse对象或者HttpResponse于类对象
# #    4.每一个处理请求的方法，第二个参数必须为HttpRequest对象
# #    """
#
#    def get(self,request,pk):
#
#       '''
#       project_data = {
#          'id': 1,
#          'name': 'XX项目',
#          'leader': '盼盼但'
#       }
#       json_str = json.dumps(project_data,ensure_ascii=False)
#       return  HttpResponse(f"<h1>获取项目{pk}信息get</h1>")
#       '''
#    #
#    #
#    #    project_data_list = [
#    #       {
#    #          'id': 1,
#    #          'name': 'XX项目1',
#    #          'leader': '盼盼但1'
#    #       },
#    #       {
#    #          'id': 2,
#    #          'name': 'XX项目2',
#    #          'leader': '盼盼但2'
#    #       },
#    #       {
#    #          'id': 3,
#    #          'name': 'XX项目3',
#    #          'leader': '盼盼但3'
#    #       },
#    #
#    #    ]
#    #
#    #    #5.HttpResponse
#    #    #a.HttpResponse第一个参数为字符串类型(需要返回到前端的字符串数据)
#    #    #b.content_type可以指定啊应头中的Content-Type零数
#    #    #c.status可以指定响应状态码
#    #
#    #    #将字典转化成字符串dumps,将字符串转化成json,load
#    #
#       #json_str = json.dumps(project_data,ensure_ascii=False)
#
#       #return  HttpResponse(f"<h1>获取项目{pk}信息get</h1>")
#    #
#    #  #  return HttpResponse(json_str,content_type='application/json'，status=200)
#    #
#    #    #6.JsonResponse
#    #    #  a.HttpResponsez子类
#    #    #  b.用于返回json数据
#    #    #  c.第一个参数可以直接传递字典或者嵌套宇典的列表
#    #    #  d.默认添加content_type为application / json
#    #    #  e.默认第一个参数只能为字典，如果为嵌套字典的列表，要设置safe = False
#    #    #return JsonResponse(project_data,json_dumps_params={'ensure_ascii':False})
#    #
#    #    #7.两种开发模式
#    #    #  1.前后端不分离的开发模式
#    #    #  a.后端如果返回的是一个完整的html 页面(页面中有填充数据)
#    #
#    #    #  2.前后端分离的开发模式
#    #    #  a.后端如果返回的是数据 (josn、xml)
#    #    return JsonResponse(project_data_list, json_dumps_params={'ensure_ascii': False},status=200,safe=False)
#    #
#
#    # 处理数据库中的数据
#    """
#      # 一、创建（C）
#         #方式一：1.先创建一个数据，再进行保存
#            #  a.直接使用模型类(字段名1=值1， 字段名2 = 值2，...)，来创建模型类实例
#            #  b.必须模型实例调用save （）方法，才会执行sq1语句
#         # obj = Projects(name='在线图书项目',leader='多喝热水' )
#         # obj.save()
#         # return HttpResponse(f"<h1>获取项目信息{pk}</h1>")
#
#         #方式二：直接创建不需要保存
#            # a使用模型类 objects返回manager对象
#            # b.使用manager对象.create(字段名1=值1，字段名2=值2，...)，来创建模型类实例
#            # c.无需使用模型实例调用save ()方法，会自动执行sql语句
#            """
#    # 一、创建（C）
#
#    #   obj = Projects.objects.create(name='在线图书项目2',leader='多喝热水' )
#    #
#    #   return HttpResponse(f"<h1>获取项目信息{pk}</h1>")
#
#    """
#     # 二、读取(R)
#     # 1、读取多条数据
#     #读取数据库中所有数据
#       # a.使用模型类 objects.a10，会将当前模型类对应的数据表中的所有数据读取出来
#       # b.模型类objects.a110，返回QuerySet对象(查询集对象)
#       # c. QuerySet对象，类似于列表，具有性查询的特性(在用’数据时，才会执行sq1语句)
#       # qs = Projects.objects.all()
#
#    # 2、读取单条数据
#    # 方式一:
#       # a.可以使用模型类 objects.get(条件1=值1)
#       # b.如果使用指定条件查询的记灵数量为0，会地出异常
#       # c.如果使用指定条件查询的记录数量超过1，也会抛出异常
#       # d.最好使用有唯一约束的条件去查询
#       # e.如果使用指定条件查询的记录数量为1，会返回这条记录对应的模型实例对象，可以使用模型对象，字段名去获取相应的字段值
#       """
#
#    # 二、读取(R)
#    # 方式1：
#
#    # obj = Projects.objects.get(id=1)
#    # print(obj)
#    # return HttpResponse(f"<h1>获取项目信息{pk}</h1>")
#
#    """
#    # 方式二:
#       # a可以使用模型类 objectsfilter(条件1=值1)，返回QuerySet对象
#       # b.如果使用指定条件查询的记录数量为0，会返回空的QuerySet对象
#       # c.如果使用指定条件查询的记录数量超过1，将符合条件的模型对象包裹到QuerySet对象中返回
#       # d. QuerySet对象，类似于列表，有如下特性:
#          # 1)支持通过数值(正整数)索引取值
#          # 2)支持切片作(正整数)
#          # 3)获取第一个模型对象: QuerySet对象.first ()
#          # 4)获取最后一个模型对象: QuerySet对象last ()
#          # 5)获取长度: len(QuerySet对象)、QuerySet对象count ()
#          # 6)判断查询集是否为空: QuerySet对象exists ()
#          # 7)支持选代作(for环，每次环返模型对系
#     # e.ORU框架中，会给每一个灰型类中的主键设置一个别名(pk)
#    """
#
#    # 方式2：
#
#    # qs = Projects.objects.filter(id=1)
#    # Projects.objects.filter(id_gt=1)
#
#    """
#    # filter方法支持多种查询类
#    # filter方法支持多种查询类型
#    # 1)字段名_查询类型=具体值
#    # 2)字名_exact=具体值，缩写形式为:名=具体值
#    # 3)字段名_gt:大于、字段名_gte: 大于等于
#    # 4)字段名_It:小于、字段名_Ite: 小于等于
#    # 5) contains:包含
#    # 6) startswith:xxx开头
#    # 7)endswith:以xxx结尾
#    # 8)isnul1:是否为null
#    # 9)一般在查询类型前添加“i”，代表忽略大小写
#
#    # exclude为反向查询，filter方法支持的所有查询类型，都支持
#
#    """
#    # qs = Projects.objects.filter(id=1)
#
#    # 创建从表数据
#    # 外键对应的父表如何传递?
#    # 方式一:
#    # 1)先获取父表模型对象
#    # 2)将获取的父表模型对象以外键字段名作为参数来传递
#    # project_obj = Projects.objects.get(name='在线图书项目')
#    # interfaces_obj = Interfaces.objects.create(name='在线图书项目-登录接口',tester='珍惜',
#    #                                            projects=project_obj)
#
#    # 方式二:
#    # # 1)先获取父表模型对象，进而获取父表数据的id值
#    # # 2)将父表数据的主键值以外键名_id作为参数来传递
#    # project_obj = Projects.objects.get(name='在线图书项目')
#    # interfaces_obj = Interfaces.objects.create(name='在线图书项目-登录接口', tester='珍惜',
#    #                                            projects=project_obj.id)
#
#    # a.通过从表模型对象(已经获取到了)，如何获取父表数据
#    # 可以通过外键字段先获取义表模型对象
#    # interface_objprojects，返回父表模型对象
#    # interface_obj = Interfaces.objects.get(id=1)
#
#
#    # b.通过父表模型对象(已经获取到了)，如何获取从表数据?
#    #  默认可以通过从表模型类名小写_set，返回manager对象，可以进一步使用filter进行过虑
#    #  如果在从表模型类的外键宇段指定了related name参数，那么会使用related name指定参数作为名称
#    # project_obj = Projects.get(id=1)
#    # project_obj.interfaces_set.all()
#
#    # c.如果想要通过父表参数来获取从表数据、想要通过从表参数获取父表数据 --- 关联查询
#    # 可以使用关联查询语句:
#    # 关联字段名称_关联模型类中的字名称_查询类型
#    # Interfaces. objects. filter(projects namecontains= xxx
#    # Projects.objects.filter(interfaces name contains='警灵
#
#    #interface_obj.projects.name
#
#    #  d.逻辑关系
#    # 与关系
#    # 方式一:
#    #在同一个filter方法内部，添加多个关键字参数，那么每个条件为“与”的关系
#
#    # 方式二
#    # 可以多次调用filter方法，那么filter方法的条件为“与”的关系 --- QuerySet链式调用特性
#
#    # qs = Projects.objects.filter(name__contains='2',leader='keyou')
#
#
#    #或关系
#    #  可以使用Q查询，实现逻辑关系，多个Q对象之间如果使用“/",那么为“或”关系
#    #qs = Projects.objects.filter(Q(name__contains='2') | Q(leader = '多喝热水'))
#
#    # e.排序 (QuerySet)
#    # 可以使用QuerySet对象 (manager对象).order_by( 字名1，，宇名2，，-字段名3’)
#    # 默认为ASC升序，可以在字名称前添加“_”，那么为DESC隆序
#    # Projects.objects.filter(Q(name__contains='2') | Q(leader='多喝热水')).ORDER_BY('name')
#
#    #三、更新操作
#    #方式一：更新一条数据
#    # project_obj = Projects.objects.get(id=1)
#    # project_obj.name = '在线图书项目1'
#    # project_obj.leader = '不语'
#    # project_obj.save()
#    '''
#
#    # 1)必须调用save方法才会执行sql语句，并且默认进行完整更新
#    # 2)可以在save方法中设置update_fields参数(序列类型)，指定需要更新的字名称(字符中)
#    # project obi save ()
#     '''
#
#    #方式二:更新多条数据
#    # Projects. objects. filter; QuerySet
#    # 可以在QuerySet对象.update(字名称=’字段值’)，返回修改成功的值,无需调用save方法
#    # qs = Projects.objects.filter(name__contains='2').update(leader='珍惜')
#
#    #四、删除数据
#    #方式一：删除一条数据
#
#
#    #方式二:删除多条数据
#
#
#
#    #obj = Projects.objects.filter(name__contains='2').delete()
#
#    #聚合运算
#    #a.可以使用QuerySet对象aggregate(聚合函数(字段名’))方法，返回字典数据
#    #b.返回的字典数据中key为字段名_聚合函数名小写
#    #c.可以使用关键字参数形式，那么返回的字典数中key为关键字参数名
#
#    # qs = Projects.objects.filter(name__contains='2').aggregate(Count('id'))
#
#    #分组查询
#    # a.可以使用QuerySet对象 values(父表主键id).annotate(聚合函数(从表模型类名小写’))
#    # b.会白动连接两张表，然后使用外键字作为分组条件
#
#    # 查询集QuerySet对象有什么特性?
#    # 1)支持链式调用:可以在查询集上多次调用filter、exclude方法
#    # 2)性查询:仅仅在使用数时才会执行sl语句，为了提开数读写性能
#    # 会执行sgI语句的场景: len0、.count 0、通过案引取值、print、for
#    # qs = Projects.objects.values('id').annotate(interfaces=Count('interfaces'))
#
#
#
#    def post(self,request,pk):
#       # 前端参数解析
#       # #前端传递参数的方式
#       # 1.路径参数
#       #  a.在ur1路径中传递的参数
#       #  b.在请求实例方法中，使用关键字参数来接收
#       #
#       # 2.查询字符串参数
#       #  a.url ? 后面的key value键值对参数，如: http://ww xxx com/?keyl=valuel&key2=value2
#       # ` b.request.GET获取
#       #  c.request.GET返回QueryDict，类似于python中dict类型
#       #  d.可以使用[key1’]、get(key1’)，会返回具体的值，如果有多个相同key的键值对，获取的是最后一行的内容
#       #  e.egetlist(key’)，获取相同key的多个值，返回list类型
#       #
#       # 请求体参数
#       # 1. json
#       #  a.json格式的参数会存放在body中，一般为字节类型
#       #  b.json.loads(request.body)，返回Python中的数据类型(字典、族套字典的列表)
#       #
#       # 2.www-formurlencoded
#       # a.一般在前端页面中使用表单灵入的参数
#       # b.request.POST返回QueryDict，类似于python中dict类型
#       #
#       #
#       # 3. file
#       # a.传递文本参数可以使用request.POST去提取
#       # b.传递的非文本零数(二进制文件)可以使用request.FILES去提取
#       # c.如果传递纯粹的文件，request.body去提取
#       #
#       # 请求参数
#       #  a.第一种方式:request.headers['key1’]或者get( keyI')
#       #  b.第二种方式: request.META['HTTPAUTHORIZATIONJ
#       #     1)请求头参数的可以被转化为: HTTP参数名大写
#       #     2)如果参数名中含有-，会自动转换为_
#       return HttpResponse("<h1>获取项目信息post</h1>")
#
#    def put(self,request):
#       return HttpResponse("<h1>获取项目信息put</h1>")
#
#    def delete(self,request):
#       return HttpResponse("<h1>获取项目信息del</h1>")


# 模拟一个需求
# 需求:
# 1、获取一条项目数据
#   GET /projects/<int:pk>/
# 2、获取所有项目数据
#  GET /projects/
# 3、创建一条项目数据
#  POST /projects  将项目数据以json的形式来传递
# 4、更新一条项目数据
#  PUT / projects / < int: pk > /  新的项目数据以json的形式来传递
# 5、删除一条项目数据
#  DELETE / projects / < int;pk >

class ProjectsView(View):
    '''


    # 2、获取所有项目数据
    #  GET /projects/
         数库作(读取所有项目数据) -》序列化输出操作(将模型对象转化为Python中的基本类型)

    # 3、创建一条项目数据
    #  POST /projects  将项目数据以json的形式来传递
    数据校验(规范传入的参数) -》反序列化输入作(将son式的数据转化为复杂的类型) -》数据库作(创建项目数据）
     -》序列化输出操作(将模型对象转化为Python中的基本类型)

  '''

    # 获取所有数据
    def get(self, request):
        # a.获取所有项目数据
        queryset = Projects.objects.all()

        # project_list = []
        # item:Projects #加一个注释，著时候才能显示出来
        # for item in queryset:
        #    #基础模式
        #    # project_dict = {
        #    #    'id': item.id,
        #    #    'name': item.name,
        #    #    'leader': item.leader
        #    # }
        #    # project_list.append(project_dict)
        #
        #    #简化模式
        #    # b.将项目的查询集数据转化为套字典
        #    project_list.append ({
        #       'id': item.id,
        #       'name': item.name,
        #       'leader': item.leader
        #    })

        # 列表推导式:读取快，性能差
        # project_list= [ {
        #    'id': item.id,
        #    'name': item.name,
        #    'leader': item.leader
        # }for item in queryset]
        # return如果在for循环里面智慧获取第一条数据，要放在跟for同一个位置才能获取全部数据

        # return JsonResponse(project_list, safe=False)

        # 使用序列化操作代替

        # 三、序列化器的使用
        # 1.可以使用序列化器进行序列化输出操作
        # a.创建序列化器对象
        # b.可以将模型对象或者查询集对象、普通对象、
        # c.如果传递的是查询集对象、套普通对象的列表(多条数据)，必须得设置many=True# d如果传递的是模型对象、普通对象，不需要设置many=True
        # e.可以使用序列化器对象的. data属性，获取序列化器之后的数据(宇典、套字典的列表)

        serializer = ProjectSerilizer(instance=queryset, many=True)

        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        # 1、获取json参数并转化为python中的数据美型(字典)
        try:
            python_data = json.loads(request.body)
        except Exception as e:
            return JsonResponse({'msg': '参数异常'}, status=400)
        # 2、需要进行大量的数据校验
        # a需要校验必传参数是否有传递
        # b.传递的有唯一约束的参数是否已经存在
        # c.必传参数的长度是否超过限制

        # 3、创建数据
        # project_obj = Projects.objects.create(name=python_data.get('name'),
        #                         leader=python_data.get('leader'),
        #                         is_execute=python_data.get('is_execute'),
        #                         desc=python_data.get('desc'))
        #

        # 3.1创建数据简单写法

        # 四、反序列化操作
        '''
        # 1.定义序列化器类，使用data健字参数传递宇典参数
        # 2.可以使用序列化器对象调用is_valid0方法，才会开始对前输入的参数进行校验
        # 3.如果校验通过is_valid0方法返回True，否则返回False
        # 4.如果调用.is_valid0方法，添加raise_exeception=True，校验不通过会抛出异常，否则不会抛出异常
        # 5.只有在调用.is_valid(方法之后，才可以使用序列化器对象调用.errors属性，来获取错误提示信息(字典类型)
        # 6.只有在调用. is_valid0方法之后，才可以使用序列化器对象调用validateddata网性，来获取校验通过之后的数据
            与使用json.load转化之后的数据有区别
  
  
        '''
        serializer11 = ProjectSerilizer(data=python_data)
        # 对数据进行校验

        if not serializer11.is_valid():
            return JsonResponse(serializer11.errors, status=400)

        # project_obj = Projects.objects.create(**python_data)

        # 要获取返回值的话，需要获取反序列化的返回值
        #project_obj = Projects.objects.create(**serializer11.validated_data)
        '''
        #1、如果在创建序列化器对象时，仅传递data参数，使用序列化器对象调用save方法时，会自动调用序列化器中的create方法
        #2、create方法用于对数据进行创建操作
        #3、序列化器类中的create方法，validated data参数为校验通过之后的数据 (一般宇典类型)
        #4、在调用save方法时，可以传递任意的关键字参数，并且会自动合并到validated_data宇典中
        #5、create方法一般需要将创建成功之后模型对象返回
        '''

        serializer11.save(myname='珍惜',myage=18)

        '''
        
      
        # 4、将创建成功的数据返回给前端
        # python_dict = {
        #     'id': project_obj.id,
        #     'name': project_obj.name,
        #     'msg': '创建成功'
        #  }

        # return JsonResponse(python_dict,status=201)
        '''
        #序列化操作

        # serializer = ProjectSerilizer(instance=project_obj)
        #
        # return JsonResponse(serializer.data, status=201)

        '''
        #1、在创建序列化器对象时，仅仅只传递data参数，那么必须得调用is_valid()方法通过之后如果没有调用save方法，使用创建序列化器对象data属性，来获取序列化输出的数据
        #2、 如果没有调用save方法，使用创建序列化器对象.data属性，来获取序列化输出的数据
            (会把validated data数据作为输入源，参照序列化器字的定义来进行输入)日
        #3、如果调用了save方法，使用创建序列化器对象data属性，来获取序列化输出的数据
            (会把create方法返回的模型对象数据作为输入源，参照序列化器字段的定义来进行输出)
        '''


        return JsonResponse(serializer11.data, status=201)


class ProjectDetailView(View):
    '''
    把地址相同的放在一个路由里面

    # 1、获取一条项目数据
    #   GET /projects/<int:pk>/
       数据校验(规范传入的参数) -》数据库作(读取一条项目数据) -》序列化输出操作(将模型对象转化为python中的基本类）

    # 4、更新一条项目数据
    #  PUT / projects / < int: pk > /  新的项目数据以json的形式来传递

     数据校验(规范传入的参数) -》反序列化输入作(将son式的数据转化为复杂的类型) -》数据库作(创建项目数据）
     -》序列化输出操作(将模型对象转化为Python中的基本类型)

    # 5、删除一条项目数据
    #  DELETE / projects / < int;pk >

     数据校验(规范传入的参数) -》数据库作(读取一条项目数据)

  '''

    def get(self, request, pk):
        # 1、需要校验pk在数据库中是否存在

        # 2、从数据库中读取项目数据
        try:
            project_obj = Projects.objects.get(id=pk)
        except Exception as e:
            return JsonResponse({'msg': '参数异常'}, status=400)
        '''
        # 3、将读取的项目数据转化为字典
        # python_dict = {
        #     'id': project_obj.id,
        #     'name': project_obj.name,
        #     'msg': '获取项目数据成功'
        # }
        # return JsonResponse(python_dict)
        '''
        # 3.1使用序列化操作
        serializer = ProjectSerilizer(instance=project_obj)

        return JsonResponse(serializer.data)

    def put(self, request, pk):
        # 1、需要校验pk在数据库中是否存在

        # 2、从数据库中读取项目数据
        try:
            project_obj = Projects.objects.get(id=pk)
        except Exception as e:
            return JsonResponse({'msg': '参数异常'}, status=400)

        # 3、获取json参数并转化为python中的数据类型(字典)
        try:
            python_data = json.loads(request.body)
        except Exception as e:
            return JsonResponse({'msg': '参数有误'}, status=400)

        # 需要进行大量数据校验 （非常复杂）

        # 使用反序列化操作，可以自动帮助校验
        # serializer11 = ProjectSerilizer(data=python_data)

        serializer11 = ProjectSerilizer(data=python_data)

        # 对数据进行校验
        if not serializer11.is_valid():
            return JsonResponse(serializer11.errors, status=400)

        # project_obj = Projects.objects.create(**serializer11.validated_data)

        # serializer = ProjectSerilizer(instance=project_obj)
        # return JsonResponse(serializer.data, status=201)

        '''
          #1、在创建序列化器对象时，仅仅只传递data参数，那么必须得调用is_valid()方法通过之后
          #2、可以使用创建序列化器对象,data属性，来获取序列化验出的数据(会把validated_data数据作为输入源，参照序列化器字段
        '''
        '''
        # return JsonResponse(serializer.data, status=201)
        '''

        '''

        # 4、更新数据
        # project_obj.name = python_data.get('name')
        # project_obj.leader = python_data.get('leader')
        # project_obj.is_execute = python_data.get('is_execute')
        # project_obj.desc = python_data.get('desc')
        # project_obj.save()
        '''

        # 4、更新数据
        '''
        # 4、更新数据
        #使用反序列化获取对应值
        # project_obj.name = serializer11.validated_data.get('name')
        # project_obj.leader = serializer11.validated_data.get('leader')
        # project_obj.is_execute = serializer11.validated_data.get('is_execute')
        # project_obj.desc = serializer11.validated_data.get('desc')
        # project_obj.save()
        project_obj = serializer.save()

        '''

        # 5、将读取的项目数据转化为字典
        '''
       # 5、将读取的项目数据转化为字典

        # python_dict = {
        #     'id': project_obj.id,
        #     'name': project_obj.name,
        #     'msg': '更新项目数据成功'
        # }

        # return JsonResponse(python_dict)
        '''

        '''
        # 1、如果在创建序列化器对象时，同时instance和data参数，使用序列化器对象调用save方法时，会自动调用序列化器类中的update方法
        # 2、update方法用于对数据进行更新操作
        # 3、序列化器类中的update方法，instance参数为待更新的模型对象，validated_data参数为校验通过之后的数据(一般字典类型)
        # 4、在调用save方法时，可以传递任意的关键字参数，并且会自动合并到validated_data宇典中
        # 5、update方法一般需要将更新成功之后模型对象返回
         '''
        serializer = ProjectSerilizer(instance=project_obj)
        return JsonResponse(serializer.data, status=201)

        # 5、将读取的项目数据转化为字典

        # serializer = ProjectSerilizer(instance=project_obj, data=python_data)

    def delete(self, request, pk):

        # 1、需要校验pk在数据库中是否存在

        # 2、读取主键为pk的项目数据
        try:
            project_obj = Projects.objects.get(id=pk)
        except Exception as e:
            return JsonResponse({'msg': '参数异常'}, status=201)

        # 3、执行删除

        project_obj.delete()

        return JsonResponse({'msg': '删除成功'}, status=204)






