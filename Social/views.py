from django.shortcuts import render, redirect, get_object_or_404
from django.http  import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import logout
from django.contrib import messages
from django.template.loader import render_to_string
from .forms import EditProfileForm, UserProfileForm, NewArticleForm, CommentForm, EditArticleForm
from .models import UserProfile, Article, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.db.models import Q


from avatar.conf import settings
from avatar.forms import PrimaryAvatarForm, DeleteAvatarForm, UploadAvatarForm
from avatar.models import Avatar
from avatar.signals import avatar_updated, avatar_deleted
from avatar.utils import (get_primary_avatar, get_default_avatar_url,
                          invalidate_cache)

# Create your views here.
def social(request):
    users = User.objects.all()
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


    return render(request, 'social/social.html', {"users": users, "latest_car_articles": latest_car_articles, "latest_tech_tips_articles": latest_tech_tips_articles, "latest_apps_websites_articles": latest_apps_websites_articles, "latest_general_discussion_articles": latest_general_discussion_articles, "latest_laptops_forum_articles": latest_laptops_forum_articles, "latest_off_topic_articles": latest_off_topic_articles, "latest_operating_systems_articles": latest_operating_systems_articles, "latest_programmes_forum_articles": latest_programmes_forum_articles, "latest_smartphones_tablets_articles": latest_smartphones_tablets_articles, "latest_sound_system_articles": latest_sound_system_articles, "latest_photography_videography_articles":latest_photography_videography_articles, "latest_tech_news_articles": latest_tech_news_articles, "latest_televisions_forum_articles": latest_televisions_forum_articles, "televisions_forum_articles": televisions_forum_articles, "tech_tips_articles": tech_tips_articles, "tech_news_articles": tech_news_articles, "photography_videography_articles": photography_videography_articles, "sound_system_articles": sound_system_articles, "programmes_forum_articles": programmes_forum_articles, "operating_systems_articles": operating_systems_articles, "off_topic_articles": off_topic_articles, "tech_tips_articles": tech_tips_articles, "smartphones_tablets_articles": smartphones_tablets_articles,
     "laptops_forum_articles": laptops_forum_articles, "general_discussion_articles": general_discussion_articles, "apps_websites_articles": apps_websites_articles, "car_articles": car_articles, "latest_car_articles": latest_car_articles})

@login_required
def login_view(request):
    return redirect('devices')

@login_required
def logout_view(request):
    logout(request)
    return redirect('devices')

@login_required
def super_profile(request):

    articles = Article.objects.filter().order_by('-id')
    comments = Comment.objects.filter().order_by('-id')
    likes = Article.objects.filter().order_by('-id')
    user = request.user

    page = request.GET.get('page', 1)
    paginator = Paginator(articles, 15)
    try:
        article_pages = paginator.page(page)
    except PageNotAnInteger:
        article_pages = paginator.page(1)
    except EmptyPage:
        article_pages = paginator.page(paginator.num_pages)

    page = request.GET.get('page', 1)
    paginator = Paginator(comments, 15)
    try:
        comment_pages = paginator.page(page)
    except PageNotAnInteger:
        comment_pages = paginator.page(1)
    except EmptyPage:
        comment_pages = paginator.page(paginator.num_pages)

    page = request.GET.get('page', 1)
    paginator = Paginator(likes, 15)
    try:
        like_pages = paginator.page(page)
    except PageNotAnInteger:
        like_pages = paginator.page(1)
    except EmptyPage:
        like_pages = paginator.page(paginator.num_pages)

    args = {'user': user, "article_pages": article_pages, "articles": articles, "comments": comments, "likes": likes}
    return render(request, 'registration/superprofile.html', args)

