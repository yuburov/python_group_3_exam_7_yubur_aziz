"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from webapp.views import IndexView
from webapp.views.choise_views import ChoiseForPullCreateView, ChoiseUpdateView, ChoiseDeleteView
from webapp.views.poll_views import PollView, PollCreateView, PollUpdateView, PollDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('poll/<int:pk>/', PollView.as_view(), name='poll_view'),
    path('poll/create/', PollCreateView.as_view(), name='poll_create'),
    path('poll/<int:pk>/edit/', PollUpdateView.as_view(), name='poll_update'),
    path('poll/<int:pk>/delete/', PollDeleteView.as_view(), name='poll_delete'),
    path('poll/<int:pk>/add-choise/', ChoiseForPullCreateView.as_view(), name='poll_choise_create'),
    path('choise/<int:pk>/edit/', ChoiseUpdateView.as_view(), name='choise_update'),
    path('choise/<int:pk>/delete/', ChoiseDeleteView.as_view(), name='choise_delete'),
]
