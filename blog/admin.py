from django.contrib import admin
from blog.models import Category
from blog.models import Entry
from blog.models import Link 

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}

admin.site.register(Category, CategoryAdmin)


class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}

admin.site.register(Entry, EntryAdmin)

class LinkAdmin(admin.ModelAdmin):
    prepopulate_fields = {'slug':['title']}

admin.site.register(Link, LinkAdmin)
