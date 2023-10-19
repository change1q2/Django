'''
URL configuration for djangoProject1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
'''
# 全局路由

from django.urls import path, include

# from projects.views import index
urlpatterns = [

    # path("index/",views.index),
    # path("get_project/",views.get_project),
    # path("creat_project/",views.creat_project),
    # path("put_project/",views.put_project),
    # path("delete_project/",views.delete_project),

    # path('projects/<int:pk>/',views.get_projects),
    # #re_path(r'^projects/(?P<pk>)/$', views.get_projects),
    # re_path(r'^projects/(?P<pk>\d+)/$', views.get_projects),
    #
    # path('project/put/',views.index),
    # path("project/",include('projects.urls')),

    path('',include('projects.urls'))


]
