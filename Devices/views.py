from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.http  import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.template.loader import render_to_string
from django.shortcuts import render_to_response
from Devices.models import PhoneSpecs, PhoneReview, SpecsComment, ReviewComment
from News.models import NewsArticle
from Social.models import Article, Comment
from .forms import ReviewCommentForm, SpecsCommentForm
from django.db.models import Q

# Create your views here.
def devices(request, pk=None):
    specs = PhoneSpecs.objects.filter().order_by('-id')[:10]
    reviews = PhoneReview.objects.filter().order_by('-id')[:10]
    articles = Article.objects.filter().order_by('-id')[:10]
    comments = Article.objects.all().order_by('-id')[:10]
    likes = Article.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(articles, 15)
    try:
        article_pages = paginator.page(page)
    except PageNotAnInteger:
        article_pages = paginator.page(1)
    except EmptyPage:
        article_pages = paginator.page(paginator.num_pages)

    car_articles = Article.car_articles()
    apps_websites_articles = Article.apps_websites_articles()
    general_discussion_articles = Article.general_discussion_articles()
    laptops_forum_articles = Article.laptops_forum_articles()
    off_topic_articles = Article.off_topic_articles()
    operating_systems_articles = Article.operating_systems_articles()
    programmes_forum_articles = Article.programmes_forum_articles()
    smartphones_tablets_articles = Article.smartphones_tablets_articles()
    sound_system_articles = Article.sound_system_articles()
    photography_videography_articles = Article.photography_videography_articles()
    tech_news_articles = Article.tech_news_articles()
    tech_tips_articles = Article.tech_tips_articles()
    televisions_forum_articles = Article.televisions_forum_articles()

    latest_car_articles = Article.objects.filter(tags__name__startswith='Cars').order_by('-id')[:1]
    latest_tech_tips_articles = Article.objects.filter(tags__name__startswith='Tech_Tips').order_by('-id')[:1]
    latest_apps_websites_articles = Article.objects.filter(tags__name__startswith='Apps_and_Website').order_by('-id')[:1]
    latest_general_discussion_articles = Article.objects.filter(tags__name__startswith='General_Discussion').order_by('-id')[:1]
    latest_laptops_forum_articles = Article.objects.filter(tags__name__startswith='Laptops').order_by('-id')[:1]
    latest_off_topic_articles = Article.objects.filter(tags__name__startswith='Off_Topic').order_by('-id')[:1]
    latest_operating_systems_articles = Article.objects.filter(tags__name__startswith='Operating_Systems').order_by('-id')[:1]
    latest_programmes_forum_articles = Article.objects.filter(tags__name__startswith='Programmes').order_by('-id')[:1]
    latest_smartphones_tablets_articles = Article.objects.filter(tags__name__startswith='SmartPhones_Tablets').order_by('-id')[:1]
    latest_sound_system_articles = Article.objects.filter(tags__name__startswith='Sound_System').order_by('-id')[:1]
    latest_photography_videography_articles = Article.objects.filter(tags__name__startswith='Photography_Videography').order_by('-id')[:1]
    latest_tech_news_articles = Article.objects.filter(tags__name__startswith='Tech_News').order_by('-id')[:1]
    latest_televisions_forum_articles = Article.objects.filter(tags__name__startswith='Televisions').order_by('-id')[:1]

    return render(request, 'index/index.html', {"specs": specs, "article_pages": article_pages, "latest_car_articles": latest_car_articles, "latest_tech_tips_articles": latest_tech_tips_articles, "latest_apps_websites_articles": latest_apps_websites_articles, "latest_general_discussion_articles": latest_general_discussion_articles, "latest_laptops_forum_articles": latest_laptops_forum_articles, "latest_off_topic_articles": latest_off_topic_articles, "latest_operating_systems_articles": latest_operating_systems_articles, "latest_programmes_forum_articles": latest_programmes_forum_articles, "latest_smartphones_tablets_articles": latest_smartphones_tablets_articles, "latest_sound_system_articles": latest_sound_system_articles, "latest_photography_videography_articles":latest_photography_videography_articles, "latest_tech_news_articles": latest_tech_news_articles, "latest_televisions_forum_articles": latest_televisions_forum_articles, "televisions_forum_articles": televisions_forum_articles, "tech_tips_articles": tech_tips_articles, "tech_news_articles": tech_news_articles, "photography_videography_articles": photography_videography_articles, "sound_system_articles": sound_system_articles, "programmes_forum_articles": programmes_forum_articles, "operating_systems_articles": operating_systems_articles, "off_topic_articles": off_topic_articles, "car_articles": car_articles, "laptops_forum_articles": laptops_forum_articles,
    "smartphones_tablets_articles": smartphones_tablets_articles, "general_discussion_articles": general_discussion_articles, "apps_websites_articles": apps_websites_articles, "reviews": reviews, "articles": articles, "likes": likes, "comments": comments})

