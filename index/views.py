# index的views.py
from django.shortcuts import render
from .models import *
from user.models import MyUser

def indexView(request):
    songDynamic = Dynamic.objects.select_related('song')
    # 热搜歌曲 (这里暂时用 popular 替代，实际可根据搜索次数筛选)
    searchs = songDynamic.order_by('-search').all()[:3]
    # 新歌推荐 (recommend 直接用 Song 模型)
    recommend = Song.objects.exclude(
        name='',
        singer='',
        img='',
        file=''
    ).order_by('-release').all()[:12]  # 获取前12首有完整信息的新歌
    # 热门歌曲 (popular)
    popular = songDynamic.order_by('-plays').all()[:12] # 获取前12首热门歌曲
    # 热门专辑 - 从歌曲中提取唯一专辑信息
    # 这里假设专辑信息存储在 Song 模型中，通过 distinct 获取不同的专辑
    albums = Song.objects.exclude(
        name='',
        singer='',
        img=''
    ).order_by('-release').distinct('name', 'singer')[:12]  # 获取前12个不同专辑
    # 为登录用户获取头像，如果未登录则使用默认头像
    user_avatar = None
    is_authenticated = request.user.is_authenticated
    if request.user.is_authenticated and hasattr(request.user, 'avatar') and request.user.avatar:
        user_avatar = request.user.avatar.url
    else:
        user_avatar = '/static/image/default-avatar.png' # 提供一个默认头像路径

    context = {
        'searchs': searchs,
        'recommend': recommend,
        'popular': popular,
        'user_avatar': user_avatar, 
        'is_authenticated': request.user.is_authenticated, # 传递登录状态
        'username': request.user.username if request.user.is_authenticated else '游客',
        'request': request,
    }
    return render(request, 'index.html', context)

def page_not_found(request, exception):
    return render(request,'404.html',status=404)
def page_error(request):
    return render(request,'404.html',status=500)