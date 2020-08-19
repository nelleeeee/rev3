from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


# 리스트 api뷰 이용 (클래스기반?) generics?
# class PublicPostListAPIView(generics.ListCreateAPIView):
#     queryset = Post.objects.filter(is_public=True)
#     serializer_class = PostSerializer

# APIView 기반 (클래스기반?)(장식자필요?)
# class PublicPostListAPIView(APIView):
#     def get(self, request):
#         qs = Post.objects.filter(is_public=True)
#         serializer = PostSerializer(qs, many=True)
#         return Response(serializer.data)


# public_post_list = PublicPostListAPIView.as_view()

#  특정 메소드만 사용하고 싶을때 사용하는 함수기반뷰
@api_view(["GET"])
def public_post_list(request):
    qs = Post.objects.filter(is_public=True)
    serializer = PostSerializer(qs, many=True)
    return Response(serializer.data)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
