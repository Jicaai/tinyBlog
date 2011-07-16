from django.shortcuts import render_to_response, get_object_or_404

from blog.models import Entry
from blog.models import Category
from django.views.generic.list_detail import object_list

#### the blow two are not needed anymore when use generic view ####
def entries_index(request):
    return render_to_response('blog/entry_index.html',
	    {'entry_list': Entry.objects.all()})

def entry_detail(request, year, month, day, slug):
    import datetime, time
    # why imported here
    date_stamp = time.strptime(year+month+day, "%Y%b%d")
    pub_date = datetime.date(*date_stamp[:3])
    entry = get_object_or_404(Entry, pub_date__year=pub_date.year,
	                           pub_date__month=pub_date.month,
				   pub_date__day=pub_date.day,
				   slug=slug)
    return render_to_response('blog/entry_detail.html',
                              {'entry':entry})

# category_list no required, generic view used
def category_list(request):
    return render_to_response('blog/category_list.html',
                              {'object_list':Category.objects.all()})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return object_list(request, queryset=category.live_entry_set.all(),
                       extra_context={'category': category})

