"""auctionrush URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from . import views
from auctions import views as auctions_views

urlpatterns = [
    path('', auctions_views.index, name="index"),
    path('about/', auctions_views.about, name="about"),
    path('myauctions/', auctions_views.my_auctions, name="my_auctions"),
    path('mybids/', auctions_views.my_bids, name="my_bids"),
    path('auctions/', include('auctions.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/register", views.register, name="register"),
    path('admin/', admin.site.urls),
    path("successPage" , views.success , name="success")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
