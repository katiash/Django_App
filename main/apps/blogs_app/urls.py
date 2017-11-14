from django.conf.urls import url
from . import views  ###THIS line is within urls.py within your 
# specific app. Import views (views.py) from this directory to render
# views (logic) depending on route (url)!


urlpatterns = [
    url(r'^$', views.index), ### Now use the 'include' function to pull in our first_app.urls...
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<number>\d+)$', views.show),
    url(r'^(?P<number>\d+)/edit$', views.edit),
    url(r'^(?P<number>\d+)/delete$', views.destroy)
]
