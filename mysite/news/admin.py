from django.contrib import admin

# Register your models here.
from.models import News, Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'category', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

#admin.site.register(News)
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

