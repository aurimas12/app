from rest_framework import serializers
from api.posts.models import Post, Tags, Description
from api.company.serializers import CompanySerializer

class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = '__all__'


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    description = DescriptionSerializer()
    tags = TagsSerializer()
    company = CompanySerializer()
    class Meta:
        model = Post
        fields = '__all__'
        


