from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.shortcuts import reverse
from django.db.models import Q,F
from index.models import *


def searchView(request, page):
    if (request.method == 'GET'):
        searchs = Dynamic.objects.select_related('song').order_by('-search').all()[:6]

        # 关键修复：优先从 GET 请求获取新关键词，再用 session 兜底
        # 原来的逻辑是 kword = request.session.get('kword','')，会覆盖新搜索的关键词
        kword = request.GET.get('keyword', request.session.get('kword', ''))
        # 将最新关键词存入 session，确保分页时不丢失
        request.session['kword'] = kword

        # 搜索逻辑（不变，但现在 kword 是最新的）
        if kword:
            songs = Song.objects.filter(Q(name__icontains=kword)
                                        | Q(singer__icontains=kword)
                                        | Q(album__icontains=kword)
                                        ).order_by('release').all()
        else:
            songs = Song.objects.order_by('-release').all()[:50]

        # 分页功能（不变）
        paginator = Paginator(songs, 5)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)

        # 添加歌曲搜索次数（修复：搜索条件和上方一致，避免统计漏项）
        if kword:
            # 原来的 idList = Song.objects.filter(name__icontains=kword) 只匹配歌曲名
            idList = Song.objects.filter(Q(name__icontains=kword) | Q(singer__icontains=kword))
            for i in idList:
                dynamics = Dynamic.objects.filter(song_id=i.id)
                if dynamics:
                    dynamics.update(search=F('search') + 1)
                else:
                    dynamic = Dynamic(plays=0, search=1, download=0, song_id=i.id)
                    dynamic.save()

        # 传递数据到模板（确保 search_count 存在，用于页面显示结果数）
        return render(request, 'search.html', {
            'keyword': kword,
            'search_count': songs.count(),  # 确保这个变量存在，否则页面会显示错误
            'pages': pages,
            'songs': songs,  # 保留原变量，避免页面循环报错（后续可优化为循环 pages.object_list）
            'searchs': searchs
        })
    else:
        request.session['kword'] = request.session.get('kword', '')
        return redirect(reverse('search', kwargs={'page': 1}))