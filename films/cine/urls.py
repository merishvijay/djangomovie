from django.contrib import admin
from django.urls import path

from cine import views
from cine import views


app_name="cine"
urlpatterns = [
    # path('',views.home,name="home"),
    path('',views.MovieList.as_view(), name="home"),

    # path('add', views.addfilms, name="add"),
     path('add',views.MovieAdd.as_view(), name="add"),
    # path('filmdetail/<int:p>' ,views.filmdetail,name="filmdetail"),

    path('filmdetail/<pk>', views.MovieDetail.as_view(), name="filmdetail"),


    # path('filmedit/<int:p>', views.filmedit, name="filmedit"),
    # path('filmedit/<pk>', views.MovieUpdate.as_view(), name="filmedit"),
     path('filmedit/<pk>/', views.MovieUpdate.as_view(), name="filmedit"),



    # path('filmdelete/<int:p>', views.filmdelete, name="filmdelete"),
    path('filmdelete/<pk>', views.MovieDelete.as_view(), name="filmdelete"),




    ]