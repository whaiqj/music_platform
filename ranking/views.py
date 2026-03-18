from django.shortcuts import render
from index.models import *
from django.views.generic import ListView
def rankingView(request):
    #热搜歌曲
    searchs = Dynamic.objects.select_related('song').order_by('-search').all()[:4]
    #歌曲分类列表
    labels = Label.objects.all()
    #歌曲列表信息
    t = request.GET.get('type','')
    if t:
        dynamic = Dynamic.objects.select_related('song').filter(song__label=t).order_by('-plays').all()[:6]
    else:
        dynamic = Dynamic.objects.select_related('song').order_by('-plays').all()[:6]
    return render(request,'ranking.html',locals())
class RankingList(ListView):
    context_object_name = 'dynamics'
    template_name = 'ranking.html'
    def get_queryset(self):
        t = self.request.GET.get('type','')
        if t:
            dynamics = Dynamic.objects.select_related('song').filter(song__label=t).order_by('-plays').all()[:6]
        else:
            dynamics = Dynamic.objects.select_related('song').order_by('-plays').all()[:6]
        return dynamics
    def get_context_data(self, **kwargs):
        context = super(RankingList, self).get_context_data(**kwargs)
        context['searchs'] = Dynamic.objects.select_related('song').order_by('-search').all()[:4]
        context['labels'] = Label.objects.all()
        return context
