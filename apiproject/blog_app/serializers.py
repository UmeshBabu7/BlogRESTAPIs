from rest_framework import serializers
from .models import Blog,Category,BlogComment
from django.urls import reverse


class BlogCommentSerializer(serializers.ModelSerializer):
    blog = serializers.StringRelatedField(read_only=True)
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = BlogComment
        fields = "__all__"


def blog_title_valid(value):
    if len(value) < 4:
        raise serializers.ValidationError("Blog title is very short")
    else:
        return value


class BlogSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Blog
        fields = "__all__"

    def get_comments(self, obj):
        comments = BlogComment.objects.filter(blog=obj)[:3]
        request = self.context.get('request')
        return {
            "comments": BlogCommentSerializer(comments, many=True).data,
            "all_comment_link": request.build_absolute_uri(reverse('blog_comment_list', kwargs={'blog_id': obj.id}))
        }
    
    

    def get_len_blog_title(self, object):
        return len(object.blog_title)
    
class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    category_name = serializers.CharField()
    category = BlogSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = "__all__"

    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.post_date = validated_data.get('post_date', instance.post_date)
        instance.is_public = validated_data.get('is_public', instance.is_public)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.save()
        return instance