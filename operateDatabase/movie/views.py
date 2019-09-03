from django.shortcuts import get_object_or_404,render
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.views import generic
from django.shortcuts import get_object_or_404,render

from pyecharts import Bar
from movie.models import Movie
# Create your views here.



def index(request):
    
    movie_list=Movie.objects.all()[1:]
    return render(request,'movie/index.html',{'movie_list':movie_list})
    
def search(request):
    title=request.POST['title']
    # print(title)
    movie_list=Movie.objects.filter(title__contains=title)
    return render(request,'movie/results.html',{'movie_list':movie_list})
   
def delete(request):
    choices=request.POST.getlist('choice')
    movie_list=[]
    for choice in choices:
        m=Movie.objects.get(id=choice)
        movie_list.append(m)
        m.delete()
    
    return render(request,'movie/deleted_results.html',{'movie_list':movie_list})
    
def add(request):
    
    try:
        title=request.POST['title']
        year=request.POST['year']
        area=request.POST['area']
        doctor=request.POST['doctor']
        rate=request.POST['rate']
        # print(title,year,area,doctor,rate)
        if title != '':
            Movie.objects.create(title=title,year=year,area=area,doctor=doctor,rate=rate)
    except:
        pass
    return render(request,'movie/add.html',)
    
    
def plot(request):
    movie_list=Movie.objects.all()[1:]
    years=[]
    for movie in movie_list:
        years.append(movie.year[:4])
        
    x,y=[],[]
    for year in range(1990,2020):
        x.append(year)
        y.append(years.count(str(year)))
    bar=Bar("柱状图","每年的电影产量")
    bar.add("电影数量",x,y, mark_line=["average"], mark_point=["max", "min"])
    print('生成图表')
    bar.render()
    f=open('render.html','r',encoding='utf8')
    html=f.read()
    f.close()
    return HttpResponse(html)