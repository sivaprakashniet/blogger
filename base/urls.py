from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from base import views
urlpatterns = [
    url(r'^$', login_required(views.home), name='home'),
]