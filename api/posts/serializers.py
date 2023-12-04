from rest_framework import serializers
from api.posts.models import Post, Tags, Description


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    description = DescriptionSerializer()
    class Meta:
        model = Post
        fields = '__all__'
        

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'

