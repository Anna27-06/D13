from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment


class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы
    # хотите видеть в таблице с товарами
    list_display = ('title', 'post_type', 'author')
    list_filter = ('title', 'post_type', 'author', 'category')
    search_fields = ('title', 'category__name')
    # генерируем список имён всех полей для более красивого отображения


class AuthorAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы
    # хотите видеть в таблице с товарами
    list_display = ('user', 'rating')
    list_filter = ('user', 'rating')
    search_fields = ('user',)


class CategoryAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы
    # хотите видеть в таблице с товарами
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


class CommentAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы
    # хотите видеть в таблице с товарами
    list_display = ('text', 'rating', 'post', 'user')
    list_filter = ('user', 'comment_time')
    search_fields = ('user', 'post__name')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment, CommentAdmin)