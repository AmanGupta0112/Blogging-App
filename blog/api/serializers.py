from rest_framework import serializers
from blog.models import Post


class BlogPostSerializers(serializers.ModelSerializer):
    class Meta():
        model = Post
        
