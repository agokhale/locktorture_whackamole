import os
import time
import fcntl
import random

maxfiles=10
fcursor = maxfiles
lfd=range(maxfiles+1)
while ( fcursor > 0 ):
	print fcursor
	lfd[fcursor] = os.open ("adsf%d.file"%fcursor, os.O_CREAT|os.O_RDWR )
	fcursor -= 1


spacecursor = 900
while (spacecursor > 0 ):
	whichfile = spacecursor % maxfiles
	try:
		if (random.randint (0,1) == 0):
			print "lock %d"%whichfile
			fcntl.flock( lfd[whichfile], fcntl.LOCK_EX| fcntl.LOCK_NB)
		else:
			print "unlock %d"%whichfile
			fcntl.flock( lfd[whichfile], fcntl.LOCK_UN)
		time.sleep (0.100)
	except:
		print "err"
	spacecursor -=1


fcursor = maxfiles
while ( fcursor > 0 ):
	os.close ( lfd[fcursor]) 
	fcursor -= 1
	
	
