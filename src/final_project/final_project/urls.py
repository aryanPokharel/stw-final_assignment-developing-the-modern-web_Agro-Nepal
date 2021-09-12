"""final_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from home.views import home_view, feedbacks_view, aboutUs_view, joinus_view, buysell_view, market_view, learn_view, automobiles_view, farmers_view
from workers.views import join_worker, joinform_view, updateworker_view
from automobiles.views import automobile_view, postautomobile_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('feedbacks.html', feedbacks_view),
    path('aboutus.html', aboutUs_view),
    path('joinus.html', joinus_view),
    path('buysell.html', buysell_view),
    path('market.html', market_view),
    path('learn.html', market_view),
    path('automobiles.html', automobiles_view),
    path('farmer.html', join_worker),
    path('joinform.html', joinform_view),
    path('update_form/<str:pk>/', updateworker_view, name='update_form'),
    path('automobile.html', automobile_view),
    path('postautomobile.html', postautomobile_view),


]
