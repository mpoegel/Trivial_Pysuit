'''
Y-HACK 2K13
authors: Matt Poegel, Ben Mizmera, Andrew Batbouta
'''

import urllib2 
import parse_html as parse
from Question import *
import key_word
import os, sys
import random

def get_html(url):
	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	infile = opener.open(url)
	page = infile.read()
	return page
	
def get_paragraphs(raw_html):
	raw_p = parse.get_paragraphs(raw_html)

	result = ''
	for s in raw_p:
		stripped_p = parse.strip_html(s).strip('\n')
		
		if len(stripped_p) == 0:
			break
		try:
			result += parse.format_string(stripped_p) + ' '
		except: pass 
	
	return result
		
def pose_question(query, is_first, score):
	print 
	query = query.replace(' ','_')
	url = 'http://en.wikipedia.org/wiki/' + query #+ '&printable=yes'
	try:
		raw_html = get_html(url)
		paragraphs = get_paragraphs(raw_html)
	
		kw = key_word.key_remove(paragraphs)
		if kw == '######' or kw.lower() == query.lower(): raise
	except:
		if not is_first: 
			print 'End of the line! Thanks for playing!'
			end_game(score)
		else:
			os.system('cls')
			q = get_random_query()
			print 'Sorry, that query does not work. Let\'s use %s' %q
			url = 'http://en.wikipedia.org/wiki/' + q
			raw_html = get_html(url)
			paragraphs = get_paragraphs(raw_html)
			kw = key_word.key_remove(paragraphs)
	
	
	print 'Searching on %s' %url	
	q = Question(paragraphs, kw)
	
	print q.make_question()
	if q.is_correct(): 
		pose_question(kw, False, score + 10)
	else: end_game(score)

def get_random_query():
	qs = ['US', 'dog', 'kitten', 'europe', 'Star_Trek', 'Star_Wars', 'human', 'africa', 'hippo', 'einstein', 'facebook', \
		'lollipop', 'colors', 'fork', 'richard_nixon']
	r = random.randint(0, len(qs)-1)
	return qs[r]
	
def end_game(score):
	print
	print
	print 'Game Over!'
	print 'Final Score: %d' %score
	sys.exit()

########################################################################
if __name__ == '__main__':
	os.system('cls')
	print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
	print '@                                                        @'
	print '@      #   # # #  #  #     ###### #    # #  #####        @'
	print '@      #   # # # #   #     #    # #    # #      #        @'
	print '@      # # # # ##    #     #    # #    # #     #         @'
	print '@      # # # # # #   #     #    # #    # #    #          @'
	print '@      ## ## # #  #  #     #  # # #    # #   #           @'
	print '@      #   # # #   # #     ###### ###### #  #####        @'
	print '@                                                        @'
	print '@             A wiki-crawling trivia game!               @'
	print '@                                                        @'
	print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
	print 
	q = raw_input('Enter start query ==> ')
	score = 0
	score = pose_question(q, True, score)
	
	