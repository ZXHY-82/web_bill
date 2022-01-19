"""web_bill URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from bill import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('bill/login', views.login),
    path('bill/zzbill', views.zzbill),
    path('bill/register', views.register),

    # 支出账单管理
    path('bill/zzbill/outcome/list', views.outcome_list),
    path('bill/zzbill/outcome/add', views.outcome_add),
    path('bill/zzbill/outcome/<int:nid>/edit', views.outcome_edit),
    path('bill/zzbill/outcome/<int:nid>/delete', views.outcome_delete),


    # 收入账单管理
    path('bill/zzbill/income/list', views.income_list),
    path('bill/zzbill/income/add', views.income_add),
    path('bill/zzbill/income/<int:nid>/edit', views.income_edit),
    path('bill/zzbill/income/<int:nid>/delete', views.income_delete),


    #数据统计与分析
    path('bill/zzbill/analysis', views.analysis),
    path('bill/zzbill/analysis/bar', views.bar),
    path('bill/zzbill/analysis/pie', views.pie),

    path('bill/zzbill/<slug:year_month>/text', views.text),

]
