# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from invite_code.models import Passwd, Person

ERROR_INFO={
		0:'初始状态',
		1:'没有按要求数量check或者填写验证码',
		2:'验证码不正确',
		3:'验证码已经被使用',
		100:'success',
		}
VOTE_MIN = 0
VOTE_MAX = 10 


def vote_filter(num):
	# if the vote value is right

	return int(num)


def checked(request):
	votes = request.POST.getlist('votes')
	code = request.POST.get('invitation','')
	guest_ip = request.META['REMOTE_ADDR']
	guest_agent = request.META['HTTP_USER_AGENT']

	if (VOTE_MIN<len(votes)<VOTE_MAX) and code:
		try:
			result=Passwd.objects.get(passwd__exact=str(code))
		except Passwd.DoesNotExist:
			error_code=2
                else:
			if result and (result.status==True):
				vote_lsit=[vote_filter(i) for i in votes]
				#print vote_lsit
				'''----------------- vote begin -------------'''
				for item in vote_lsit:
					try:check=Person.objects.get(id=item)
					except Person.DoesNotExist:
						pass
					else:
						check.votes+=1
						check.save()

				'''----------------- vote begin -------------'''
				# set status=False
				result.status=False
				result.usedip=guest_ip
				result.voteinfo=str(vote_lsit)
				result.save()
				error_code=100
			else:
				error_code=3
		finally:
			# all right
			return render_to_response('voteform/check_form.html',
					{'error_code':error_code,
						})
	elif votes or code:
		error_code=1
	else:
		error_code=0
	return render_to_response('voteform/check_form.html',
				{'error_code':error_code,
					})

def show(request):
	all_person = Person.objects.all()
	return render_to_response('voteform/show_info.html',
			{'all':all_person,
				})

def invite_codes(request):
	all_invite= Passwd.objects.all()
	return render_to_response('voteform/show_invite.html',
			{'all':all_invite,
				})
