#子路由
from django.urls import path

from projects import views

urlpatterns = [
    # path("projects/<int:pk>",views.get_projects),
    # path("get/",views.get_project),
    # path("creat/",views.creat_project),
    # path("put/",views.put_project),
    # path("delete/",views.delete_project),
    # path("projects/", views.projects1),

    # path("projects/", views.projects),

    #使用类调用视图
    #定义类视图的路由条目
    #类视图as_view()
    path('projects/<int:pk>/',views.ProjectcView.as_view())


]