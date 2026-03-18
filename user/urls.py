# urls.py（示例，需与你的项目匹配）
from django.urls import path
from . import views

urlpatterns = [
    # 登录路由（必须指向 loginView，渲染 login.html）
    path('login.html', views.loginView, name='login'),  # 关键：name="login" 需与模板中 {% url 'login' %} 匹配
    # 个人中心路由（指向 homeView，渲染 home.html）
    path('home/<int:page>/.html', views.homeView, name='home'),
    path('logout.html',views.logoutView,name='logout'),
    path('user.html', views.userView, name='user'),
]