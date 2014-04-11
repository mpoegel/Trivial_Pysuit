#!/usr/bin/env python
from __future__ import print_function
from alchemyapi import AlchemyAPI
import json
import random


alchemyapi = AlchemyAPI()

def key_remove( taext):
	rand_int= 0
	ret = '######'
	try:
		response = alchemyapi.entities( 'text' , taext, { 'sentiment':1 })
		if len(response['entities']) > 0 :
			rand_int  = random.randint( 0 , len( response['entities'])-1 )
			if response['status'] == 'OK':
				ret = response['entities'][rand_int]['text']
				
		response = alchemyapi.keywords('text', taext, { 'sentiment':1 })
		if len(response['keywords']) > 0 and rand_int == 0 :
			response = alchemyapi.keywords('text', taext, { 'sentiment':1 })
			rand_int = random.randint(0, len(response['keywords']))
			ret = response['keywords'][rand_int]['text']
		
	except: pass

	return ret
 
if __name__ == '__main__':
        test = 'Ben Franklin is a subspecies of the gray wolf , a member of the Canidae family of the mammalian order Carnivora. The term "domestic dog" is generally used for both domesticated and feral varieties. The dog was the first domesticated animal and has been the most widely kept working, hunting, and pet animal in human history. The word "dog" can also refer to the male of a canine species, as opposed to the word "bitch" which refers to the female of the species.'
        print (key_remove(test))
