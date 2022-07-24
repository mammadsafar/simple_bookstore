from django.contrib import admin
from .models import Book, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'text', 'created_at')
    list_filter = ('user', 'book', 'created_at')
    search_fields = ('user', 'book', 'text')
    # ordering = ('-created_at')


admin.site.register(Book)
# admin.site.register(Comment, CommentAdmin)
