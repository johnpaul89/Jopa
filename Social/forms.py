from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import UserProfile, Article, Comment, tags
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from django.contrib.admin.widgets import FilteredSelectMultiple

class EditProfileForm(UserChangeForm):
    email = forms.CharField(label="Email", widget=CKEditorWidget(attrs={'class': 'form-control', 'rows':'2', 'cols':'50'}))
    first_name = forms.CharField(label="First Name", widget=CKEditorWidget(attrs={'class': 'form-control', 'rows':'2', 'cols':'50'}))
    last_name = forms.CharField(label="Last Name", widget=CKEditorWidget(attrs={'class': 'form-control', 'rows':'2', 'cols':'50'}))
    class Meta:
        model = User
        exclude = ['password',]
        fields = (
            'email',
            'first_name',
            'last_name',
        )

class UserProfileForm(forms.ModelForm):
    description = forms.CharField(label="Description", widget=CKEditorWidget(attrs={'class': 'form-control', 'rows':'7', 'cols':'50'}))
    city = forms.CharField(label="Town/City", widget=CKEditorWidget(attrs={'class': 'form-control', 'rows':'2', 'cols':'50'}))
    website = forms.CharField(label="Website", widget=CKEditorWidget(attrs={'class': 'form-control', 'rows':'2', 'cols':'50'}))
    phone = forms.CharField(label="Phone Number", widget=CKEditorWidget(attrs={'class': 'form-control', 'rows':'2', 'cols':'50'}))
    class Meta:
        model = UserProfile
        fields= (
            'description',
            'city',
            'website',
            'phone',
        )

class NewArticleForm(forms.ModelForm):
    tags = forms.RadioSelect()
    class Meta:
        model = Article
        exclude = ['editor', 'pub_date', 'likes']


class EditArticleForm(forms.ModelForm):
    tags = forms.RadioSelect()
    class Meta:
        model = Article
        exclude = ['editor', 'pub_date', 'likes', 'article_image']


class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=CKEditorWidget(attrs={'class': 'form-control', 'placeholder': 'Text Goes here!!', 'rows':'4', 'cols':'50'}))
    class Meta:
        model = Comment
        fields = ('content',)