@login_required
def update_profile(request, pk=None):

    if pk:
        user = User.objects.get(pk=pk)
        articles = Article.objects.filter(editor__id=pk).order_by('-id')
        comments = Comment.objects.filter(user__id=pk, post__id=pk).order_by('-id')
        likes = Article.objects.filter(likes__id=pk).order_by('-id')

        page = request.GET.get('page', 1)
        paginator = Paginator(articles, 15)
        try:
            article_pages = paginator.page(page)
        except PageNotAnInteger:
            article_pages = paginator.page(1)
        except EmptyPage:
            article_pages = paginator.page(paginator.num_pages)

        page = request.GET.get('page', 1)
        paginator = Paginator(comments, 15)
        try:
            comment_pages = paginator.page(page)
        except PageNotAnInteger:
            comment_pages = paginator.page(1)
        except EmptyPage:
            comment_pages = paginator.page(paginator.num_pages)

        page = request.GET.get('page', 1)
        paginator = Paginator(likes, 15)
        try:
            like_pages = paginator.page(page)
        except PageNotAnInteger:
            like_pages = paginator.page(1)
        except EmptyPage:
            like_pages = paginator.page(paginator.num_pages)

    else:
        user = request.user

    args = {'user': user, "comment_pages": comment_pages, "like_pages": like_pages, "article_pages": article_pages, "articles": articles, "comments": comments, "likes": likes}
    return render(request, 'registration/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        user_form = EditProfileForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user = request.user
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('accountsprofilewithpk', pk=user.pk)
        else:
            messages.error(request, ('Please correct the error below.'))

    else:
        user_form = EditProfileForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)
        args = {'user_form': user_form, "profile_form": profile_form}
    return render(request, 'registration/edit_profile.html', args)

