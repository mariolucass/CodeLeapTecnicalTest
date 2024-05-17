from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from rest_framework.views import APIView, Request, Response, status

from .models import Post
from .serializers import PostSerializer

# With Generic Views.


class PostView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_url_kwarg = "post_id"


# Without Generic Views.

# class PostView(APIView):
#     def post(self, request: Request):
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)

#     def get(self, request: Request):
#         posts = Post.objects.all().order_by("id")
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


# class PostDetailView(APIView):
#     def patch(self, request: Request, post_id: int):
#         post = get_object_or_404(Post, id=post_id)
#         serializer = PostSerializer(post, request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def delete(self, request: Request, post_id: int):
#         post = get_object_or_404(Post, id=post_id)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
