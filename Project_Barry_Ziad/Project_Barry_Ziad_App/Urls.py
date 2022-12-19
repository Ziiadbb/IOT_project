from . import views,api
from django.urls import path

urlpatterns = [
    path('data/', views.test, name='Data'),
    path('',views.home,name='home'),
##api
    path('api/list',api.Dlist,name='DHT11list'),
##genericViews
    path('api/post',api.Dhtviews.as_view(),name='DHT_post'),

]
