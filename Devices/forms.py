from django.contrib.auth.models import User
from django import forms
from .models import ReviewComment, SpecsComment
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ReviewCommentForm(forms.ModelForm):
    review_content = forms.CharField(label="", widget=CKEditorWidget(attrs={'class': 'form-control', 'placeholder': 'Comment Goes here!!', 'rows':'4', 'cols':'50'}))
    class Meta:
        model = ReviewComment
        fields = ('review_content',)

class SpecsCommentForm(forms.ModelForm):
    specs_comment = forms.CharField(label="", widget=CKEditorWidget(attrs={'class': 'form-control', 'placeholder': 'Comment Goes here!!', 'rows':'4', 'cols':'50'}))
    class Meta:
        model = SpecsComment
        fields = ('specs_comment',)
