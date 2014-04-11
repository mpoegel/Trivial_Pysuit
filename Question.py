class Question(object):

	# Constructor for the question object
	def __init__(self, text, keyword, ):
		self.doc = text
		self.removing = keyword
		
	#formats the string doc to contain only the part of the sentence that contains the key word	
	def make_question(self):	
		my_bool = False
		while  not my_bool :
			val = self.doc.find(". ")
			val2 = self.doc.find(self.removing)
			if val < val2:
				self.doc = self.doc[val + 2:]
			else:
				self.doc = self.doc[:val + 1]
				self.doc = self.doc.replace(self.removing, "__________")
				my_bool = True
		return self.doc		
	
    #checks if response variable is equal to the keyword
	def is_correct(self):
		guess = raw_input("Enter what you you think the blank space is:   ")
		if guess.lower() == self.removing.lower():
			print "You got it right, have some points: 10 points."
			return True
		else:
			print "WRONG! No points for you. The correct answer was %s." % (self.removing)	
			return False
		
	