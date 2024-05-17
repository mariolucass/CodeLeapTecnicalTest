from rest_framework import serializers

from .models import Post


# With Model Serializer
class PostSerializer(serializers.ModelSerializer):
    def update(self, instance: Post, validated_data: dict):
        items_to_update = ["title", "content"]

        for key in items_to_update:
            if key in validated_data:
                setattr(instance, key, validated_data[key])

        instance.save()
        return instance

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    class Meta:
        model = Post
        fields = ["id", "username", "created_datetime", "title", "content"]
        read_only_fields = ["id", "created_datetime"]


# Without Model Serializer

# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     username = serializers.CharField()
#     created_datetime = serializers.DateTimeField(read_only=True)
#     title = serializers.CharField()
#     content = serializers.CharField()

#     def update(self, instance: Post, validated_data: dict):
#         items_to_update = ["title", "content"]

#         for key in items_to_update:
#             if key in validated_data:
#                 setattr(instance, key, validated_data[key])

#         instance.save()
#         return instance

#     def create(self, validated_data):
#         return Post.objects.create(**validated_data)
