from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    description = models.CharField(max_length = 100, blank=True, null=True)
    city = models.CharField(max_length = 100, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    Profile_image = models.ImageField(upload_to = 'avatars/', blank=True)

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

class tags(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    tags = models.ManyToManyField(tags)
    post = RichTextUploadingField()
    editor = models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="likes", blank=True)
    article_views=models.IntegerField(default=0)
    article_image = models.ImageField(upload_to='social_articles/', blank=True)

    def __str__(self):
        return self.editor.username

    def total_likes(self):
        return self.likes.count()

    @classmethod
    def car_articles(cls):
        articles = cls.objects.filter(tags__name__startswith='Cars').order_by('-id')
        return articles

    @classmethod
    def apps_websites_articles(cls):
        articles = cls.objects.filter(tags__name__startswith='Apps_and_Website').order_by('-id')
        return articles

    @classmethod
    def general_discussion_articles(cls):
        articles = cls.objects.filter(tags__name__startswith='General_Discussion').order_by('-id')
        return articles

    @classmethod
    def laptops_forum_articles(cls):
        articles = cls.objects.filter(tags__name__startswith='Laptops').order_by('-id')
        return articles

    @classmethod
    def off_topic_articles(cls):
        articles = cls.objects.filter(tags__name__startswith='Off_Topic').order_by('-id')
        return articles

    @classmethod
    def operating_systems_articles(cls):
        articles = cls.objects.filter(tags__name__startswith='Operating_Systems').order_by('-id')
        return articles

    @classmethod
    def programmes_forum_articles(cls):
        articles = cls.objects.filter(tags__name__startswith='Programmes').order_by('-id')
        return articles

    @classmethod
    def smartphones_tablets_articles(cls):
        articles = cls.objects.filter(tags__name__startswith='SmartPhones_Tablets').order_by('-id')
        return articles

    @classmethod
    def sound_system_articles(cls):
        articles = cls.objects.filter(tags__name__startswith='Sound_System').order_by('-id')
        return articles

    @classmethod
    def photography_videography_articles(cls):
        articles = cls.objects.filter(tags__name__startswith='Photography_Videography').order_by('-id')
        return articles

    @classmethod
    def tech_news_articles(cls):
        articles = cls.objects.filter(tags__name__startswith='Tech_News').order_by('-id')
        return articles

    @classmethod
    def tech_tips_articles(cls):
        articles = cls.objects.filter(tags__name__startswith='Tech_Tips').order_by('-id')
        return articles

    @classmethod
    def televisions_forum_articles(cls):
        articles = cls.objects.filter(tags__name__startswith='Gaming_Televisions').order_by('-id')
        return articles


    @classmethod
    def search_by_title(cls,search_term):
        forums_search = cls.objects.filter(title__icontains=search_term)
        return forums_search

class Comment(models.Model):
    post = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    reply = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, related_name="replies")
    content = models.TextField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.post.title, str(self.user.username))


class Meta:
    ordering = ['name']
