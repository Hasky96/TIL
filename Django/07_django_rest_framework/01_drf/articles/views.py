from django.shortcuts import get_list_or_404, get_object_or_404, render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def article_list(request):
    # 전체 게시글 조회
    if request.method == 'GET':
        articles=get_list_or_404(Article)
        serializers = ArticleListSerializer(articles, many=True)
        return Response(serializers.data)
    
    elif request.method == 'POST':
        serializers = ArticleSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        # return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializers = ArticleSerializer(article)
        return Response(serializers.data)

    elif request.method == 'DELETE':
        data = {
            'delete' : f'데이터 {article.pk}번이 삭제 되었습니다.'
        }
        article.delete()
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
def comment_list(request):
    comments = get_list_or_404(Comment)
    # 개별 쿼리가 아닌 쿼리 셋 -> 복수, 많은 데이터 -> many=True
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        data ={
            'delete': f'{comment_pk}is deleted!',
            'comment': f'{comment.content}is deleted'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)



@api_view(['POST'])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)