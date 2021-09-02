from django.contrib import admin
from .models import Article

#reordering the fields
class ArticleForm(admin.ModelAdmin):
    list_display=('body','approved')
    list_filter=['approved']
    search_fields=['body']


# Register your models here.
admin.site.register(Article,ArticleForm)
# admin.site.register(Article)
