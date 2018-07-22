from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from blog import views
urlpatterns = [
    url(r'^$', login_required(views.BlogListView.as_view()), name='blogs'),
    url(r'add', login_required(views.BlogView.as_view()), name='create_blog'),
    url(r'edit/(?P<slug>[-\w]+)/$', login_required(views.BlogEditView.as_view()), name='update_blog'),
    url(r'(?P<slug>[-\w]+)/$', login_required(views.BlogDetailView.as_view()), name='view_blog'),
    url(r'delete/(?P<slug>[-\w]+)/$', login_required(views.BlogDetailView.as_view()), name='delete_blog')   
]