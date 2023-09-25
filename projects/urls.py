#子路由
from django.urls import path

from projects import views

urlpatterns = [
    path("projects/<int:pk>",views.get_projects),
    path("get/",views.get_project),
    path("creat/",views.creat_project),
    path("put/",views.put_project),
    path("delete/",views.delete_project),

]