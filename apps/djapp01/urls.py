"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

from apps.djapp01 import views
from apps.djapp01.views import DataAnalysisListView, ChartData_BF01, ChartData_MH01, ChartData_MH01_BF01

urlpatterns = [

    #path('accounts/', include('django.contrib.auth.urls')),

    #path('', views.v_home, name='v_home'),
    #path('admin/', admin.site.urls),
    path('hello/', views.v_home, name="v_hello"),

    path('listda', DataAnalysisListView.as_view(), name = 'v_data_analysis_list'),
    path('dacr/', views.v_data_analysis_create_auto, name="v_data_analysis_create_auto"),
    path('dadel/', views.v_data_analysis_del, name="v_data_analysis_del"),
    path('v_data_analysis_create_form', views.v_data_analysis_create_form, name="v_data_analysis_create_form"),
    path('v_data_analysis_create_post',views.v_data_analysis_create_post, name="v_data_analysis_create_post"),
    path('api/chart-bf01/data/', ChartData_BF01.as_view(), name="api-chart-bf01-data"),
    path('api/data/', views.chat_data_jason, name='api-data'),
    #path(r'^api/data/$', views.get_data, name='api-data'),
    path('v_data_analysis_charts_bf01', views.v_data_analysis_charts_bf01, name = "v_data_analysis_charts_bf01"),

    ##
    path('api/chart-mh01/data/', ChartData_MH01.as_view(), name="api-chart-mh01-data"),
    path('v_data_analysis_charts_mh01', views.v_data_analysis_charts_mh01, name="v_data_analysis_charts_mh01"),
    path('api/chart-mh01-bf01/data/', ChartData_MH01_BF01.as_view(), name="api-chart-mh01-bf01-data"),
    path('v_data_analysis_charts_mh01_bf01', views.v_data_analysis_charts_mh01_bf01, name="v_data_analysis_charts_mh01_bf01"),
]

