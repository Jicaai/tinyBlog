from django.db import models
import datetime
from django.contrib.auth.models import User

from tagging.fields import TagField
from markdown import markdown

from django.conf import settings

class Category(models.Model):
    title = models.CharField(max_length=250, help_text='Maximum 250 characters.')
    slug = models.SlugField(unique=True, help_text="Suggested value automatically generated from title. Must be unique.")
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Categories'
    ordering = ['title']

    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/categories/%s/" % self.slug


class Entry(models.Model):
    title = models.CharField(max_length=250)
    excerpt = models.TextField(blank=True)
    body = models.TextField()
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    slug = models.SlugField(unique_for_date='pub_date')
    author = models.ForeignKey(User)
    enable_comments = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'),
    (DRAFT_STATUS, 'Draft'),
    (HIDDEN_STATUS, 'Hidden'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS)

    categories = models.ManyToManyField(Category)
    tags = TagField()
    excerpt_html = models.TextField(editable=False, blank=True)
    body_html = models.TextField(editable=False, blank=True)

    def save(self, force_insert=False, force_update=False):
        self.body_html = markdown(self.body)
	if self.excerpt:
	    self.excerpt_html = markdown(self.excerpt)
	super(Entry, self).save(force_insert, force_update)

    class Meta:
        verbose_name_plural = "Entries"
    ordering = ['-pub_date']

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('blog_entry_detail',(),{ 'year': self.pub_date.strftime("%Y"),
                                         'month': self.pub_date.strftime("%b").lower(),
                                         'day': self.pub_date.strftime("%d"),
                                         'slug': self.slug })
    #get_absolute_url = models.permalink(get_absolute_url)

class Link(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    description_html = models.TextField(blank=True)
    url = models.URLField(unique=True, verify_exists=False)
    post_by = models.ForeignKey(User)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    slug = models.SlugField(unique_for_date='pub_date',
                            help_text='Must be unique for the publication date.i')
    tags = TagField()
    enable_comments = models.BooleanField(default=True)
    post_elsewhere = models.BooleanField('Post to Delicious',
                                          default=True,
                                          help_text='If checked, this link will be post both to your weblog and you del.icio.us account.')
    via_name = models.CharField('Via', max_length=250, blank=True,
                                 help_text='The name of the person whose site you spotted the link on. Optional.')
    via_url = models.URLField('Via URL', blank=True,
                              help_text='The URL of the site where you spotted the link. Optional.')
    
    class Meta:
        ordering = ['-pub_date']
    def __uicode__(self):
        return self.title
    def save(self):
        '''if not self.id and self.post_elsewhere:
            import pydelicious
            from django.utils.encoding import smart_str
            pydelicious.add(settings.DELICIOUS_USER,
                            settings.DELICIOUS_PASSWORD,
                            smart_str(self.url),
                            smart_str(self.title),
                            smart_str(self.tags))'''
        if self.description:
            self.description_html = markdown(self.description)
        super(Link, self).save()

        def get_absolute_url(self):
            return ('blog_link_detail', (),
                    {'year': self.pub_date.strftime('%Y'),
                     'month': self.pub_date.strftime('%b').lower(),
                     'day': self.pub_date.strftime('%d'),
                     'slug': self.slug})
        get_absolute_url = models.permalink(get_absolute_url)
