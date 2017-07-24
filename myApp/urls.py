from django.conf.urls import url
from myApp import views

urlpatterns = [

url(r'^MyView/$', views.myView, name='MyView'),
url(r'^MySecondView/$', views.mySecondView, name='MySecondView'),
url(r'^MyList/$', views.MyList, name = 'MyList'),
url(r'^MyDetail/(?P<MyModel_id>\d+)/$', views.MyDetail, name = 'MyDetail')

]