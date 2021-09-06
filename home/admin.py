from django.contrib import admin
from .models import Category,Post

# customize category in admin
class Category_custom(admin.ModelAdmin):
    list_display=('Image','title','date',)
    search_fields=('title','date',)
    # list_filter=('post_category',)
    list_per_page=10

# customize Post in admin
class Post_custom(admin.ModelAdmin):
    list_display=('Image','title','date','post_category',)
    search_fields=('title','date',)
    list_filter=('post_category',)

# Register your models here.

admin.site.register(Category,Category_custom)
admin.site.register(Post,Post_custom)