"""
    路由login将实现用户注册与登录功能，路由的HTTP请求由视图函数loginView负责接收和处理。
"""

# user的views.py
# user的views.py
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from index.models import Dynamic
from user.models import *
from .form import MyUserCreationForm

# 用户注册与登录
def loginView(request):
    user_form = MyUserCreationForm()  # 变量名改为 user_form，避免与 request.user 冲突
    tips = ''
    if request.method == 'POST':
        # 1. 处理登录请求（前端传了 loginUser 参数）
        if request.POST.get('loginUser', ''):
            login_user = request.POST.get('loginUser', '')  # 用户名/手机号
            login_pwd = request.POST.get('password', '')    # 密码
            # 查找用户（支持手机号或用户名登录）
            try:
                # 这里修复：原代码 .first() 多余（get() 只能返回一个，加 first() 会报错）
                user = MyUser.objects.get(Q(mobile=login_user) | Q(username=login_user))
            except MyUser.DoesNotExist:
                tips = '用户不存在'
            else:
                # 校验密码（Django 的 check_password 会自动匹配哈希后的密码）
                if check_password(login_pwd, user.password):
                    login(request, user)  # 登录成功，初始化登录状态
                    return redirect(reverse('index'))
                else:
                    tips = '密码错误'
        # 2. 处理注册请求（前端没传 loginUser 参数）
        else:
            user_form = MyUserCreationForm(request.POST)
            # 表单验证通过：保存用户
            if user_form.is_valid():
                user_form.save()  # 关键：之前遗漏了保存用户，导致注册后无数据
                tips = '注册成功，请登录'
            else:
                # 提取第一个错误提示（优化用户体验）
                if user_form.errors.get('username'):
                    tips = user_form.errors['username'][0]
                elif user_form.errors.get('mobile'):
                    tips = user_form.errors['mobile'][0]
                else:
                    tips = '注册失败，请检查信息'
    # GET 请求：渲染登录页面（传递表单和提示）
    return render(request, 'login.html', {'user_form': user_form, 'tips': tips})

# 用户中心
# 设置用户登录限制
@login_required(login_url='/login.html')
def homeView(request, page):
    # 热搜歌曲
    searchs = Dynamic.objects.select_related('song').\
        order_by('-search').all()[:4]
    # 分页功能
    songs = request.session.get('play_list', [])
    paginator = Paginator(songs, 3)
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {
        "user": request.user,
    })
# 退出登录
def logoutView(request):
    logout(request)
    return redirect('login')
@login_required(login_url='/user/login.html')
def userView(request):
    return render(request, 'user.html', {"user": request.user})

