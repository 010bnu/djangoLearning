from django.urls import path

from . import views


# hard coding
# app_name='polls'
# urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:question_id>/',views.detail,name='detail'),
    # path('<int:question_id>/results/',views.results,name='results'),
    # path('<int:question_id>/vote/',views.vote,name='vote')
# ]

#generic view

app_name='movie'
urlpatterns=[
    path('',views.index,name='index'),
    path('results.html',views.search,name='search'),
    path('deleted_results.html',views.delete,name='delete'),
    path('add.html',views.add,name='add'),
    path('plot.html',views.plot,name='plot'),
]
