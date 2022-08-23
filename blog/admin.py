from django.contrib import admin

from blog.models import Post, Category


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', ]
#
#
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['category', ]
#
#
admin.site.register(Category)
admin.site.register(Post)
