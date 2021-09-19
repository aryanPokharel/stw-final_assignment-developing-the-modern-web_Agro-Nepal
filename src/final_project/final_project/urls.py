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
from django.urls import path, include
from home.views import aboutUs_view, joinus_view, market_view, home_view

from .views import allsaleitems_view, bucketlist_view, learn_view, ministryreport_view
from students.views import showform
from remarks.views import remarkpage_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('home/', home_view),
    # path('remarks.html', feedbacks_view),
    path('aboutus.html', aboutUs_view),
    path('joinus.html', joinus_view),
    path('bucketlist/', bucketlist_view),
    path('market.html', market_view),
    path('learn.html', market_view),

    path('workers/', include('workers.urls')),
    path('products/', include('products.urls')),
    path('automobiles/', include('automobiles.urls')),
    path('allsaleitems/', allsaleitems_view),
    path('learn/', learn_view),
    path('ministry_report/', ministryreport_view),
    path('students/', showform),
    path('remarks/', remarkpage_view),
    path('insiders/', include('insiders.urls')),

]
