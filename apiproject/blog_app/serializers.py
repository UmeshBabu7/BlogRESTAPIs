from rest_framework import serializers
from .models import Blog,Category

def blog_title_valid(value):
    if len(value) < 4:
        raise serializers.ValidationError("Blog title is very short")
    else:
        return value


class BlogSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Blog
        fields = "__all__"

    def get_len_blog_title(self, object):
        return len(object.blog_title)
    
class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField()
    category = BlogSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        exclude = ['id',]

    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.post_date = validated_data.get('post_date', instance.post_date)
        instance.is_public = validated_data.get('is_public', instance.is_public)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.save()
        return instance