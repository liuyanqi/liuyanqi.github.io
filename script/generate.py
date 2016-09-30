from __future__ import print_function

log = open("text.txt", 'w')

for i in range(1,51):

	x = '<a href="img/journal/thumb/%d_thumb.jpg" data-gallery><img src="img/journal/thumb/%d_thumb.jpg" width="84" height="84"/></a>\n' % (i,i)

	log.write(x)
