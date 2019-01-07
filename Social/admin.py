from django.contrib import admin
from .models import UserProfile, Article, tags, Comment

# Register your model here.
admin.site.register(UserProfile)
admin.site.register(tags)

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)
    list_display = ('editor', 'title')

admin.site.register(Article, ArticleAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'content')

admin.site.register(Comment, CommentAdmin)
