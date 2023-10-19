'''
序列化与反序列化
序列化和反序列化是计算机科学中用于将数据结构或对象转换为可存储或传输的格式的过程。序列化是将数据转换为字节流或其他可存储格式的过程，而反序列化是将先前序列化的数据重新还原为原始数据结构或对象的过程。

序列化通常用于以下情况：

数据持久化：将数据保存到磁盘或数据库，以便在以后重新加载。

数据传输：将数据通过网络传输，例如在客户端和服务器之间或不同系统之间进行通信。

跨语言通信：允许不同编程语言之间的应用程序交换数据，因为序列化后的数据通常是与语言无关的。

对象状态保存：在某些编程语境中，可以使用序列化来保存对象的状态，以便稍后还原。

反序列化用于从序列化的数据中重新构建原始数据结构或对象，使其可以在程序中使用。

常见的序列化格式包括 JSON（JavaScript Object Notation）、XML（eXtensible Markup Language）、Protocol Buffers、Thrift 等。不同编程语言通常都提供了库或工具，以便进行序列化和反序列化操作。

总之，序列化和反序列化是在计算机编程中非常常见的操作，用于数据的持久化、通信和跨语言数据交换。

# 一、序列化器
# a.如果需要使用DRF框架来实现序列化、反列化、数据操作，在于应用中创建serializers.py文件
# b.文件名推荐命名为serializers.py'
#c，必须得继Serializer类或者Serializer于类
#d. 定义的序列化器类中，字名要与模型类中的宇名保持一致
#e.定义的序列化器类的字(美属性)为Field于美
#f. 默认定义哪些字段，那么哪些宇段就会返回前端


二、定义序列化器类
1.必须得继承Serializer类或者Serializer于类
2.定义的序列化器类中，字段名要与模型类中的字名保持一致
3.定义的序列化器类的字(类属性)为Field于类
4. 默认定义哪些宇段，那么哪些宇段就会返回前端
5.常用的序列化器字类型
    IntegerField ->int
    CharField-》str
    BooleanField -> bool
    DateTimeField -> datetime

6.可以在序列化器宇中指定不同的选项
    Iabel和heIp_text，与模型类中的verbose_name和help_text参数一样
    IntegerField，可以使用maxvalue指定最大值，min_value指定最小值
    CharField，可以使用maxlength指定最大长度，min_length指定最小长度
    required=False,表示这个字段不是必填项，默认不懈的话为必填项

# 7.定义的序列化器字段中，required默认为True，说明默认定义的宇段必须得输和输出
# 8.如果在序列化器宇段中，设置required=False，那么前端用户可以不传递改字段(校验时不会报错)
# 9.如果未定义模型类中的某个字段，那么该宇段不会输入，也不会输出
# 10.前必须的输入(反序列化输入) name (必须得校验)，但是不会要输出(序列化器输出)?
        如果某个参数指定了write_only=True，那么该宇段仅仅只输入(反序列化输入，做数据校验)，不会输出(序列化器输出)
        默认write_only为False#
# 11.前端可以不用传递，但是后端需要输出?如果某个参数指定了read only=True，
      那么该字段仅仅只输出(序列化器输出)，不会输入(反序列化输入，做数据校验)
      默认read_only为False
# 12.在序列化器类中定义的字段，默认allow null=False，该字段不允许传递null空值，如果指定allow null=True,工那么该字段允许传递
# 13.在序列化器类中定义CharField宇段，默认allow_blank=False，该字段不允许传递空字符串,
     如果指定allow_blank=True，那么该宇允许传递空宇符串
# 14.在序列化器类中定义的字段，可以使用default参数来指定默认值，如果指定了default参数，那么前端用户可以不用传递
    会将default指定的值作为入
'''

'''
# 1、可以在序列化器宇段上使用validators指定自定义的校验规则
# 2、validators必须得为序列类型(列表)，在列表中可以添加多个校验规则
# 3、DRF框架自带Uniquelalidator校验器，必须得使用queryset指定查询集对象，用于对该字段进行校验
# 4、UniqueValidator校验器，可以使用message指定自定义报错信息

# b.可以任意序列化器宇上使用error_messages来自定义错误提示信息
# c.使用校验选项名(校验方法名)作为key，把具体的错误提示信息作为value
'''
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Projects