@login_required(login_url='/accounts/login/')
def new_article(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewArticleForm(request.POST or None, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.editor = current_user
            article.save()
            return redirect('edit_article', id=article.id)
    else:
        form = NewArticleForm()
    return render(request, 'social/new_article.html', {"form": form})

def edit_article(request, id):
    article = get_object_or_404(Article, id=id)
    if article.editor != request.user:
        raise Http404()
    if request.method == "POST":
        form = EditArticleForm(request.POST or None, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('readarticle', pk=article.pk)
    else:
        form = EditArticleForm(instance=article)

    return render(request, "social/article_edit.html", {"form": form, "article":article})

def delete_article(request, id):
    article = get_object_or_404(Article, id=id)
    if request.user != article.editor:
        raise Http404()
    article.delete()
    return redirect('carsforum')



def read_article(request, pk):
    article = get_object_or_404(Article, pk = pk)
    post = get_object_or_404(Article, pk=pk)
    comments = Comment.objects.filter(post=post, reply=None).order_by('-id')
    car_articles = Article.objects.filter(tags__name__startswith='Cars').order_by('-id')[:5]

    blog_object=Article.objects.get(id=pk)
    blog_object.article_views=blog_object.article_views+1
    blog_object.save()

    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True

    if request.method == "POST":
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(post=post, user=request.user, content=content, reply=comment_qs)
            comment.save
            # return redirect('readarticle', pk=article.pk)
    else:
        comment_form = CommentForm()

    if request.is_ajax():
        html = render_to_string('social/comments.html', {"article": article, "post": post, "comment_form":comment_form, "is_liked": is_liked, "total_likes": post.total_likes(), "comments":comments} ,request=request)
        return JsonResponse({ 'form': html })

    return render(request, "social/article.html", {"article": article, "post": post, "comment_form":comment_form, "is_liked": is_liked, "total_likes": post.total_likes(), "comments":comments})

def like_post(request):
    # post = get_object_or_404(Article, id=request.POST.get('post_id'))
    post = get_object_or_404(Article, id=request.POST.get('id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True

    args = {
        "post": post,
        "is_liked": is_liked,
        "total_likes": post.total_likes(),
    }
    if request.is_ajax():
        html = render_to_string('social/like_section.html', args, request=request)
        return JsonResponse({ 'form': html })

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/accounts/profile')
        else:
            return redirect('/accounts/change-password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
    return render(request, 'registration/change_password.html', args)



def cars_forum(request):
    articles = Article.car_articles()
    users = User.objects.all()
    comments = Comment.objects.all()
    popular_articles = Article.objects.annotate(Count('article_views')).filter(article_views__gt=5).order_by('-article_views')[:15]

    page = request.GET.get('page', 1)
    paginator = Paginator(articles, 15)
    try:
        article_pages = paginator.page(page)
    except PageNotAnInteger:
        article_pages = paginator.page(1)
    except EmptyPage:
        article_pages = paginator.page(paginator.num_pages)

    return render(request, 'social/cars.html', {"articles": articles, "article_pages": article_pages, "popular_articles": popular_articles, "comments": comments, "users": users})

def apps_websites(request):
    articles = Article.apps_websites_articles()
    users = User.objects.all()
    comments = Comment.objects.all()
    popular_articles = Article.objects.annotate(Count('article_views')).filter(article_views__gt=5).order_by('-article_views')[:15]

    page = request.GET.get('page', 1)
    paginator = Paginator(articles, 15)
    try:
        article_pages = paginator.page(page)
    except PageNotAnInteger:
        article_pages = paginator.page(1)
    except EmptyPage:
        article_pages = paginator.page(paginator.num_pages)

    return render(request, 'social/apps_and_websites.html', {"articles": articles, "article_pages": article_pages, "popular_articles": popular_articles, "comments": comments, "users": users})

def general_discussion(request):
    articles = Article.general_discussion_articles()
    users = User.objects.all()
    comments = Comment.objects.all()
    popular_articles = Article.objects.annotate(Count('article_views')).filter(article_views__gt=5).order_by('-article_views')[:15]

    page = request.GET.get('page', 1)
    paginator = Paginator(articles, 15)
    try:
        article_pages = paginator.page(page)
    except PageNotAnInteger:
        article_pages = paginator.page(1)
    except EmptyPage:
        article_pages = paginator.page(paginator.num_pages)

    return render(request, 'social/general_discussion.html', {"articles": articles, "article_pages": article_pages, "popular_articles": popular_articles, "comments": comments, "users": users})

def laptops_forum(request):
    articles = Article.laptops_forum_articles()
    users = User.objects.all()
    comments = Comment.objects.all()
    popular_articles = Article.objects.annotate(Count('article_views')).filter(article_views__gt=5).order_by('-article_views')[:15]

    page = request.GET.get('page', 1)
    paginator = Paginator(articles, 15)
    try:
        article_pages = paginator.page(page)
    except PageNotAnInteger:
        article_pages = paginator.page(1)
    except EmptyPage:
        article_pages = paginator.page(paginator.num_pages)

    return render(request, 'social/laptops.html', {"articles": articles, "article_pages": article_pages, "popular_articles": popular_articles, "comments": comments, "users": users})

def off_topic(request):
    articles = Article.off_topic_articles()
    users = User.objects.all()
    comments = Comment.objects.all()
    popular_articles = Article.objects.annotate(Count('article_views')).filter(article_views__gt=5).order_by('-article_views')[:15]

    page = request.GET.get('page', 1)
    paginator = Paginator(articles, 15)
    try:
        article_pages = paginator.page(page)
    except PageNotAnInteger:
        article_pages = paginator.page(1)
    except EmptyPage:
        article_pages = paginator.page(paginator.num_pages)

    return render(request, 'social/off_topic.html', {"articles": articles, "article_pages": article_pages, "popular_articles": popular_articles, "comments": comments, "users": users})

def operating_systems(request):
    articles = Article.operating_systems_articles()
    users = User.objects.all()
    comments = Comment.objects.all()
    popular_articles = Article.objects.annotate(Count('article_views')).filter(article_views__gt=5).order_by('-article_views')[:15]

    page = request.GET.get('page', 1)
    paginator = Paginator(articles, 15)
    try:
        article_pages = paginator.page(page)
    except PageNotAnInteger:
        article_pages = paginator.page(1)
    except EmptyPage:
        article_pages = paginator.page(paginator.num_pages)

    return render(request, 'social/operating_systems.html', {"articles": articles, "article_pages": article_pages, "popular_articles": popular_articles, "comments": comments, "users": users})

def photography_videography(request):
    articles = Article.photography_videography_articles()
    users = User.objects.all()
    comments = Comment.objects.all()
    popular_articles = Article.objects.annotate(Count('article_views')).filter(article_views__gt=5).order_by('-article_views')[:15]

    page = request.GET.get('page', 1)
    paginator = Paginator(articles, 15)
    try:
        article_pages = paginator.page(page)
    except PageNotAnInteger:
        article_pages = paginator.page(1)
    except EmptyPage:
        article_pages = paginator.page(paginator.num_pages)

    return render(request, 'social/photography_and_videography.html', {"articles": articles, "article_pages": article_pages, "popular_articles": popular_articles, "comments": comments, "users": users})

def programmes_forum(request):
    articles = Article.programmes_forum_articles()
    users = User.objects.all()
    comments = Comment.objects.all()
    popular_articles = Article.objects.annotate(Count('article_views')).filter(article_views__gt=5).order_by('-article_views')[:15]

    page = request.GET.get('page', 1)
    paginator = Paginator(articles, 15)
    try:
        article_pages = paginator.page(page)
    except PageNotAnInteger:
        article_pages = paginator.page(1)
    except EmptyPage:
        article_pages = paginator.page(paginator.num_pages)

    return render(request, 'social/programmes.html', {"articles": articles, "article_pages": article_pages, "popular_articles": popular_articles, "comments": comments, "users": users})

def smartphones_tablets(request):
    articles = Article.smartphones_tablets_articles()
    users = User.objects.all()
    comments = Comment.objects.all()
    popular_articles = Article.objects.annotate(Count('article_views')).filter(article_views__gt=5).order_by('-article_views')[:15]

    page = request.GET.get('page', 1)
    paginator = Paginator(articles, 15)
    try:
        article_pages = paginator.page(page)
    except PageNotAnInteger:
        article_pages = paginator.page(1)
    except EmptyPage:
        article_pages = paginator.page(paginator.num_pages)

    return render(request, 'social/smartphones_and_tablets.html', {"articles": articles, "article_pages": article_pages, "popular_articles": popular_articles, "comments": comments, "users": users})

def sound_system(request):
    articles = Article.sound_system_articles()
    users = User.objects.all()
    comments = Comment.objects.all()
    popular_articles = Article.objects.annotate(Count('article_views')).filter(article_views__gt=5).order_by('-article_views')[:15]

    page = request.GET.get('page', 1)
    paginator = Paginator(articles, 15)
    try:
        article_pages = paginator.page(page)
    except PageNotAnInteger:
        article_pages = paginator.page(1)
    except EmptyPage:
        article_pages = paginator.page(paginator.num_pages)

    return render(request, 'social/sound_system.html', {"articles": articles, "article_pages": article_pages, "popular_articles": popular_articles, "comments": comments, "users": users})

def tech_news(request):
    articles = Article.tech_news_articles()
    users = User.objects.all()
    comments = Comment.objects.all()
    popular_articles = Article.objects.annotate(Count('article_views')).filter(article_views__gt=5).order_by('-article_views')[:15]

    page = request.GET.get('page', 1)
    paginator = Paginator(articles, 15)
    try:
        article_pages = paginator.page(page)
    except PageNotAnInteger:
        article_pages = paginator.page(1)
    except EmptyPage:
        article_pages = paginator.page(paginator.num_pages)

    return render(request, 'social/tech_news.html', {"articles": articles, "article_pages": article_pages, "popular_articles": popular_articles, "comments": comments, "users": users})

def tech_tips(request):
    articles = Article.tech_tips_articles()
    users = User.objects.all()
    comments = Comment.objects.all()
    popular_articles = Article.objects.annotate(Count('article_views')).filter(article_views__gt=5).order_by('-article_views')[:15]

    page = request.GET.get('page', 1)
    paginator = Paginator(articles, 15)
    try:
        article_pages = paginator.page(page)
    except PageNotAnInteger:
        article_pages = paginator.page(1)
    except EmptyPage:
        article_pages = paginator.page(paginator.num_pages)

    return render(request, 'social/techtips.html', {"articles": articles, "article_pages": article_pages, "popular_articles": popular_articles, "comments": comments, "users": users})

def televisions_forum(request):
    articles = Article.televisions_forum_articles()
    users = User.objects.all()
    comments = Comment.objects.all()
    popular_articles = Article.objects.annotate(Count('article_views')).filter(article_views__gt=5).order_by('-article_views')[:15]

    page = request.GET.get('page', 1)
    paginator = Paginator(articles, 15)
    try:
        article_pages = paginator.page(page)
    except PageNotAnInteger:
        article_pages = paginator.page(1)
    except EmptyPage:
        article_pages = paginator.page(paginator.num_pages)

    return render(request, 'social/televisions.html', {"articles": articles, "article_pages": article_pages, "popular_articles": popular_articles, "comments": comments, "users": users})










@login_required
def add(request, extra_context=None, next_override=None,
        upload_form=UploadAvatarForm, *args, **kwargs):
    if extra_context is None:
        extra_context = {}
    avatar, avatars = _get_avatars(request.user)
    upload_avatar_form = upload_form(request.POST or None,
                                     request.FILES or None,
                                     user=request.user)
    if request.method == "POST" and 'avatar' in request.FILES:
        if upload_avatar_form.is_valid():
            avatar = Avatar(user=request.user, primary=True)
            image_file = request.FILES['avatar']
            avatar.avatar.save(image_file.name, image_file)
            avatar.save()
            messages.success(request, _("Successfully uploaded a new avatar."))
            avatar_updated.send(sender=Avatar, user=request.user, avatar=avatar)
            return redirect(next_override or _get_next(request))
    context = {
        'avatar': avatar,
        'avatars': avatars,
        'upload_avatar_form': upload_avatar_form,
        'next': next_override or _get_next(request),
    }
    context.update(extra_context)
    template_name = settings.AVATAR_ADD_TEMPLATE or 'avatar/add.html'
    return render(request, template_name, context)


@login_required
def change(request, extra_context=None, next_override=None,
           upload_form=UploadAvatarForm, primary_form=PrimaryAvatarForm,
           *args, **kwargs):
    if extra_context is None:
        extra_context = {}
    avatar, avatars = _get_avatars(request.user)
    if avatar:
        kwargs = {'initial': {'choice': avatar.id}}
    else:
        kwargs = {}
    upload_avatar_form = upload_form(user=request.user, **kwargs)
    primary_avatar_form = primary_form(request.POST or None,
                                       user=request.user,
                                       avatars=avatars, **kwargs)
    if request.method == "POST":
        updated = False
        if 'choice' in request.POST and primary_avatar_form.is_valid():
            avatar = Avatar.objects.get(
                id=primary_avatar_form.cleaned_data['choice'])
            avatar.primary = True
            avatar.save()
            updated = True
            invalidate_cache(request.user)
            messages.success(request, _("Successfully updated your avatar."))
        if updated:
            avatar_updated.send(sender=Avatar, user=request.user, avatar=avatar)
        return redirect(next_override or _get_next(request))

    context = {
        'avatar': avatar,
        'avatars': avatars,
        'upload_avatar_form': upload_avatar_form,
        'primary_avatar_form': primary_avatar_form,
        'next': next_override or _get_next(request)
    }
    context.update(extra_context)
    template_name = settings.AVATAR_CHANGE_TEMPLATE or 'avatar/change.html'
    return render(request, template_name, context)


@login_required
def delete(request, extra_context=None, next_override=None, *args, **kwargs):
    if extra_context is None:
        extra_context = {}
    avatar, avatars = _get_avatars(request.user)
    delete_avatar_form = DeleteAvatarForm(request.POST or None,
                                          user=request.user,
                                          avatars=avatars)
    if request.method == 'POST':
        if delete_avatar_form.is_valid():
            ids = delete_avatar_form.cleaned_data['choices']
            for a in avatars:
                if six.text_type(a.id) in ids:
                    avatar_deleted.send(sender=Avatar, user=request.user,
                                        avatar=a)
            if six.text_type(avatar.id) in ids and avatars.count() > len(ids):
                # Find the next best avatar, and set it as the new primary
                for a in avatars:
                    if six.text_type(a.id) not in ids:
                        a.primary = True
                        a.save()
                        avatar_updated.send(sender=Avatar, user=request.user,
                                            avatar=avatar)
                        break
            Avatar.objects.filter(id__in=ids).delete()
            messages.success(request,
                             _("Successfully deleted the requested avatars."))
            return redirect(next_override or _get_next(request))

    context = {
        'avatar': avatar,
        'avatars': avatars,
        'delete_avatar_form': delete_avatar_form,
        'next': next_override or _get_next(request),
    }
    context.update(extra_context)
    template_name = settings.AVATAR_DELETE_TEMPLATE or 'avatar/confirm_delete.html'
    return render(request, template_name, context)
