from django.contrib import admin
from .models import News, Comment
from redis import StrictRedis

cache = StrictRedis()


def purge_cache(modeladmin, request, queryset):
    cache.delete('*')


class NewsAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'updated_at',
        'get_image',
        'status'
    ]
    list_editable = ('status',)
    readonly_fields = ('get_image',)
    actions = [purge_cache]
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]


admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)