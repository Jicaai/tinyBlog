from django.dispatch import dispatcher
from django.db.models.signals import post_syncdb
# from Gen_passwd import models as passwd_app
from invite_code.models import Passwd
import invite_code.models

from django.dispatch import receiver

from random import choice
import string

def GenPasswd(length=8, chars= string.letters+string.digits):
	yield ''.join([choice(chars) for i in range(length)])



#@receiver(post_syncdb,sender=Passwd)
def pass_gen(sender, **kwargs):
	line1=list()
	for i in xrange(2000):
	    for item in GenPasswd():
		    line1.append(item)
	line2=list(set(line1))
	for str in line2:
		p=Passwd(passwd=str, status=1, usedip='0.0.0.0')
		p.save()


post_syncdb.connect(pass_gen, sender= invite_code.models)



