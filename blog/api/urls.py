from django.conf.urls import url
from blog.api.views import api_detail_post_view

app_name = 'blog'

urlpatterns = [

    url(r'(?P<pk>\d+)/', api_detail_post_view, name = 'detail'),

]
