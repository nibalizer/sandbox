#!/usr/bin/python

from BeautifulSoup import BeautifulSoup

import urllib
import re

#page = urllib.urlopen('http://www.tv-links.eu/tv-shows/Star-Trek--The-Next-Generation--TNG-_641/')
page = open('index.html')

soup = BeautifulSoup(page)

#for episode in soup('a', href='/tv-shows/Star-Trek--The-Next-Generation--TNG-_641/'):
#for episode in soup('ul'):
#    print len(episode)
#    print episode.attrMap['title']
#    for i in episode:
#        print i
#        print '#'
#lis = soup.findAll('li')
#lis = lis[12:]
#lis = lis[:-17]

#print len(lis[0])
#link = lis[0].findAll('a')

#print len(link)
#print link
#print lis[0]
#print lis[0].contents[1].contents
#for i in lis:
#    print i.contents[1]
#for i in lis[0].contents:
#    print i.encode('latin1')
eps = soup('a', href=re.compile('/tv-shows/Star-Trek--The-Next-Generation--TNG-_641/season.*'))

eps_byname = {}
for i in eps:
    #print i.attrMap['title'].encode('latin1')
    #print i.attrMap['href'].encode('latin1')

    name = i.attrMap['title'].encode('latin1')
    name = name.replace(' on Tv-links.eu', '')
    name = name.replace('Watch ', '')

    print name
    eps_byname[name] = i.attrMap['href'].encode('latin1')


