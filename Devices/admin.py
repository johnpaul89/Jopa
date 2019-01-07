from django.contrib import admin
from .models import PhoneSpecs, PhoneReview, tags, ReviewComment, SpecsComment

# Register your models here.
admin.site.register(PhoneSpecs)
admin.site.register(PhoneReview)
admin.site.register(tags)

class ReviewCommentAdmin(admin.ModelAdmin):
    list_display = ('review_post', 'review_content')

admin.site.register(ReviewComment, ReviewCommentAdmin)

class SpecsCommentAdmin(admin.ModelAdmin):
    list_display = ('specs_post', 'specs_comment')

admin.site.register(SpecsComment, SpecsCommentAdmin)