def phone_specs(request):
    specifications = PhoneSpecs.objects.all().order_by('-id')[:1000]

    page = request.GET.get('page', 1)
    paginator = Paginator(specifications, 15)
    try:
        specs_pages = paginator.page(page)
    except PageNotAnInteger:
        specs_pages = paginator.page(1)
    except EmptyPage:
        specs_pages = paginator.page(paginator.num_pages)

    return render(request, 'specs/specs.html', {"specifications": specifications, "specs_pages": specs_pages})

def phone_reviews(request):
    reviews = PhoneReview.objects.filter().order_by('-id')[:1000]

    page = request.GET.get('page', 1)
    paginator = Paginator(reviews, 15)
    try:
        review_pages = paginator.page(page)
    except PageNotAnInteger:
        review_pages = paginator.page(1)
    except EmptyPage:
        review_pages = paginator.page(paginator.num_pages)

    return render(request, 'reviews/reviews.html', {"reviews": reviews, "review_pages": review_pages})

def review_article(request, pk):
    reviews = PhoneReview.objects.filter()
    reviewarticle = get_object_or_404(PhoneReview, pk = pk)
    reviewpost = get_object_or_404(PhoneReview, pk=pk)
    reviewcomments = ReviewComment.objects.filter(review_post=reviewpost, review_reply=None).order_by('-id')
    similar = PhoneReview.objects.all().order_by('-id')[:10]

    page = request.GET.get('page', 1)
    paginator = Paginator(reviews, 15)
    try:
        review_article_pages = paginator.page(page)
    except PageNotAnInteger:
        review_article_pages = paginator.page(1)
    except EmptyPage:
        review_article_pages = paginator.page(paginator.num_pages)

    is_liked = False
    if reviewpost.likes.filter(id=request.user.id).exists():
        is_liked = True

    if request.method == "POST":
        review_comment_form = ReviewCommentForm(request.POST or None)
        if review_comment_form.is_valid():
            reviewcontent = request.POST.get('review_content')
            reviewreply_id = request.POST.get('comment_id')
            review_comment_qs = None
            if reviewreply_id:
                review_comment_qs = ReviewComment.objects.get(id=reviewreply_id)
            reviewcomment = ReviewComment.objects.create(review_post=reviewpost, review_user=request.user, review_content=reviewcontent, review_reply=review_comment_qs)
            reviewcomment.save
            # return redirect('readarticle', pk=article.pk)
    else:
        review_comment_form = ReviewCommentForm()

    if request.is_ajax():
        html = render_to_string('reviews/review_comments.html', {"reviewarticle": reviewarticle, "reviewpost": reviewpost, "review_comment_form":review_comment_form, "is_liked": is_liked, "total_likes": reviewpost.total_likes(), "reviewcomments":reviewcomments} ,request=request)
        return JsonResponse({ 'form': html })

    return render(request, "reviews/review_article.html", {"reviews":reviews, "similar": similar, "review_article_pages": review_article_pages, "reviewarticle": reviewarticle, "reviewpost": reviewpost, "review_comment_form":review_comment_form, "is_liked": is_liked, "total_likes": reviewpost.total_likes(), "reviewcomments":reviewcomments})

def review_like_post(request):
    # post = get_object_or_404(Article, id=request.POST.get('post_id'))
    reviewpost = get_object_or_404(PhoneReview, id=request.POST.get('id'))
    is_liked = False
    if reviewpost.likes.filter(id=request.user.id).exists():
        reviewpost.likes.remove(request.user)
        is_liked = False
    else:
        reviewpost.likes.add(request.user)
        is_liked = True

    args = {
        "reviewpost": reviewpost,
        "is_liked": is_liked,
        "total_likes": reviewpost.total_likes(),
    }
    if request.is_ajax():
        html = render_to_string('reviews/review_like_section.html', args, request=request)
        return JsonResponse({ 'form': html })

