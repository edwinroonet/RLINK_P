"""rlink URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')) 
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from web import views
from web.view.CM import WCM010_S101, WCM010_U101, WCM020_S101, WCM020_U101, WCM021_S101, WCM021_S201, WCM021_U101, WCM031_S101, WCM031_U101
from web.view.CMM import WCM_110, WCM_200
from web.view.MB import WMB_100

urlpatterns = [
    
    path('MB/WMB_100', WMB_100.main, name='WMB_100'), #
    path('CMM/WCM_110', WCM_110.main, name='WCM_110'), #
    path('CMM/WCM_200', WCM_200.procPmsLang, name="WCM_200"), #

    path('CM/WCM010_S101', WCM010_S101.main, name='WCM010_S101'), #
    path('CM/WCM010_U101', WCM010_U101.main, name='WCM010_U101'), #
    path('CM/WCM020_S101', WCM020_S101.main, name='WCM020_S101'), #
    path('CM/WCM020_U101', WCM020_U101.main, name='WCM020_U101'), #
    path('CM/WCM021_S101', WCM021_S101.main, name='WCM021_S101'), #
    path('CM/WCM021_S201', WCM021_S201.main, name='WCM021_S201'), #
    path('CM/WCM021_U101', WCM021_U101.main, name='WCM021_U101'), #
    path('CM/WCM031_S101', WCM031_S101.main, name='WCM031_S101'), #
    path('CM/WCM031_U101', WCM031_U101.main, name='WCM031_U101'), #

    #path('', WMB_100.main, name='WMB_100'), #디폴트경로
    path('', WMB_100.main, name='WMB_100'), #디폴트경로

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


''''
프린트 오토핏, 가로 맞춤, 가리기 noprinttag
'''