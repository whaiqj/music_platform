from django.contrib import admin
from django.urls import path,re_path,include
from django.views.static import serve
from django.conf import settings
from index import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("index.urls")),
    path('ranking.html',include("ranking.urls")),
    path('play/',include('play.urls')),
    path('comment/',include("comment.urls")),
    path('search/',include("search.urls")),
    path('user/',include("user.urls")),
    # 定义静态资源的路由信息（开发环境走 STATICFILES_DIRS，生产走 STATIC_ROOT）
    re_path('static/(?P<path>.*)', serve, {
        'document_root': settings.STATICFILES_DIRS[0] if getattr(settings, 'DEBUG', True) and getattr(settings, 'STATICFILES_DIRS', None) else settings.STATIC_ROOT
    }, name='static'),
    # 定义媒体资源的路由信息
    re_path('media/(?P<path>.*)',serve,{'document_root': settings.MEDIA_ROOT},name = 'media'),
]

handler404 = views.page_not_found
handler500 = views.page_error