from rest_framework import serializers
from .models import Blog

def name_valid(value):
    if len(value) < 4:
        raise serializers.ValidationError("Blog title is very short")
    else:
        return value


class BlogSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    name = serializers.CharField(validators = [name_valid])
    description = serializers.CharField()
    post_date = serializers.DateTimeField(required=False)
    is_public = serializers.BooleanField()
    slug = serializers.CharField(required=False)

    class Meta:
        model = Blog
        fields = "__all__"

        # fields = ['name', 'description', 'is_public', 'slug']
        # exclude = ['slug']

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Blog title and description can not be same")
        else:
            return data
    
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.post_date = validated_data.get('post_date', instance.post_date)
        instance.is_public = validated_data.get('is_public', instance.is_public)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.save()
        return instance