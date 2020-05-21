from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.models import Post
from blog.api.serializers import BlogPostSerializers
import datetime

"""
When the GET request is called to the server,it show a status = ok if the server find any post related to that primary key
"""
@api_view(['GET',])
def api_detail_post_view(request,pk):
    try:
        blog_post = Post.objects.get(pk = pk)
        now = datetime.datetime.now()
        data = {}
        if now:
            data['status'] = 'OK'
        return Response(data = data)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
