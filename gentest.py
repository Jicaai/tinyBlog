import random
import string
def GenPasswd(length=8,chars=string.letters+string.digits):
	while True:
		yield ''.join(random.sample(chars,length))

if __name__=='__main__':
	line=list()
	number=8
	item=GenPasswd()
	for i in xrange(number):
		line.append(item.next())
	print len(line)
