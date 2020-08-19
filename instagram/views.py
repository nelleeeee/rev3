from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer

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
# @api_view(["GET"])
# def public_post_list(request):
#     qs = Post.objects.filter(is_public=True)
#     serializer = PostSerializer(qs, many=True)
#     return Response(serializer.data)

# 클래스 기반뷰셋(모델뷰셋)에 액션데코레이터로 추가기능(새로운 엔드포인트) 구현
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=False, methods=["GET"])
    def public(self, request):
        qs = self.get_queryset().filter(is_public=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["PATCH"])
    def set_public(self, request, pk):
        instance = self.get_object()
        instance.is_public = True
        instance.save(update_fields=["is_public"])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


# RetrieveAPIView로 html랜더링 하기
class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "instagram/post_detail.html"

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        return Response({"post": post})
