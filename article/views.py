from rest_framework.response import Response
from rest_framework.generics import (get_object_or_404, GenericAPIView, 
    ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Article, Author
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