# 自定义的序列化器类实际上也是Field的子类

class InterfaceSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


'''
# 1、可以在类外自定义校验函数
#2、第一个参数为待校验的值
#3、如果校验不通过，必须得抛出serializers.ValidationError(报错信息)异常，同时可以指定具体的报错信息
#4、需要将校验函数名放置到validators列表中


'''


def is_contains_keyword(value):
    if '项目' not in value:
        raise serializers.ValidationError('项目名称中必须得包含“项目”关键字')


class ProjectSerilizer(serializers.Serializer):
    # id = serializers.IntegerField(label='项目id',help_text='项目id',max_value=1000,min_value=1)
    # name = serializers.StringRelatedField()
    # leader = serializers.StringRelatedField()

    '''
    # 1、可以在序列化器宇段上使用validators指定自定义的校验规则
    # 2、validators必须得为序列类型(列表)，在列表中可以添加多个校验规则
    # 3、DRF框架自带Uniquelalidator校验器，必须得使用queryset指定查询集对象，用于对该字段进行校验
    # 4、UniqueValidator校验器，可以使用message指定自定义报错信息
    # 5、校验规则的执行颇序?
            对宇段类型进行校验 -》依次验证validators列表中的校验规则 -》从右到左依次验证其他规则 --》调用单字段校验方法-》调用多宇段联合校验方法validate方法

    '''
    # name = serializers.CharField(label='项目名称',help_text='项目名称',max_length=20,min_length=5,
    #                              error_messages={
    #                                  'min_length':'项目名称不能少于5位',
    #                                  'max_length': '项目名称不能超过20位',
    #                              },validators=[UniqueValidator(queryset=Projects.objects.all(),message='项目名称不能重复')])

    # 使用自定义校验函数
    name = serializers.CharField(label='项目名称', help_text='项目名称', max_length=20, min_length=5,
                                 error_messages={
                                     'min_length': '项目名称不能少于5位',
                                     'max_length': '项目名称不能超过20位',
                                 }, validators=[UniqueValidator(queryset=Projects.objects.all(), message='项目名称不能重复'),
                                                is_contains_keyword])

    leader = serializers.CharField(default='阿明', label='项目负责人', help_text='项目名称', required=False, allow_null=True,
                                   allow_blank=True)
    is_execute = serializers.BooleanField()
    update_time = serializers.DateTimeField(label='更新时间', help_text='更新时间', format='%Y年%m月%d日 %H:%M:%S', required=False)
    # creat_time = serializers.DateTimeField()

    '''
    # 1、如果定义了一个模型类中没有的字，并且该宇段需要输出《序列化输出)
    # 2、需要在create方法、update方法中的模型对象上，添加动态的属性即可
    '''

    # token = serializers.CharField(read_only=True)

    '''
    #3、如果定义了一个模型类中没有的字段，并且该字段需要输入 (反序列化输入)
    #4、需要在create方法、update方法调用之前，将该宇段pop调用
    '''
    # 短信校验码
    sms_code = serializers.CharField(write_only=True)

    '''
    #1、可以在序列化器类中对单个字段进行校验
    #2、单字段的校验方法名称，必须把validate_作为前缓，加上待校验的宇段名，如: validate_待校验的字段名
    #3、如果校验不通过，必须得返回serializers.ValidationError(具体报错信息’)异常
    # 4、如果校验通过，往往需要将校验之后的值，返回 
    # 5、如果该宇段在定义时添加的校验规则不通过，那么是不会调用单字段的校验方法
    '''

    # 在类的里面对单个字段校验
    def validated_leader(self, attr: str):
        if not attr.endswith('项目'):
            raise serializers.ValidationError('项目名称必须得以“项目”结尾')
        return attr

    '''
        # 1、可以在序列化器类中对多个宇段进行联合校验
        # 2、使用固定的validate方法，会接收上面校验通过之后的宇典数据 
        # 3、当所有字殷定义时添加的校验规则都通过，且每个字典的单字段校验方法通过的情况下，才会调用validate
        
        '''

    # 多字段校验
    def validate(self, attrs: dict):
        if len(attrs.get('leader')) <= 4 or not attrs.get('is_execute'):
            raise serializers.ValidationError('项目负责人名称长度不能少于4位或者is execute参数为False')
        return attrs

    '''
     # 1、to_internal_value方法，是所有字开始进行校验时入口方法(最先调用的方法)
     # 2、会依次对序列化器类的各个序列化器字段进行校验:
        对字段类型进行校验 -》依次验证validators列表中的校验规则 -》从右到左依次验证其他规则 -》调用单字段校验方法
        to_internal_value调用结束 -》调用多宇联合校验方法validate方法
        
       #对各个单字段校验结束后的数据进行修改 
        
    '''

    # super()函数用于调用父类的方法，以扩展或覆盖其行为。在这种情况下，它调用父类中的to_internal_value方法，并将data参数传递给父类方法
    # def to_internal_value(self, data):
    #     tmp =super().to_internal_value(data)
    #
    #     return tmp

    # # 1、to_representation方法，是所有字段开始进行序列化输出时的入口方法《最先调用的方法)
    # def to_representation(self, instance):
    #     tmp = super().to_representation(instance)
    #     return tmp

    def create(self, validated_data):
        myname = validated_data.pop('myname')
        myage = validated_data.pop('myage')
        validated_data.pop('sms_code ')
        project_obj = Projects.objects.create(**validated_data)
        project_obj.token = 'XXXXXXXXXXXXXXXXXX'

        return project_obj

    def update(self, instance, validated_data: dict):

        # 简单方式
        # for key,value in validated_data.items():
        #     setattr(instance,key,value)

        instance.name = validated_data.validated_data.get('name') or instance.name
        instance.leader = validated_data.validated_data.get('leader') or instance.leader
        instance.is_execute = validated_data.validated_data.get('is_execute') or instance.is_execute
        instance.desc = validated_data.validated_data.get('desc') or instance.desc
        instance.save()
        return instance

    '''
    #一、关联字段
    # 1、可以定义PrimaryKeyRelatedField来获取关联表的外键值
    # 2、如果通过父获取从表数 据，默认需要使用从表模型类名小写 set作为序列化器类中的关联字殿名称
    # 3、如果在定义模型类的外键字段时，指定了realated name参数那么会把realatedname参数名作为序列化器类中的关联字段
    # 4、PrimaryKeyRelatedField宇段，要么指定read only=True，要么指定queryset参数，否则会报错
    # 5、如果指定了read only=True，那么该字仅序列化输出
    # 6、如果指定了queryset参数(关联表的查询集对象)，用于对参数进行校验
    # 7、如果关联字良有多个值，那么必须添加many=True，一般义表获取从表数据时，关联字需要指定
            interfacesset = serializers.PrimaryKeyRelatedField(label='项目所属接口id，help text='项目所属接口id
                many=True, queryset=Interfaces. ob jects. all0， write only=True)
    

    '''

    # inter = serializers.PrimaryKeyRelatedField(label='项目所属接口id',help_text='项目所属接口id',
    #                                                     read_only=True,many=True,)

    # inter = serializers.PrimaryKeyRelatedField(label='项目所属接口id',help_text='项目所属接口id',
    #                                                     many=True,queryset=Interfaces.objects.all(),write_only=True)

    '''
    # 1、使用StringRelatedField字段，将关联字段模型类中的_str 方法的返回值作为该字段的值
    # 2、StringRelatedField宇段默认添加了read only=True，该字段仅序列化输出
    '''
    # interfaces_set = serializers.StringRelatedField(many=True)

    '''
    # 1、使用SlugRelatedField宇段，将关联模型类中的某个字段，作为该字段的值
    # 2、如果指定了read only=True，那么该宇仅序列化输出
    '''
    # 输出从表的某个项目名称
    # interfaces_set = serializers.SlugRelatedField(slug_field='name',many=True,read_only=True)

    interfaces_set = InterfaceSerializers(label='所属接口信息', help_text='所属接口信息', read_only=True, many=True)


