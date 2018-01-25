#coding:utf-8
from django.contrib import admin
from .models import Post,Category,Tag
# Register your models here.

#定制我们的后台显示
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author',)   #当选中这个Post表时，标题栏会以这样的标题显示，需要注册到admin站点中才可以
#在django 创建的后台中注册我们应用中models 中定义的数据库配置
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
