from django.conf.urls import url, include
from django.contrib import admin
# from myApp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main/', include('myApp.urls')),
]
