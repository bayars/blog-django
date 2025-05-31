from django.contrib import admin
from .models import Album, Photo

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'album', 'created_at', 'updated_at')
    list_filter = ('album', 'created_at', 'updated_at')
    search_fields = ('title', 'description') 