def specs_article(request, pk):
    specifications = PhoneSpecs.objects.filter()

    page = request.GET.get('page', 1)
    paginator = Paginator(specifications, 10)
    try:
        specs_article_pages = paginator.page(page)
    except PageNotAnInteger:
        specs_article_pages = paginator.page(1)
    except EmptyPage:
        specs_article_pages = paginator.page(paginator.num_pages)

    specsarticle = get_object_or_404(PhoneSpecs, pk = pk)
    specspost = get_object_or_404(PhoneSpecs, pk=pk)
    specscomments = SpecsComment.objects.filter(specs_post=specspost, specs_reply=None).order_by('-id')

    is_liked = False
    if specspost.likes.filter(id=request.user.id).exists():
        is_liked = True

    if request.method == "POST":
        specs_comment_form = SpecsCommentForm(request.POST or None)
        if specs_comment_form.is_valid():
            specscomment = request.POST.get('specs_comment')
            specsreply_id = request.POST.get('comment_id')
            specs_comment_qs = None
            if specsreply_id:
                specs_comment_qs = SpecsComment.objects.get(id=specsreply_id)
            specscomment = SpecsComment.objects.create(specs_post=specspost, specs_user=request.user, specs_comment=specscomment, specs_reply=specs_comment_qs)
            specscomment.save
            # return redirect('readarticle', pk=article.pk)
    else:
        specs_comment_form = SpecsCommentForm()

    if request.is_ajax():
        html = render_to_string('specs/specs_comments.html', {"specsarticle": specsarticle, "specspost": specspost, "specs_comment_form":specs_comment_form, "is_liked": is_liked, "total_likes": specspost.total_likes(), "specscomments":specscomments} ,request=request)
        return JsonResponse({ 'form': html })

    return render(request, "specs/specs_article.html", {"specifications": specifications, "specs_article_pages": specs_article_pages, "specsarticle": specsarticle, "specspost": specspost, "specs_comment_form":specs_comment_form, "is_liked": is_liked, "total_likes": specspost.total_likes(), "specscomments":specscomments})

def specs_like_post(request):
    # post = get_object_or_404(Article, id=request.POST.get('post_id'))
    specspost = get_object_or_404(PhoneSpecs, id=request.POST.get('id'))
    is_liked = False
    if specspost.likes.filter(id=request.user.id).exists():
        specspost.likes.remove(request.user)
        is_liked = False
    else:
        specspost.likes.add(request.user)
        is_liked = True

    args = {
        "specspost": specspost,
        "is_liked": is_liked,
        "total_likes": specspost.total_likes(),
    }
    if request.is_ajax():
        html = render_to_string('specs/specs_like_section.html', args, request=request)
        return JsonResponse({ 'form': html })

def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_reviews_term = request.GET.get("article")
        search_specs_term = request.GET.get("article")
        # search_news_term = request.GET.get("article")
        search_forums_term = request.GET.get("article")

        searched_reviews_articles = PhoneReview.search_by_title(search_reviews_term).order_by('-id')[:50]
        searched_specs_articles = PhoneSpecs.search_by_title(search_reviews_term).order_by('-id')[:50]
        # searched_news_articles = NewsArticle.search_by_title(search_news_term).order_by('-id')[:50]
        searched_forums_articles = Article.search_by_title(search_forums_term).order_by('-id')[:50]

        message_reviews = f"{search_reviews_term}"
        # message_news = f"{search_news_term}"
        message_specs = f"{search_specs_term}"
        message_forums = f"{search_forums_term}"

        return render(request, 'index/search.html',{"message_reviews":message_reviews, "message_specs": message_specs, "message_forums": message_forums, "searched_reviews_articles": searched_reviews_articles,  "reviews_articles": searched_reviews_articles, "specs_articles": searched_specs_articles, "forums_articles": searched_forums_articles})

    else:
        message_reviews = "You haven't searched for any term"
        message_news = "You haven't searched for any term"
        message_specs = "You haven't searched for any term"
        message_forums = "You haven't searched for any term"

    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''

    ajax_search_reviews = PhoneReview.objects.filter(title__icontains=search_text)[:10]
    ajax_search_specs = PhoneSpecs.objects.filter(title__icontains=search_text)[:10]
    ajax_search_forums = Article.objects.filter(title__icontains=search_text)[:10]
    ajax_search_news = NewsArticle.objects.filter(title__icontains=search_text)[:10]
    ajax_search_forums_all = Article.objects.filter(title__icontains=search_text)
    ajax_search_news_all = NewsArticle.objects.filter(title__icontains=search_text)
    ajax_search_specs_all = PhoneSpecs.objects.filter(title__icontains=search_text)
    ajax_search_reviews_all = PhoneReview.objects.filter(title__icontains=search_text)

    return render(request, 'index/ajax_search.html', {"message_reviews":message_reviews, "ajax_search_reviews_all": ajax_search_reviews_all, "ajax_search_specs_all": ajax_search_specs_all, "ajax_search_forums_all": ajax_search_forums_all, "ajax_search_news_all" :ajax_search_news_all, "ajax_search_specs": ajax_search_specs, "ajax_search_forums": ajax_search_forums, "ajax_search_news": ajax_search_news, "ajax_search_reviews": ajax_search_reviews, "message_news": message_news, "message_specs": message_specs, "message_forums": message_forums})
