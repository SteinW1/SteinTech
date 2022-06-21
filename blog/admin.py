from django.contrib import admin

from .models import Post, Article

admin.site.register(Post)
admin.site.register(Article)

admin.site.site_header = 'SteinTech Admin'
admin.site.index_title = 'Site Information and Data'
admin.site.site_title = 'SteinTech Admin'