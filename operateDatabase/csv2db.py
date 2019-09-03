#!/usr/bin/env python
#coding:utf-8
  
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "operateDatabase.settings")
  

  
import django
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()
  
  
def main():
    from movie.models import Movie
    f = open('data.csv',encoding='utf8')
    for line in f:
        #电影名,年份,地区,剧情类型,导演,主演,评分,评论人数,简介
        print(line)
        title,year,area,type,doctor,stars,rate,num,desc = line.split(',')
        Movie.objects.create(title=title,
                             year=year,
                             area=area,
                             type=type,
                             doctor=doctor,
                             stars=stars,
                             rate=rate,
                             num=num,
                             desc=desc)
    f.close()
  
if __name__ == "__main__":
    main()
    print('Done!')