'''
在许多编程语言中，"str" 和 "char" 是用于表示文本数据的不同数据类型。下面是它们的主要区别：

str (String):

"str" 是字符串类型，通常用于表示文本数据，可以包含多个字符。
字符串可以包含任意长度的字符序列，包括字母、数字、符号、空格等。
字符串通常用双引号或单引号括起来，例如："Hello, World!" 或 'Python'。
字符串可以进行多种文本处理操作，如拼接、分割、替换等。
char (Character):

"char" 是字符类型，通常用于表示单个字符。
字符类型只能包含一个字符，通常用单引号括起来，例如：'A' 或 '1'。
字符类型通常用于处理单个字符的数据，例如，在某些编程语境中，处理密码、键盘输入、字符匹配等。
总结来说，主要区别在于：

"str" 表示字符串，可以包含多个字符，用于表示文本数据。
"char" 表示字符，只包含一个字符，通常用于表示单个字符数据。
这些概念的具体实现和行为可能会因编程语言而异，所以确保查阅你正在使用的编程语言的文档以了解其详细规范。在某些编程语言中，甚至可能没有明确定义的 "char" 类型，而是使用单字符的 "str" 来代表字符。


在一些编程语境中，"char"（字符）可能用于表示单个字符，但在Django REST framework的serializers.CharField()中，它实际上用于表示字符串字段，而不是强制限制为单个字符。

serializers.CharField() 允许你定义字符串字段，而不限制它们只能包含单个字符。
这是因为在实际应用中，字符串字段通常需要包含文本信息，而不仅仅是单个字符。

所以，即使使用 serializers.CharField() 来定义字段，你可以成功返回字符串数据，而不仅仅是单个字符。这种命名可能会引起混淆，
但在Django REST framework中，serializers.CharField() 更接近一般编程语言中的字符串字段而不是单字符字段。
如果你需要限制为单字符，你可以使用其他方法或验证来实现。

'''

