"""tradebooks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

from accounts.views import UserRegistrationView
from market.views import (
    NewBookView,
    HomeView,
    EditBookView,
    BookDetailsView,
    MyBooksListView)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),

    # User accounts
    url(r'^registration/$', UserRegistrationView.as_view(), name='user_registration'),
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/login/'}, name='logout'),

    # Book views
    url(r'^books/new/$', NewBookView.as_view(), name='new_book'),
    url(r'^books/my/$', MyBooksListView.as_view(), name='my_books'),
    url(r'^books/(?P<pk>\d+)/edit/$', EditBookView.as_view(), name='edit_book'),
    url(r'^books/(?P<pk>\d+)/$', BookDetailsView.as_view(), name='book_details'),    
]