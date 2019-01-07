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
    latest_car_articles = Article.objects.filter(tags__name__startswith='Cars').order_by('-id')[:1]

    return render(request, 'social/social.html', {"users": users, "car_articles": car_articles, "latest_car_articles": latest_car_articles})

def cars_forum(request):
    articles = Article.car_articles()
    users = User.objects.all()
    comments = Comment.objects.all()

    return render(request, 'social/cars.html', {"articles": articles, "comments": comments, "users": users})

@login_required
def login_view(request):
    return redirect('social')

@login_required
def logout_view(request):
    logout(request)
    return redirect('social')

@login_required
def super_profile(request):

    articles = Article.objects.filter().order_by('-id')
    comments = Comment.objects.filter().order_by('-id')
    likes = Article.objects.filter().order_by('-id')
    user = request.user

    args = {'user': user, "articles": articles, "comments": comments, "likes": likes}
    return render(request, 'registration/superprofile.html', args)

@login_required
def update_profile(request, pk=None):

    if pk:
        user = User.objects.get(pk=pk)
        articles = Article.objects.filter(editor__id=pk).order_by('-id')
        comments = Comment.objects.filter(user__id=pk).order_by('-id')
        likes = Article.objects.filter(likes__id=pk).order_by('-id')
    else:
        user = request.user

    args = {'user': user, "articles": articles, "comments": comments, "likes": likes}
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
        form = EditArticleForm(request.POST or None, instance=article)
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