'''
StringRelatedField 和 serializers.CharField 都用于在 Django REST framework 的序列化器中处理字符串数据，但它们有不同的用途和行为。

StringRelatedField:

StringRelatedField 通常用于处理关联字段的字符串表示。当你有一个关联字段（例如，外键或多对多关系），它将该字段的值转换为字符串，通常是关联对象的主键字段的字符串表示。

它通常用于表示关联对象的字符串标识，而不是直接表示字段的值。例如，如果你有一个外键字段，StringRelatedField 将返回外键对象的主键值的字符串表示。

适用于展示关联对象的标识，而不是详细信息。

serializers.CharField:

serializers.CharField 用于处理一般字符串字段，可以包含任何文本数据。

它通常用于表示模型中的文本字段，例如名称、描述等。

适用于处理一般的文本字段，不一定需要关联到其他模型的字段。

要选择使用哪一个取决于你的需求。如果你需要在序列化时表示关联对象的标识，你可以使用 StringRelatedField。如果你只需要处理一般的文本字段，你可以使用 serializers.CharField。

'''


class ProjectModelSerializer(serializers.ModelSerializer):
    '''
    可以模型序列化器类
    #1、继承serializers.ModelSerializer类或其于类
    #2、需要在Meta内部类中指定model、fields类属性参数
    #3、mode1指定模型类(需要生成序列化器的模型类)
    #4、fields指定模型类中哪些宇段需要自动生成序列化器宇段
    #5、会给id主键、有指定auto_now_add或者auto_now参数的参数的DateTimeField字段，
        添加readonly=True，仅仅只进序列化输出
    #6、有设置unique=True的模型字段，会自动在validators列表中添加唯一约束校验validators=[<UniqueValidator(queryset=Projects.objects.all())>])
    #7、有设置default=True的模型宇段，会自动添加required=False
    #8、有设置null=True的模型宇段，会自动添加allow_null=True
    #9、有设置blank=True的模型宇段，会自动添加allow blank=True

    '''

    class Meta:
        model = Projects

        '''
        # fields指定模型类中哪些宇段需要自动生成序列化器宇段
        # a.如果指定为“__all__”，那么模型类中所有的字段都需要自动转化为序列化器字良
        # b.可以传递需要转化为序列化器字的模型字名元组
        # c..exclude指定模型类中哪些字段不需要转化为序列化器字段，其他的字段都需要转换为序列化字段
        '''
        # fields = "__all__"
        # fields = ('id', 'name', 'leader')
        exclude = ('creat_time', 'update_time')
