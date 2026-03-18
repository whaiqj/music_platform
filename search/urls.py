# urls.py 修复后
from django.urls import path
from .import views
from django.shortcuts import redirect, reverse
urlpatterns = [
    # 新增 page 参数，类型为 int，默认值 1
    path('<int:page>/', views.searchView, name='search'),
    # 新增默认路由：访问 /search/ 时自动跳转到 page=1
    path('', lambda request: redirect(reverse('search', kwargs={'page': 1})), name='search_default'),
]