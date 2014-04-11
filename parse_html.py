# ----------------------------------------------------------------

def remove_inbetween( in_s, c0, c1):
	# Remove all of the html tags
	result_str = ''
	in_tag = False
	for c in in_s:
		if c == c0:
			in_tag = True
		elif c == c1:
			in_tag = False
		elif not in_tag:
			result_str += c
	return result_str

# ----------------------------------------------------------------

def strip_html(in_s):
	# Remove everything inbetween the tag delimiters
	result = remove_inbetween( in_s, '<', '>' )
	result = remove_inbetween( result, '{', '}' )
	result = remove_inbetween( result, '[', ']' )
	result = remove_inbetween( result, '(', ')' )
	return result

def get_paragraphs(in_s):
	i = 0
	paragraphs = []
	p = ''
	in_paragraph = False
	while i < len(in_s)-3:
		if in_s[i:i+3] == '<p>':
			in_paragraph = True
			i += 2
		elif in_s[i:i+4] == '</p>':
			in_paragraph = False
			paragraphs.append(p)
			p = ''
			i += 3
		elif in_paragraph:
			p += in_s[i]
		
		i += 1
	return paragraphs
# ----------------------------------------------------------------

def format_string( rstring ):
	i = 0
	result = ''
	while i < len(rstring):
		c = rstring[i]
		if c.isalnum() or c == '.' or c == '!' or c == '?' or c == "'" or c == ' ' or c == '=' or c == '-' or c == ',':
			result += c 
		i += 1
	return result
