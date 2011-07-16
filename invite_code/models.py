# -*- coding:utf-8 -*-
from django.db import models


DISTRIBUTE_CHOICES = (
		(0, 'no distribute'),
		(1, 'tz1'),
		(2, 'tz2'),
		(3, 'tz3'),
		(4, 'tz4'),
		(5, 'slb'),
		(6, 'zzb'),
		(7, 'hqb'),
		(8, 'zhzb'),
		(9, 'jsb'),
    )

class Passwd(models.Model):
	passwd=models.CharField(max_length=10, help_text='Maximum 10 characters.')
	distribute = models.IntegerField(choices=DISTRIBUTE_CHOICES,default=0)
	status = models.BooleanField()
	usedip = models.IPAddressField(blank=True)
	usedtime = models.DateTimeField(auto_now=True)
	#voteinfo = models.CommaSeparatedIntegerField(blank=True,max_length=40)
	voteinfo = models.CharField(blank=True,max_length=40)


	def __unicode__(self):
		return self.passwd

	class Meta:
		verbose_name_plural = "Passwords"


class Person(models.Model):
        id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=10)
	unit = models.IntegerField(choices=DISTRIBUTE_CHOICES,default=0)
	votes = models.IntegerField(default=0)
