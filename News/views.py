# from django.shortcuts import render
# from .models import NewsArticle
#
# # Create your views here.
# def news(request):
#     news_articles = NewsArticle.objects.filter()
#     return render(request, 'news/news.html', {"news_articles": news_articles})
#
# def read_news_article(request, id):
#     try:
#         article = NewsArticle.objects.get(id=id)
#     except DoesNotExist:
#         raise Http404()
#     return render(request,"news/article.html", {"article":article})
