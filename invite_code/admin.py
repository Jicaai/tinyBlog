from django.contrib import admin
from invite_code.models import Passwd, Person

class PasswdAdmin(admin.ModelAdmin):
	list_display=('id','passwd','status','distribute','usedip','usedtime','voteinfo')
	ordering=('status',)
	search_fields=('title',)
        list_filter = ('status',)

class PersonAdmin(admin.ModelAdmin):
	list_display=('id','name','unit','votes')
	ordering=('votes',)
	search_fields=('title',)
        list_filter = ('unit',)
        

admin.site.register(Passwd, PasswdAdmin)
admin.site.register(Person, PersonAdmin)
