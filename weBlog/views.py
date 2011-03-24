from django.shortcuts import render_to_response, get_object_or_404
from weBlog.models import Entry


def entries_index(request):
    return render_to_response('weBlog/entry_index.html',
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
    return render_to_response('weBlog/entry_detail.html',
                              {'entry':entry})
